# BUG-006: Payment form accepts a non-numeric card number and an expired date

| Field | Value |
|---|---|
| Bug ID | BUG-006 |
| Severity | Major |
| Priority | P2 – Medium |
| Status | New |
| Module | Checkout (payment entry) |
| Environment | Chrome (latest stable) on Windows 11, 1920×1080; https://automationexercise.com |
| Related test cases | TC-CHK-08, TC-CHK-09 |
| Reported by | Abdul Hadi |

## Preconditions

- Logged in, Blue Top in the cart, user has clicked **Place Order** and is on the **Payment** page.

## Steps to Reproduce

**Case A: letters in card number (TC-CHK-08)**

1. Enter Name on Card `Hadi QA`, Card Number `abcd efgh ijkl mnop`, CVC `123`, Expiration `12` / `2030`.
2. Click **Pay and Confirm Order**.

**Case B: expired date (TC-CHK-09)**

1. Add Blue Top to the cart again and go to the **Payment** page.
2. Enter Name on Card `Hadi QA`, Card Number `4111 1111 1111 1111`, CVC `123`, Expiration `01` / `2020`.
3. Click **Pay and Confirm Order**.

## Expected Result

The order is not placed. The card number field rejects non-digits (and ideally fails a
Luhn check), and the expiry fields reject a date in the past, each with a message next to
the field.

## Actual Result

Both orders are placed and the **ORDER PLACED!** confirmation is shown.

## Notes

- Payment-gateway behaviour is out of scope, but field-format validation on the payment
  page is in scope: it is the first line of defence and the only feedback the user sees
  before submitting.
- On a real store this would either send bad data to the gateway (failed charges after
  the customer thinks the order succeeded) or confirm unpaid orders. Rated Major rather
  than Critical because this demo site does not take real payments.
- Also worth checking: CVC with letters, month `13`, and a two-digit year.

## Attachments

- `evidence/BUG-006_letters-card-number.png`: payment form with the letters entered
- `evidence/BUG-006_order-placed.png`: confirmation page after Case A
