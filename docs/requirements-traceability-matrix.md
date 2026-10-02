# Requirements Traceability Matrix

Maps each requirement to the test cases that cover it and to any defect those cases
found. Read it left to right to check coverage ("is every requirement tested?") and right
to left to check impact ("which requirement does this bug break?").

Automation Exercise has no published requirements document, so the requirements below
were written from the site's visible features and standard e-commerce expectations
during test planning. They are numbered so cases and bugs can refer to them.

| Req ID | Module | Requirement | Test cases | Defects | Coverage |
|---|---|---|---|---|---|
| REQ-01 | Registration | A new customer can create an account with valid details | TC-REG-01, TC-REG-05, TC-REG-06, TC-REG-07, TC-REG-08 | – | Covered – all passed |
| REQ-02 | Registration | Signup rejects duplicate, missing and malformed email/name | TC-REG-02, TC-REG-03, TC-REG-04 | – | Covered – all passed |
| REQ-03 | Login | A registered customer can log in and stay logged in across pages and tabs | TC-LOG-01, TC-LOG-06, TC-LOG-07 | [BUG-002](../bugs/BUG-002_login-error-message.md) | Covered – 1 of 3 failed |
| REQ-04 | Login | Invalid or missing credentials are rejected with a clear message | TC-LOG-02, TC-LOG-03, TC-LOG-04 | – | Covered – all passed |
| REQ-05 | Login | Logout ends the session | TC-LOG-05 | – | Covered – all passed |
| REQ-06 | Products & Search | Customers can browse the product list and view product details | TC-PRD-01, TC-PRD-02 | – | Covered – all passed |
| REQ-07 | Products & Search | Keyword search returns matching products and explains when nothing matches | TC-PRD-03, TC-PRD-04, TC-PRD-05 | [BUG-004](../bugs/BUG-004_search-no-results-handling.md) | Covered – 1 of 3 failed |
| REQ-08 | Products & Search | Search input is handled as plain text (no errors, no script execution) | TC-PRD-06, TC-PRD-07 | – | Covered – all passed |
| REQ-09 | Products & Search | Products can be filtered by category and brand | TC-PRD-09, TC-PRD-10 | – | Covered – all passed |
| REQ-10 | Cart | Products can be added to the cart in a valid quantity | TC-CRT-01, TC-CRT-03, TC-CRT-04, TC-CRT-06, TC-PRD-08 | – | Covered – all passed |
| REQ-11 | Cart | The cart shows correct line totals and lets the customer change or remove items | TC-CRT-02, TC-CRT-05, TC-CRT-07 | [BUG-003](../bugs/BUG-003_cart-quantity-update.md) | Covered – 1 of 3 failed |
| REQ-12 | Cart | Cart contents survive logging in | TC-CRT-08 | – | Covered – all passed |
| REQ-13 | Checkout | Checkout requires a logged-in account | TC-CHK-01 | – | Covered – all passed |
| REQ-14 | Checkout | Checkout shows the correct addresses, order lines and total | TC-CHK-02, TC-CHK-03, TC-CHK-04, TC-CHK-05 | – | Covered – all passed |
| REQ-15 | Checkout | The payment form validates card details before placing the order | TC-CHK-07, TC-CHK-08, TC-CHK-09 | [BUG-006](../bugs/BUG-006_payment-card-format-validation.md) | Covered – 2 of 3 failed |
| REQ-16 | Checkout | A valid payment places the order, confirms it and empties the cart | TC-CHK-06, TC-CHK-10 | – | Covered – all passed |
| REQ-17 | Orders | The invoice is downloadable and states the correct amount | TC-ORD-01, TC-ORD-02, TC-ORD-03 | [BUG-001](../bugs/BUG-001_checkout-total-mismatch.md) | Covered – 1 of 3 failed |
| REQ-18 | Account | Logged-in state is visible and the account can be deleted | TC-ACC-01, TC-ACC-02 | – | Covered – all passed |
| REQ-19 | Account | Customers can subscribe to the newsletter with a valid email | TC-ACC-03, TC-ACC-04 | – | Covered – all passed |
| REQ-20 | Contact Form | The contact form validates input and confirms submission | TC-CON-01, TC-CON-02, TC-CON-03, TC-CON-04, TC-CON-05, TC-CON-06 | [BUG-005](../bugs/BUG-005_contact-form-validation.md) | Covered – 2 of 6 failed |
| REQ-21 | UI / Cross-browser | The purchase path works in Chrome, Firefox, Edge and on a mobile viewport | TC-UI-01, TC-UI-02, TC-UI-03 | – | Covered – all passed |

## Coverage Summary

| Measure | Value |
|---|---|
| Requirements | 21 |
| Requirements with at least one test case | 21 (100%) |
| Test cases mapped to a requirement | 59 of 59 |
| Requirements with all cases passing | 15 |
| Requirements with one or more failed cases | 6 (REQ-03, REQ-07, REQ-11, REQ-15, REQ-17, REQ-20) |

## Defect to Requirement Lookup

| Defect | Severity | Requirement | Failed case(s) |
|---|---|---|---|
| [BUG-001](../bugs/BUG-001_checkout-total-mismatch.md) | Critical | REQ-17 Invoice states the correct amount | TC-ORD-02 |
| [BUG-002](../bugs/BUG-002_login-error-message.md) | Minor | REQ-03 Customer can log in | TC-LOG-06 |
| [BUG-003](../bugs/BUG-003_cart-quantity-update.md) | Major | REQ-11 Cart lets the customer change items | TC-CRT-05 |
| [BUG-004](../bugs/BUG-004_search-no-results-handling.md) | Minor | REQ-07 Search explains when nothing matches | TC-PRD-05 |
| [BUG-005](../bugs/BUG-005_contact-form-validation.md) | Minor | REQ-20 Contact form validates input | TC-CON-03, TC-CON-04 |
| [BUG-006](../bugs/BUG-006_payment-card-format-validation.md) | Major | REQ-15 Payment form validates card details | TC-CHK-08, TC-CHK-09 |
