#!/usr/bin/env python3
"""Consistency checks for the test suite documents.

The CSV, defect reports, traceability matrix and summary report all repeat the same
facts (case IDs, pass/fail counts, bug links). After a test run, when Actual_Result and
Status are edited by hand, it is easy for them to drift apart. This script catches that.

Usage: python3 scripts/check_suite.py
"""

import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES_CSV = ROOT / "docs" / "test-cases.csv"
RTM = ROOT / "docs" / "requirements-traceability-matrix.md"
SUMMARY = ROOT / "docs" / "test-summary-report.md"
BUGS_DIR = ROOT / "bugs"

COLUMNS = ["TC_ID", "Module", "Title", "Preconditions", "Test_Steps", "Test_Data",
           "Expected_Result", "Actual_Result", "Status", "Priority", "Severity"]
STATUSES = {"Pass", "Fail", "Blocked", "Not Run"}
PRIORITIES = {"High", "Medium", "Low"}
SEVERITIES = {"Critical", "Major", "Minor", "Trivial"}
BUG_FIELDS = ["Bug ID", "Severity", "Priority", "Status", "Environment",
              "## Preconditions", "## Steps to Reproduce", "## Expected Result",
              "## Actual Result", "## Notes", "## Attachments"]

TC_ID_RE = re.compile(r"\bTC-[A-Z]{2,3}-\d{2}\b")
BUG_ID_RE = re.compile(r"\bBUG-\d{3}\b")


def load_cases(errors):
    with CASES_CSV.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != COLUMNS:
            errors.append(f"test-cases.csv: header is {reader.fieldnames}, expected {COLUMNS}")
            return []
        rows = list(reader)

    seen = set()
    for line, row in enumerate(rows, start=2):
        tc = row["TC_ID"]
        where = f"test-cases.csv line {line} ({tc or 'no id'})"
        if not TC_ID_RE.fullmatch(tc):
            errors.append(f"{where}: TC_ID does not match TC-XXX-NN")
        if tc in seen:
            errors.append(f"{where}: duplicate TC_ID")
        seen.add(tc)
        for col in COLUMNS:
            if not row[col].strip():
                errors.append(f"{where}: {col} is empty")
        if row["Status"] not in STATUSES:
            errors.append(f"{where}: Status '{row['Status']}' not in {sorted(STATUSES)}")
        if row["Priority"] not in PRIORITIES:
            errors.append(f"{where}: Priority '{row['Priority']}' not in {sorted(PRIORITIES)}")
        if row["Severity"] not in SEVERITIES:
            errors.append(f"{where}: Severity '{row['Severity']}' not in {sorted(SEVERITIES)}")
    return rows


def check_bugs(cases, errors):
    bug_files = {p.name[:7]: p for p in BUGS_DIR.glob("BUG-*.md")}
    failing_by_bug = {}

    for row in cases:
        if row["Status"] != "Fail":
            continue
        bug_ids = BUG_ID_RE.findall(row["Actual_Result"])
        if not bug_ids:
            errors.append(f"{row['TC_ID']}: Status is Fail but Actual_Result names no BUG-NNN")
        for bug_id in bug_ids:
            if bug_id not in bug_files:
                errors.append(f"{row['TC_ID']}: references {bug_id}, which has no file in bugs/")
            failing_by_bug.setdefault(bug_id, set()).add(row["TC_ID"])

    for bug_id, path in sorted(bug_files.items()):
        text = path.read_text(encoding="utf-8")
        for field in BUG_FIELDS:
            if field not in text:
                errors.append(f"bugs/{path.name}: missing '{field}'")
        if f"| Bug ID | {bug_id} |" not in text:
            errors.append(f"bugs/{path.name}: Bug ID field does not match file name")
        if bug_id not in failing_by_bug:
            errors.append(f"bugs/{path.name}: no failed test case references {bug_id}")
        for tc in failing_by_bug.get(bug_id, ()):
            if tc not in text:
                errors.append(f"bugs/{path.name}: does not mention failing case {tc}")
    return bug_files


def check_rtm(cases, errors):
    text = RTM.read_text(encoding="utf-8")
    in_rtm = set(TC_ID_RE.findall(text))
    in_csv = {row["TC_ID"] for row in cases}
    for tc in sorted(in_csv - in_rtm):
        errors.append(f"RTM: {tc} is not mapped to any requirement")
    for tc in sorted(in_rtm - in_csv):
        errors.append(f"RTM: {tc} does not exist in test-cases.csv")


def check_summary(cases, bug_files, errors):
    text = SUMMARY.read_text(encoding="utf-8")
    counts = Counter(row["Status"] for row in cases)
    expected = {
        "Test cases planned": len(cases),
        "Passed": counts["Pass"],
        "Failed": counts["Fail"],
        "Defects logged": len(bug_files),
    }
    for label, value in expected.items():
        match = re.search(rf"^\| {re.escape(label)} \| (\d+)", text, re.MULTILINE)
        if not match:
            errors.append(f"summary report: no '{label}' row found")
        elif int(match.group(1)) != value:
            errors.append(f"summary report: '{label}' says {match.group(1)}, CSV gives {value}")


def heading_anchors(path):
    anchors = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            title = line.lstrip("#").strip().lower()
            anchors.add(re.sub(r"[^\w\- ]", "", title).replace(" ", "-"))
    return anchors


def check_links(errors):
    link_re = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
    for md in sorted(ROOT.rglob("*.md")):
        for target in link_re.findall(md.read_text(encoding="utf-8")):
            if re.match(r"[a-z]+:", target):
                continue
            file_part, _, anchor = target.partition("#")
            dest = (md.parent / file_part).resolve() if file_part else md
            rel = md.relative_to(ROOT)
            if not dest.exists():
                errors.append(f"{rel}: broken link to {target}")
            elif anchor and dest.suffix == ".md" and anchor not in heading_anchors(dest):
                errors.append(f"{rel}: link {target} points to a missing heading")


def main():
    errors = []
    cases = load_cases(errors)
    if cases:
        bug_files = check_bugs(cases, errors)
        check_rtm(cases, errors)
        check_summary(cases, bug_files, errors)
    check_links(errors)

    if errors:
        print(f"{len(errors)} problem(s) found:")
        for err in errors:
            print(f"  - {err}")
        return 1

    counts = Counter(row["Status"] for row in cases)
    print(f"OK: {len(cases)} cases ({counts['Pass']} pass, {counts['Fail']} fail), "
          f"{len(bug_files)} defect reports, all links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
