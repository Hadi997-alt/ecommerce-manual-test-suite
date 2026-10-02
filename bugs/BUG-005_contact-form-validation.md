# BUG-005: Contact form accepts a blank name and an empty message

| Field | Value |
|---|---|
| Bug ID | BUG-005 |
| Severity | Minor |
| Priority | P2 – Medium |
| Status | New |
| Module | Contact Form |
| Environment | Chrome (latest stable) on Windows 11, 1920×1080; https://automationexercise.com |
| Related test cases | TC-CON-03, TC-CON-04 |
| Reported by | Abdul Hadi |

## Preconditions

- User is on https://automationexercise.com/contact_us.

## Steps to Reproduce

**Case A: name made of spaces (TC-CON-03)**

1. In **Name** type three spaces.
2. Fill **Email** `qa.hadi@example.com`, **Subject** `Order query`, **Your Message Here** `Where is my order?`.
3. Click **Submit** and click **OK** in the confirmation dialog.

**Case B: empty message (TC-CON-04)**

1. Reload the page.
2. Fill **Name** `Hadi QA`, **Email** `qa.hadi@example.com`, **Subject** `Order query`; leave the message box empty.
3. Click **Submit** and click **OK** in the confirmation dialog.

## Expected Result

In both cases the form is not submitted and the user is told which field needs a value.
A contact request without a name or a message cannot be acted on by support.

## Actual Result

Both submissions succeed and show "Success! Your details have been submitted
successfully."

## Notes

- Email field validation works (TC-CON-02, TC-CON-05), so the gap is limited to Name
  (whitespace not trimmed) and Message (not marked required).
- Fix should be on the server as well as in the browser, since client-side `required`
  alone can be bypassed.
- Empty submissions create noise for the support team and make spam easier.

## Attachments

- `evidence/BUG-005_blank-name-success.png`: success message after Case A
- `evidence/BUG-005_empty-message-success.png`: success message after Case B
