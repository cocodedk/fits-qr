<div align="center">

<img src="website/fits-logo-white.png" width="150" alt="FITS">

# FITS QR

**Three FITS contacts. One scan each.**

A single-screen Android app for [FITS](https://fits.dk). Swipe between three contact cards and
scan a QR code to save the contact. Offline, no permission prompts, no tracking. On your phone the
app is called FITS.

[![CI](https://github.com/cocodedk/fits-qr/actions/workflows/ci.yml/badge.svg)](https://github.com/cocodedk/fits-qr/actions/workflows/ci.yml)
[![Release APK](https://github.com/cocodedk/fits-qr/actions/workflows/release-apk.yml/badge.svg)](https://github.com/cocodedk/fits-qr/actions/workflows/release-apk.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-00B2B8)](LICENSE)

</div>

## Install

<!-- cocode-apps:install:start -->
- Coming to F-Droid
- [Download the Android installation file (APK) from GitHub](https://github.com/cocodedk/fits-qr/releases/latest/download/FITS-QR.apk)
- [Add the app to Obtainium, an app that keeps it up to date](https://apps.obtainium.imranr.dev/redirect?r=obtainium://add/https://github.com/cocodedk/fits-qr)
<!-- cocode-apps:install:end -->

Open the downloaded `FITS-QR.apk`. If Android asks, allow your browser or file manager to install
unknown apps, then confirm the installation. Requires Android 8.0 (API 26) or newer.

Every release APK is built and signed by GitHub Actions from this source, with
[build provenance](https://docs.github.com/en/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds)
attached to the workflow run.

## Website

- [English](https://cocodedk.github.io/fits-qr/) · [Dansk](https://cocodedk.github.io/fits-qr/da/)
- The app on its own page, filling the display:
  [English](https://cocodedk.github.io/fits-qr/app/) ·
  [Dansk](https://cocodedk.github.io/fits-qr/da/app/)

The site shows a preview of the app screen. You can swipe it, and you can scan its QR codes
straight off your monitor. They are prepared images that hold the same contact details as the
app's codes. The home page's **Fullscreen** button enlarges the phone to fill the browser. The
`/app/` page shows the contact cards without the surrounding website navigation, which suits a
laptop at a stand or a tablet on a desk.

The preview scales a fixed 390×844 layout. The Android app adjusts to the phone's available
screen space.

## Features

The FITS logo and tagline stay fixed at the top. Below them sit three cards on a circular
pager — swiping past the last one wraps back to the first:

| | Role | |
|---|---|---|
| Bassil Salameh | CEO | fits@l7consulting.dk |
| Babak Bandpey | CTO | bba@l7consulting.dk |
| Silas Stilling Jørgensen | Cybersecurity Developer | ssj@l7consulting.dk |

Each card shows a QR code that holds a **vCard 3.0** (a standard contact-card format): name,
role, organisation, work phone, work email, the Roskilde office address and `https://fits.dk`.
A compatible camera or QR scanner can read the code and offer to save the contact. The app
generates the codes on the device with ZXing, so it needs no network access and shows no
permission prompts.

## Privacy

The app shows no permission prompts and makes no network calls: the QR codes are generated on
the device, and the app sends nothing over the network. Scanning a code gives the scanning phone
that one contact card. There is no server component and there are no stored credentials. The only
personal details in the app are the three work contacts compiled into it.

The About screen has buttons that open web pages (the latest release, the privacy policy, the
website, the source code and the issue list) in your browser, only when you tap them. The app
itself has no internet permission.

## Build

Needs a JDK 17 and an Android SDK with platform 37.

```bash
./gradlew assembleDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk
```

`local.properties` is not committed — point it at your SDK:

```properties
sdk.dir=/path/to/your/android-sdk
```

## Changing the contacts

Everything a card shows lives in one list. Edit `contacts` in
[`app/src/main/java/dk/fits/contact/Fits.kt`](app/src/main/java/dk/fits/contact/Fits.kt). The app's
QR codes are generated from the same data, so the app needs nothing else changed. Company-level
facts (address, website) sit in the `Fits` object beside it; the tagline and every other line of
interface text live in [`strings.xml`](app/src/main/res/values/strings.xml).

The website keeps its own copy of the contacts and shows prepared QR images. After editing
`Fits.kt`, update the matching data in `scripts/build-site.py` and regenerate the affected QR
images in `website/` yourself (no script in this repository makes them). Then update the pages:

```bash
python3 scripts/build-site.py
```

## Verifying a QR

Looking at a QR code cannot tell you whether it encodes the right bytes, so decode it from a real
screenshot instead:

```bash
python -m venv .venv && .venv/bin/pip install zxing-cpp pillow
adb exec-out screencap -p > shot.png
.venv/bin/python -c "import zxingcpp; from PIL import Image; \
  print(zxingcpp.read_barcode(Image.open('shot.png').convert('L')).text)"
```

The decoded text must match `Contact.vCard` exactly, `ø` included — ZXing defaults to ISO-8859-1,
so [`QrCode.kt`](app/src/main/java/dk/fits/contact/QrCode.kt) sets `CHARACTER_SET` to UTF-8.

## Releases

Releases are cut by hand from the **Release APK** workflow (`workflow_dispatch`, with a
`patch`/`minor`/`major` bump). The newest `v*` Git tag is the only version source: the workflow
reads it, computes the next one, stamps it into `versionName`/`versionCode` at build time, and
creates the tag along with the GitHub Release.

Signing needs four repository secrets — `KEYSTORE_BASE64`, `KEYSTORE_PASSWORD`, `KEY_ALIAS`,
`KEY_PASSWORD`. Generate a keystore and upload them with:

```bash
bash scripts/generate-keystore.sh   # writes ~/.fits-release/, never committed
bash scripts/setup-signing.sh       # uploads the four secrets via gh
```

Keep `~/.fits-release/release.keystore` backed up somewhere durable. It is the only key that can
sign updates to an already-installed app.

## Repo layout

```
app/                 the Android app (Kotlin, Jetpack Compose)
website/             the GitHub Pages site (en + da), generated by scripts/build-site.py
design/             the design canvas artboards the screen was drawn from
scripts/             keystore, signing, hooks, site generation
.githooks/           pre-commit, commit-msg, owner-locked pre-push
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Install the git hooks first:

```bash
bash scripts/install-hooks.sh
```

Security issues: [SECURITY.md](SECURITY.md).

## License

[Apache-2.0](LICENSE) © 2026 [Cocode](https://cocode.dk) · created by
[Babak Bandpey](https://linkedin.com/in/babakbandpey)

The FITS name and logo belong to [FITS](https://fits.dk); the licence covers this app's source,
not the brand.
