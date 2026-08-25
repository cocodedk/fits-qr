# Security Policy

## Reporting a Vulnerability

Do **not** open a public GitHub issue for security vulnerabilities.

To report a vulnerability:
- Use the **"Report a vulnerability"** button on the **Security** tab of this repository
  (GitHub private advisory), or
- Email **babak@cocode.dk**.

We will acknowledge within 5 business days and aim to release a fix within 30 days of
confirmation.

## Scope

The app requests no runtime permissions and makes no network calls — it is a static,
offline QR-code viewer. There is no server component, no stored credentials, and no data
leaves the device. The realistic attack surface is the on-device vCard/QR encoding path:
malformed input reaching `Contact.vCard` or the ZXing QR generation in
[`QrCode.kt`](app/src/main/java/dk/fits/contact/QrCode.kt) that could produce a
malformed or misleading vCard payload. Report issues there, or in the build/release
pipeline, the same way as any other vulnerability.

## Supported Versions

| Version | Supported |
|---------|-----------|
| latest  | ✅        |
| older   | ❌        |
