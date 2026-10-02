# Test Strategy

How testing is done for the Automation Exercise store: which kinds of testing are used,
how effort is prioritised, and how defects are classified and tracked. The
[Test Plan](test-plan.md) covers scope, schedule and environment.

## 1. Testing Types

| Type | Used for | Example from this suite |
|---|---|---|
| Functional (positive) | Confirming each feature does what a customer expects with valid input | Register a new account and see "ACCOUNT CREATED!" (TC-REG-01) |
| Negative | Invalid, missing or unexpected input is rejected with a clear message | Log in with a wrong password (TC-LOG-03) |
| Boundary | Values at and just outside limits | Product quantity of 0, 1 and 999 (TC-PRD-08, TC-CRT-03, TC-CRT-04) |
| Exploratory | Timeboxed sessions on high-risk flows to find what scripted cases miss | Comparing the checkout total against the downloaded invoice led to BUG-001 |
| UI | Labels, messages, layout and navigation are correct and consistent | Empty search results give the user feedback (TC-PRD-05) |
| Cross-browser / responsive | The main purchase path works in Chrome, Firefox and Edge and on a mobile viewport | TC-UI-01 to TC-UI-03 |

Injection-style strings (`' OR '1'='1`, `<script>alert(1)</script>`) are used in search and
form fields only to check that input is handled safely and displayed as plain text. This
is input validation, not security testing, which is out of scope.

## 2. Risk-Based Prioritisation

Each module is rated on two questions: how much damage a failure causes (money, lost
orders, trust) and how often customers use it.

| Module | Business impact | Usage | Risk | Test priority |
|---|---|---|---|---|
| Checkout & payment entry | High: wrong totals or failed orders lose money | High | **High** | Executed first; every case High or Medium |
| Cart | High: feeds the checkout total | High | **High** | Executed early |
| Orders / invoice | High: the customer's financial record | Medium | **High** | Executed with checkout |
| Login / logout | Medium: blocks returning customers | High | **Medium** | |
| Registration | Medium: blocks new customers | Medium | **Medium** | |
| Products & search | Medium: affects discovery, not money | High | **Medium** | |
| Account | Medium | Low | **Low** | |
| Contact form | Low: support channel only | Low | **Low** | |

Case priority in the CSV follows this rating: **High** means it must pass before release,
**Medium** should pass, **Low** is nice to have.

## 3. Severity and Priority

Severity describes the impact of a defect on the user or business. Priority describes how
soon it should be fixed. They are set independently: a typo on the home page is Trivial
severity but could be High priority before a launch.

### Severity

| Severity | Definition | Example |
|---|---|---|
| Critical | Wrong money handling, data loss, or a core flow cannot be completed and there is no workaround | Order total on the invoice differs from the amount charged |
| Major | A feature does not work as intended; a workaround exists but is awkward | Cart quantity cannot be changed; item must be removed and re-added |
| Minor | Feature works, but behaviour is confusing or a validation is missing with limited impact | No message when a search returns nothing |
| Trivial | Cosmetic: spelling, alignment, colour | Misaligned footer text |

### Priority

| Priority | Definition |
|---|---|
| P1 – High | Fix before release |
| P2 – Medium | Fix in the current or next release |
| P3 – Low | Fix when convenient |

## 4. Defect Lifecycle

```
New ──► Open ──► In Progress ──► Fixed ──► Retest ──► Closed
         │                                    │
         ├──► Rejected (not a bug)            └──► Reopened ──► In Progress
         ├──► Duplicate
         └──► Deferred (accepted for a later release)
```

| Status | Meaning | Who moves it |
|---|---|---|
| New | Logged by QA, not yet triaged | QA |
| Open | Confirmed and accepted for fixing | Product owner / lead |
| In Progress | Developer is working on it | Developer |
| Fixed | Fix is in a build available for testing | Developer |
| Retest | QA is verifying the fix | QA |
| Closed | Fix verified; original case passes | QA |
| Reopened | Retest failed; back to the developer | QA |
| Rejected / Duplicate / Deferred | Not fixed in this cycle, with a reason recorded | Product owner |

Since there is no development team behind the public demo site, defects in this
portfolio stay in **New**. In a real project the same reports would be raised in Jira or on
a Trello board with columns matching the statuses above, and the report file would link
to the ticket.

## 5. Defect Report Fields

Every report in [`bugs/`](../bugs) uses the same fields so they can be pasted into a tracker
without reformatting: Bug ID, Title, Severity, Priority, Environment, Preconditions,
Steps to Reproduce, Expected Result, Actual Result, Status, Notes, Attachments.

A report is ready to submit when someone who has never seen the bug can reproduce it from
the steps alone, and the title says what is wrong and where (not "checkout broken").

## 6. Test Case Conventions

- IDs are `TC-<MODULE>-<NN>`: REG, LOG, PRD, CRT, CHK, ORD, ACC, CON, UI.
- One case checks one behaviour. Steps are numbered and specific enough to run without
  guessing which button or field is meant.
- `Status` is one of `Pass`, `Fail`, `Blocked`, `Not Run`. Every `Fail` names its bug ID
  in `Actual_Result`.
- `Severity` on a case is the impact if that case fails, used to judge which failures
  matter most during execution.
