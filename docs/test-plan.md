# Test Plan: Automation Exercise Web Store

| Field | Value |
|---|---|
| Document ID | TP-AE-01 |
| Application | [Automation Exercise](https://automationexercise.com) (public practice store) |
| Test cycle | Cycle 1: functional regression of the customer purchase journey |
| Author | Abdul Hadi |
| Version | 1.0 |

## 1. Introduction

Automation Exercise is a public demo clothing store used for QA practice. It has the
flows a real storefront has (sign-up, login, product catalogue, search, cart, checkout
with card entry, an order confirmation with a downloadable invoice, and a contact form),
which makes it a realistic target for manual test design.

This plan defines what is tested in Cycle 1, how it is tested, what has to be true to
start and finish, and what could get in the way. The testing types, prioritisation rules
and defect classification are in the companion [Test Strategy](test-strategy.md).

## 2. Objectives

1. Confirm that a new customer can register, log in, find a product, add it to the cart,
   check out, pay, and receive an order confirmation and invoice.
2. Check that each form rejects missing, malformed and boundary input with a clear message
   instead of failing silently or accepting bad data.
3. Find and report defects with enough detail that a developer can reproduce them without
   asking follow-up questions.
4. Give a release recommendation backed by pass/fail data and open-defect severity.

## 3. Scope

### 3.1 In scope

| Module | What is covered |
|---|---|
| Registration | Sign-up form, mandatory fields, duplicate email, password and date-of-birth input, account-created flow |
| Login / logout | Valid and invalid credentials, empty fields, error messages, session state after logout |
| Products & search | Product list, product detail page, category and brand filters, keyword search including special characters and injection-style strings |
| Cart | Add from list and detail page, quantities, line totals, remove item, cart persistence after login |
| Checkout & payment entry | Login gate, address review, order total, order comment, card form validation, order placement |
| Orders | Order confirmation page and invoice download |
| Account | Logged-in header state, account deletion, newsletter subscription |
| Contact form | Mandatory fields, email format, file upload, submission confirmation |
| UI / cross-browser | Navigation, responsive layout on a mobile viewport, behaviour in Chrome, Firefox and Edge |

### 3.2 Out of scope

| Area | Reason |
|---|---|
| Payment-gateway internals | The site does not process real payments; only the card-entry form is tested |
| Performance and load | Needs tooling and a controlled environment; a public shared site is not appropriate |
| Security testing | Penetration testing a public site without permission is not appropriate. Injection-style strings are used only as *input validation* checks on search and forms, observing whether input is handled safely in the UI |
| Third-party ads and embedded widgets | Not owned by the application |
| Public API (`/api/...`) | Covered separately by API automation, not by this manual suite |

## 4. Test Approach

- **Design techniques:** equivalence partitioning and boundary value analysis for form
  fields and quantities; state-based tests for the cart and login session; error guessing
  and short timeboxed exploratory sessions around checkout and search.
- **Prioritisation:** risk-based. Checkout, payment entry and order totals are High
  priority because a failure there costs money or orders. Details are in the
  [Test Strategy](test-strategy.md#2-risk-based-prioritisation).
- **Execution:** cases are run manually in a browser from [`test-cases.csv`](test-cases.csv),
  using DevTools to inspect network requests, console errors and form attributes where
  a result is unclear.
- **Test data:** fresh accounts are created per run using a unique email pattern
  (`qa.hadi+<yyyymmdd><nn>@example.com`) so cases do not depend on each other. Card
  details are dummy values; no real payment data is ever entered.
- **Defect logging:** every failed case gets a defect report in [`bugs/`](../bugs) using the
  template fields in the strategy. Screenshots go in [`evidence/`](../evidence).
- **Retest and regression:** fixed defects are retested with the original case, and the
  High-priority cases in the affected module are re-run.

## 5. Test Environment

| Item | Detail |
|---|---|
| Application URL | https://automationexercise.com |
| Primary browser | Google Chrome, latest stable, on Windows 11 (1920×1080) |
| Cross-browser | Mozilla Firefox (latest stable) and Microsoft Edge (latest stable) on Windows 11 |
| Mobile viewport | Chrome DevTools device toolbar, iPhone 12 Pro preset (390×844) |
| Tools | Browser DevTools (Elements, Console, Network), a text editor for the invoice file, Trello board for defect tracking |
| Network | Standard broadband; ad blocker disabled during execution so layout matches what users see |

The exact browser build numbers used for a run are recorded in the
[Test Summary Report](test-summary-report.md#test-environment-used).

## 6. Entry and Exit Criteria

### Entry criteria

- The site loads and the home page, product list and login page respond.
- Test cases are reviewed and the CSV is the agreed baseline for the cycle.
- Test email addresses and dummy card data are prepared.

### Exit criteria

- 100% of High-priority cases and at least 95% of all cases executed.
- No open Critical defects. Any open Major defect has an agreed workaround or is
  accepted by the product owner.
- All failed cases have a linked defect report.
- Test Summary Report completed with a release recommendation.

### Suspension and resumption

Testing is suspended if the site is down, or if a defect blocks the purchase flow so that
more than a third of the remaining cases cannot run. It resumes once the blocker is
resolved or a workaround is found, starting with the blocked cases.

## 7. Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| The site is a shared public demo and its data or behaviour can change between runs | Results may not reproduce later | Record date, browser build and test data with each run; capture screenshots for every failure |
| Ads and pop-ups overlap page elements | Clicks land on the wrong element; false failures | Close overlays before each step; note any overlay-caused issue separately from app defects |
| Accounts created by other testers may collide with test emails | Registration cases fail for the wrong reason | Use the unique email pattern in Section 4 |
| No access to developers or a requirements document | Expected results must be inferred | Base expected results on common e-commerce conventions and the site's own on-screen text; flag assumptions in the case or bug notes |
| Checkout defects block later cases | Orders and invoice cases cannot run | Run checkout cases early in the cycle so blockers surface first |

## 8. Deliverables

| Deliverable | Location |
|---|---|
| Test Plan (this document) | `docs/test-plan.md` |
| Test Strategy | [`docs/test-strategy.md`](test-strategy.md) |
| Test cases with execution results | [`docs/test-cases.csv`](test-cases.csv) |
| Defect reports | [`bugs/`](../bugs) |
| Requirements Traceability Matrix | [`docs/requirements-traceability-matrix.md`](requirements-traceability-matrix.md) |
| Test Summary Report | [`docs/test-summary-report.md`](test-summary-report.md) |
| Screenshots of failures | [`evidence/`](../evidence) |

## 9. Schedule (notional)

| Activity | Duration | Output |
|---|---|---|
| Explore the application and agree scope | 0.5 day | Scope section of this plan |
| Write test plan and strategy | 0.5 day | Plan and strategy documents |
| Design test cases | 1 day | `test-cases.csv` baseline |
| Build the traceability matrix | 0.5 day | RTM showing every requirement is covered |
| Execute Cycle 1 and log defects | 1.5 days | Updated CSV, defect reports, screenshots |
| Retest and write the summary report | 0.5 day | Test Summary Report with recommendation |

## 10. Roles

| Role | Person | Responsibility |
|---|---|---|
| QA Engineer | Abdul Hadi | Plan, design, execute, log defects, report |
| Product owner / developer | Not available (public demo site) | Defect triage is simulated: severity and priority are assigned by QA using the strategy definitions |
