# Contributing to FITS Contact App

A single-screen Android app for [fits.dk](https://fits.dk) — Kotlin + Jetpack Compose,
built and run entirely from the CLI.

## Local Setup

1. Install a JDK 17 and the Android SDK command-line tools — no Android Studio required.
2. Point `local.properties` (ignored by git) at your Android SDK, and export `JAVA_HOME`
   at a JDK 17 install.
3. The Gradle wrapper is committed — `./gradlew` bootstraps everything else.

## Install Git Hooks

Run once after cloning so the local gates are active:

```
bash scripts/install-hooks.sh
```

## Build and Install

```bash
export JAVA_HOME=<path to a JDK 17>
./gradlew assembleDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk
```

There is no automated test suite yet — verification today is a manual install and a visual
check of the three contact cards and their QR codes. Contributions that add tests (unit tests
for the vCard formatting, Compose UI tests for the pager) are welcome; there is no coverage
gate to satisfy, just tests that actually exercise the change.

## Coding Style

- Keep files small and focused; contact and company data lives in
  [`Fits.kt`](app/src/main/java/dk/fits/contact/Fits.kt), QR generation in
  [`QrCode.kt`](app/src/main/java/dk/fits/contact/QrCode.kt).
- Models are immutable (`data class`).
- No hardcoded user-facing strings where a resource or constant fits.

## Local Git Setup

Run once after cloning:

```bash
git config pull.rebase true          # rebase on pull instead of a merge commit
git config core.autocrlf input       # normalize CRLF -> LF on commit (macOS/Linux)
git config push.autoSetupRemote true # push without -u the first time
```

Windows contributors: use `core.autocrlf true`.

## Branch Naming

Kebab-case; the prefix matches the Conventional Commit type used in the PR:

| Prefix | Commit type | Example |
|---|---|---|
| `feature/` | `feat:` | `feature/add-fourth-contact` |
| `fix/` | `fix:` | `fix/qr-charset-encoding` |
| `chore/` | `chore:` | `chore/bump-dependencies` |
| `docs/` | `docs:` | `docs/clarify-setup` |
| `refactor/` | `refactor:` | `refactor/extract-qr-generation` |
| `ci/` | `ci:` | `ci/add-dependabot` |

Never commit directly to `main` — always open a PR.

## PR Checklist

- [ ] `./gradlew assembleDebug` succeeds.
- [ ] Manually verified on a device/emulator: cards swipe, QR codes scan into a real
      contact with the correct name, role, phone, email and address.
- [ ] Docs updated if behaviour changed.
- [ ] Commit messages follow Conventional Commits.
