# BUG-002: Login fails with a generic error when a registered email is typed in a different letter case

| Field | Value |
|---|---|
| Bug ID | BUG-002 |
| Severity | Minor |
| Priority | P2 – Medium |
| Status | New |
| Module | Login |
| Environment | Chrome (latest stable) on Windows 11, 1920×1080; https://automationexercise.com |
| Related test case | TC-LOG-06 |
| Reported by | Abdul Hadi |

## Preconditions

- An account exists with email `qa.hadi+<date>01@example.com` and password `Test@1234`.
- User is logged out.

## Steps to Reproduce

1. Click **Signup / Login**.
2. Under **Login to your account** enter `QA.HADI+<date>01@EXAMPLE.COM` (same address, upper case).
3. Enter the correct password `Test@1234`.
4. Click **Login**.

## Expected Result

The user is logged in. Email addresses are treated as case-insensitive by almost every
service, and users often type them with a capital letter on mobile keyboards that
auto-capitalise.

## Actual Result

Login is rejected with "Your email or password is incorrect!". The same credentials typed
in lower case log in successfully.

## Notes

- The message correctly does not reveal which field is wrong (good for account privacy),
  but because the password *is* correct, the user has no way to work out what to change.
  There is also no "Forgot password" link on the page, so a user who hits this is stuck.
- Suggested fix: normalise email to lower case on both signup and login. If that is not
  possible, add "Email addresses are case-sensitive" help text under the field.
- Check whether signup has the same problem: can `QA.HADI+<date>01@EXAMPLE.COM` register as
  a second account? If so, that is a separate, more serious defect.

## Attachments

- `evidence/BUG-002_login-uppercase-email.png`: login form with the error message
