# BUG-001: Invoice amount ignores item quantity and does not match the checkout total

| Field | Value |
|---|---|
| Bug ID | BUG-001 |
| Severity | Critical |
| Priority | P1 – High |
| Status | New |
| Module | Orders / Checkout |
| Environment | Chrome (latest stable) on Windows 11, 1920×1080; https://automationexercise.com |
| Related test case | TC-ORD-02 (fails); TC-ORD-03 (passes, single item) |
| Reported by | Abdul Hadi |

## Preconditions

- Logged in with a registered account that has a saved address.
- Cart is empty before step 1.

## Steps to Reproduce

1. Open https://automationexercise.com/product_details/1 (Blue Top, Rs. 500).
2. Set quantity to **3** and click **Add to cart**, then **Continue Shopping**.
3. Open https://automationexercise.com/product_details/2 (Men Tshirt, Rs. 400), leave quantity at **1**, click **Add to cart**.
4. Open **Cart** and click **Proceed To Checkout**.
5. In **Review Your Order**, note the **Total Amount**.
6. Click **Place Order**, enter dummy card data (Name: Hadi QA, Card: 4111 1111 1111 1111, CVC: 123, Expiry: 12 / 2030) and click **Pay and Confirm Order**.
7. On the **ORDER PLACED!** page click **Download Invoice** and open the file.
8. Compare the amount in the invoice with the Total Amount from step 5.

## Expected Result

The invoice states a purchase amount of **1900**, matching the checkout Total Amount
(3 × 500 + 1 × 400).

## Actual Result

- Checkout **Total Amount**: Rs. 1900 (correct).
- Invoice: "Your total purchase amount is **900**". This equals 500 + 400, i.e. the unit
  prices summed with quantity ignored.

## Notes

- With a single item at quantity 1 (TC-ORD-03) the invoice matches, which points at the
  invoice calculation using unit price instead of line total.
- The invoice is the customer's financial record of the order. A customer who compares it
  to their card statement will see a Rs. 1000 difference, which leads to disputes and
  refund requests, hence Critical.
- Suggested check for the fix: rerun TC-ORD-02 and TC-ORD-03, and add a case with two
  multi-quantity lines.

## Attachments

- `evidence/BUG-001_checkout-total.png`: Review Your Order section showing Rs. 1900
- `evidence/BUG-001_invoice.png`: opened invoice file showing 900
