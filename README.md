# E-Commerce Manual Test Suite & Defect Portfolio

[![Check suite consistency](https://github.com/Hadi997-alt/ecommerce-manual-test-suite/actions/workflows/check-suite.yml/badge.svg)](https://github.com/Hadi997-alt/ecommerce-manual-test-suite/actions/workflows/check-suite.yml)

Manual functional, negative, boundary, and exploratory testing of an e-commerce web
application, with a complete QA documentation set: test plan, test cases, defect
reports, traceability matrix, and a test summary report.

The aim is to show the thinking behind manual QA: deciding what is worth testing and why,
writing cases someone else can run without guessing, reporting defects a developer can
reproduce from the steps alone, and turning results into a release decision.

## Application Under Test

[Automation Exercise](https://automationexercise.com), a public practice clothing store
with registration, login, a product catalogue with search and filters, a cart, checkout
with card entry, a downloadable invoice, and a contact form.

## Scope

**In scope:** registration, login, product search, cart, checkout, orders, account,
contact form, plus a cross-browser and mobile-viewport pass on the purchase path.

**Out of scope:** payment-gateway internals, performance, and security testing.
Injection-style strings are used in search and forms only to check that input is
handled as plain text.

## Test Approach

Risk-based manual testing across functional, negative, boundary, exploratory, UI, and
cross-browser dimensions. Checkout, payment entry, cart and invoice are rated high risk
because a failure there costs money, so they are tested first and most heavily.
Cases are designed with equivalence partitioning and boundary values (for example
quantities 0, 1 and 999), and exploratory sessions target the places where totals are
recalculated. The full reasoning is in the [Test Strategy](docs/test-strategy.md).

## Deliverables

| Artifact | Location | What it contains |
|---|---|---|
| Test Plan | [docs/test-plan.md](docs/test-plan.md) | Scope, environment, entry/exit criteria, risks, schedule |
| Test Strategy | [docs/test-strategy.md](docs/test-strategy.md) | Testing types, risk ratings, severity/priority scale, bug lifecycle |
| Test Cases | [docs/test-cases.csv](docs/test-cases.csv) | 59 cases across 9 modules with steps, data, expected and actual results |
| Defect Reports | [bugs/](bugs) | 6 reports, one per defect, ready to paste into Jira or Trello |
| Traceability Matrix | [docs/requirements-traceability-matrix.md](docs/requirements-traceability-matrix.md) | 21 requirements mapped to cases and defects |
| Test Summary Report | [docs/test-summary-report.md](docs/test-summary-report.md) | Results, risk areas, quality assessment, release recommendation |
| Evidence | [evidence/](evidence) | Screenshots captured during execution |

## Summary of Results

| Cases | Passed | Failed | Defects | Recommendation |
|---|---|---|---|---|
| 59 | 51 (86.4%) | 8 | 6 (1 Critical, 2 Major, 3 Minor) | **No-Go** until BUG-001 is fixed |

| Defect | Severity | Summary |
|---|---|---|
| [BUG-001](bugs/BUG-001_checkout-total-mismatch.md) | Critical | Invoice amount ignores quantity and differs from the checkout total |
| [BUG-003](bugs/BUG-003_cart-quantity-update.md) | Major | Quantity cannot be changed on the cart page |
| [BUG-006](bugs/BUG-006_payment-card-format-validation.md) | Major | Payment form accepts letters in the card number and an expired date |
| [BUG-002](bugs/BUG-002_login-error-message.md) | Minor | Upper-case version of a registered email fails login with a generic error |
| [BUG-004](bugs/BUG-004_search-no-results-handling.md) | Minor | Search with no matches shows a blank page with no message |
| [BUG-005](bugs/BUG-005_contact-form-validation.md) | Minor | Contact form accepts a whitespace-only name and an empty message |

Registration, account and cross-browser cases all passed. The failures cluster around
money (invoice, payment entry, cart) and around validation that only checks "not empty".

## How to Use This Repo

1. Read the [Test Plan](docs/test-plan.md) for context and scope.
2. Open [docs/test-cases.csv](docs/test-cases.csv) in Excel, Google Sheets or directly on
   GitHub. Filter `Status` = `Fail` to jump to the problems; each one names its bug ID.
3. Read the matching report in [bugs/](bugs).
4. Use the [Traceability Matrix](docs/requirements-traceability-matrix.md) to see which
   requirement each defect affects.
5. Finish with the [Test Summary Report](docs/test-summary-report.md) for the release call.

### Running the cases yourself

The cases are written to be executed in a browser against the live site. When re-running:

- Replace `<date>` in test emails with the current date so each run creates fresh accounts.
- Use only the dummy card data given in the cases.
- Save screenshots of every failure to `evidence/` using the file names listed in each
  bug report's Attachments section.
- If the site's behaviour differs from what is recorded, update `Actual_Result` and
  `Status` in the CSV, then the bug report and summary counts.

### Checking the documents stay consistent

The same facts appear in several files, so a small script verifies them after edits:

```bash
python3 scripts/check_suite.py
```

It needs only Python 3 (no packages) and checks that every case has all fields and valid
Status/Priority/Severity values, every failed case names an existing bug report and every
bug report is backed by a failed case, every case appears in the traceability matrix,
the pass/fail counts in the summary report match the CSV, and every relative link and
heading anchor in the Markdown files resolves. It runs on every push via GitHub Actions.

## Project Structure

```
├── docs/
│   ├── test-plan.md
│   ├── test-strategy.md
│   ├── test-cases.csv
│   ├── requirements-traceability-matrix.md
│   └── test-summary-report.md
├── bugs/                  one Markdown file per defect (BUG-001 … BUG-006)
├── evidence/              screenshots from execution
├── scripts/check_suite.py consistency check for the documents
└── .github/workflows/     runs the check in CI
```

## Decisions

- **CSV for test cases.** It opens in any spreadsheet tool for filtering and execution,
  renders as a table on GitHub, and diffs line by line in git, so result changes between
  runs are reviewable.
- **One file per defect.** Each report mirrors a tracker ticket and can be linked from the
  CSV, the matrix and the summary without duplication.
- **Requirements written by QA.** The site has no public requirements document, so the
  21 requirements in the matrix were derived from its visible features and common
  e-commerce behaviour. That assumption is stated in the matrix.
- **Severity and priority kept separate.** BUG-004 is Minor and P3, but BUG-002 is Minor
  and P2 because a customer who hits it cannot log in and has no recovery path.
- **Six defects rather than five.** The payment-format failures (TC-CHK-08, TC-CHK-09)
  did not fit any of the other reports, and every failed case must link to a defect, so
  they have their own report (BUG-006).

## Known Limitations

- Automation Exercise is a shared public demo. Its behaviour can change without notice, so
  recorded results reflect the cycle in which they were captured and should be
  re-verified before being quoted.
- Defects stay in **New** status: there is no development team to triage, fix or retest
  them, so the lifecycle in the strategy is documented but not exercised end to end.
- Mobile coverage uses a DevTools device preset, not a physical phone.

## Future Improvements

Automate the regression-critical happy paths listed at the end of the summary report:
see my API and UI automation repos.

## License

[MIT](LICENSE)

## Author

Abdul Hadi — QA Engineer · [GitHub](https://github.com/hadi997-alt) · [LinkedIn](https://linkedin.com/in/malik-hadi-a7b0a9319)
