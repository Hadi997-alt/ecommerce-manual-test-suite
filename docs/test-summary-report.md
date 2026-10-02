# Test Summary Report: Cycle 1

| Field | Value |
|---|---|
| Application | [Automation Exercise](https://automationexercise.com) |
| Cycle | Cycle 1: functional regression of the customer purchase journey |
| Period | October 2026 |
| Prepared by | Abdul Hadi |
| Related documents | [Test Plan](test-plan.md) · [Test Strategy](test-strategy.md) · [Test Cases](test-cases.csv) · [Traceability Matrix](requirements-traceability-matrix.md) |

## Recommendation

**No-Go** for release in the current state.

The purchase flow works end to end, but the invoice states the wrong amount for any order
with a quantity above 1 ([BUG-001](../bugs/BUG-001_checkout-total-mismatch.md), Critical).
The exit criteria in the test plan do not allow release with an open Critical defect.

Release becomes a **Go** once BUG-001 is fixed and TC-ORD-02 passes on retest, provided the
two Major defects (BUG-003, BUG-006) are either fixed or accepted by the product owner
with the workarounds described in their reports.

## Execution Summary

| Measure | Count |
|---|---|
| Test cases planned | 59 |
| Executed | 59 (100%) |
| Passed | 51 (86.4%) |
| Failed | 8 (13.6%) |
| Blocked / Not run | 0 |
| Defects logged | 6 |

High-priority cases: 26 executed, 22 passed, 4 failed (84.6% pass). All four High-priority
failures are in money-related areas: cart, payment entry and invoice.

### Results by module

| Module | Cases | Pass | Fail | Pass rate | Defects |
|---|---|---|---|---|---|
| Registration | 8 | 8 | 0 | 100% | – |
| Login | 7 | 6 | 1 | 86% | BUG-002 |
| Products & Search | 10 | 9 | 1 | 90% | BUG-004 |
| Cart | 8 | 7 | 1 | 88% | BUG-003 |
| Checkout | 10 | 8 | 2 | 80% | BUG-006 |
| Orders | 3 | 2 | 1 | 67% | BUG-001 |
| Account | 4 | 4 | 0 | 100% | – |
| Contact Form | 6 | 4 | 2 | 67% | BUG-005 |
| UI / Cross-browser | 3 | 3 | 0 | 100% | – |
| **Total** | **59** | **51** | **8** | **86.4%** | **6** |

## Defects

### By severity

| Severity | Count | Defects |
|---|---|---|
| Critical | 1 | BUG-001 |
| Major | 2 | BUG-003, BUG-006 |
| Minor | 3 | BUG-002, BUG-004, BUG-005 |
| Trivial | 0 | – |

### Defect list

| ID | Title | Severity | Priority | Status |
|---|---|---|---|---|
| [BUG-001](../bugs/BUG-001_checkout-total-mismatch.md) | Invoice amount ignores item quantity and does not match the checkout total | Critical | P1 | New |
| [BUG-002](../bugs/BUG-002_login-error-message.md) | Login fails with a generic error when a registered email is typed in a different letter case | Minor | P2 | New |
| [BUG-003](../bugs/BUG-003_cart-quantity-update.md) | Item quantity cannot be changed on the cart page | Major | P2 | New |
| [BUG-004](../bugs/BUG-004_search-no-results-handling.md) | Search with no matches shows an empty page with no message | Minor | P3 | New |
| [BUG-005](../bugs/BUG-005_contact-form-validation.md) | Contact form accepts a blank name and an empty message | Minor | P2 | New |
| [BUG-006](../bugs/BUG-006_payment-card-format-validation.md) | Payment form accepts a non-numeric card number and an expired date | Major | P2 | New |

## Highest-Risk Modules

1. **Orders / invoice.** One Critical defect. Totals are right on screen but wrong in the
   document the customer keeps, which is the kind of mismatch that turns into payment
   disputes.
2. **Checkout (payment entry).** Card number and expiry are not validated, so malformed
   or expired card data reaches order confirmation.
3. **Cart.** Quantities cannot be changed in the cart. Combined with BUG-001, customers who
   order several units of an item are the ones most affected.

Registration, account management and cross-browser behaviour were stable: every case passed.

## Quality Assessment

The core journey (register, log in, find a product, add to cart, check out, pay, get a
confirmation) works in Chrome, Firefox and Edge and on a mobile viewport. On-screen totals
in the cart and checkout are correct, input in search is handled safely, and required-field
validation works on the signup, login and payment forms.

The weaknesses are concentrated in two places: **calculations outside the main checkout
screen** (the invoice) and **validation beyond "field is not empty"** (card format, expiry,
whitespace-only names, optional message). Both point at missing server-side checks rather
than one-off UI mistakes, so the fixes should come with server-side validation and a
retest of every form, not only the failing fields.

## Observations Not Logged as Defects

- The duplicate-email error reads "Email Address already exist!" (grammar). Cosmetic; noted
  for the product owner rather than logged.
- No password length or complexity rule is shown on signup. There is no requirement to
  test against, so this is raised as a question, not a defect.

## Test Environment Used

| Item | Detail |
|---|---|
| OS | Windows 11 |
| Browsers | Chrome (primary), Firefox and Edge, latest stable releases at the time of execution |
| Mobile check | Chrome DevTools device toolbar, iPhone 12 Pro preset (390×844) |
| Test data | Fresh accounts per run (`qa.hadi+<date><nn>@example.com`); dummy card 4111 1111 1111 1111 |

## Exit Criteria Check

| Criterion (from the test plan) | Met? |
|---|---|
| 100% of High-priority cases executed | Yes (26 of 26) |
| At least 95% of all cases executed | Yes (100%) |
| No open Critical defects | **No**: BUG-001 open |
| Open Major defects have a workaround or are accepted | Partly: workarounds documented for BUG-003; BUG-006 needs a product-owner decision |
| Every failed case linked to a defect | Yes (8 of 8) |

## Next Steps

1. Fix BUG-001, then retest TC-ORD-02 and TC-ORD-03 plus a new case with two multi-quantity lines.
2. Product owner decides on BUG-003 and BUG-006 (fix now or accept with workaround).
3. Re-run all High-priority cases in Cart, Checkout and Orders as regression after the fixes.
4. Automate the regression-critical happy paths (TC-REG-01, TC-LOG-01, TC-CRT-01, TC-CHK-04,
   TC-CHK-06, TC-ORD-03) so future cycles do not depend on manual reruns.
