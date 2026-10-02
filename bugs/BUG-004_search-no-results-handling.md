# BUG-004: Search with no matches shows an empty page with no message

| Field | Value |
|---|---|
| Bug ID | BUG-004 |
| Severity | Minor |
| Priority | P3 – Low |
| Status | New |
| Module | Products & Search |
| Environment | Chrome (latest stable) on Windows 11, 1920×1080; https://automationexercise.com |
| Related test case | TC-PRD-05 |
| Reported by | Abdul Hadi |

## Preconditions

- None (logged in or out).

## Steps to Reproduce

1. Click **Products** in the header.
2. In **Search Product** type `xyzqw123`.
3. Click the search button.

## Expected Result

The results area shows a clear message, for example
`No products found for "xyzqw123"`, with a suggestion to check spelling or a link back to
all products.

## Actual Result

The heading **SEARCHED PRODUCTS** is displayed above a blank area with no message.
It looks as if the page failed to load rather than that nothing matched.

## Notes

- Impact is on usability, not on data or money, hence Minor. Priority is Low because
  other search cases (TC-PRD-03, TC-PRD-04, TC-PRD-06, TC-PRD-07) pass.

## Attachments

- `evidence/BUG-004_empty-search.png`: results page after searching for xyzqw123
