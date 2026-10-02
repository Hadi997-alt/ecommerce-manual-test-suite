# BUG-003: Item quantity cannot be changed on the cart page

| Field | Value |
|---|---|
| Bug ID | BUG-003 |
| Severity | Major |
| Priority | P2 – Medium |
| Status | New |
| Module | Cart |
| Environment | Chrome (latest stable) on Windows 11, 1920×1080; https://automationexercise.com |
| Related test case | TC-CRT-05 |
| Reported by | Abdul Hadi |

## Preconditions

- Cart contains Blue Top with quantity 1.

## Steps to Reproduce

1. Click **Cart** in the header.
2. In the Blue Top row, click the value in the **Quantity** column and try to type `3`.
3. Look for increment/decrement controls or an **Update cart** button.
4. Inspect the Quantity cell in DevTools.

## Expected Result

The quantity can be changed in the cart (editable field or +/- buttons), and the line
total and cart total recalculate, e.g. 3 × Rs. 500 = Rs. 1500.

## Actual Result

Quantity is rendered as a disabled button showing `1`. It cannot be focused or edited,
and there is no update control anywhere on the page.

## Notes

- Workaround: open the product detail page and add the product again with the extra
  quantity (TC-CRT-06 confirms this merges into one row), or remove the row with X and
  re-add with the correct quantity. Neither is discoverable from the cart page.
- Reducing a quantity has no workaround other than removing the item and adding it again.
- Changing quantity in the cart is standard behaviour on e-commerce sites; without it
  customers abandon or over-order.

## Attachments

- `evidence/BUG-003_cart-quantity.png`: cart row with DevTools showing the disabled quantity element
