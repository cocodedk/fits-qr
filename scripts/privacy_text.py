"""The words of the privacy policy, in English (here) and Danish (privacy_text_da.py).

Both languages carry the same nine sections in the same order, so the two pages stay one policy.
Every claim is backed by the app's manifest, source or build files; if the app changes (a
permission, a network call, a library), change the text here and re-run `python3 scripts/build-site.py`.
The wording is for a reader who is new to the app: what they need first, short sentences, each
technical term explained where it first appears.
"""
from __future__ import annotations

from privacy_common import DPA, ISSUES, MAIL, PERMISSION

EN = {
    "lang": "en", "locale": "en_GB", "other": "da", "other_label": "Dansk",
    "title": "Privacy policy: FITS",
    "description": ("Privacy policy for the FITS Android app: it collects nothing, has no internet "
                    "permission and sends no data anywhere."),
    "effective": 'Effective <time datetime="2026-10-07">7 October 2026</time>. This policy covers the '
                 "Android app FITS. The app's package name, its unique ID on Android, is "
                 "<code>dk.fits.contact</code>. This website calls the app FITS QR.",
    "back": "Back to the front page", "about": "About FITS",
    "sections": [
        ("Summary", [
            "FITS does not collect anything about you. It cannot send anything over the internet, "
            "because it does not have permission to use the internet. The About screen has buttons "
            "that open web pages, but only when you tap one, and then your phone's browser opens "
            "the page, not the app. The app only shows three work "
            "contact cards, each with a QR code (a square barcode that a phone camera reads). "
            "Everything on the cards is built into the app. The app has no account, no analytics "
            "(tools that measure how people use an app) and no ads.",
        ]),
        ("What is collected", [
            "Nothing. The app has no sign-up, no input fields and no settings, so you never give it "
            "anything. It does not ask for access to your contacts, camera, location, microphone or files.",
            "The app does contain personal details of three people: Bassil Salameh (CEO), Babak "
            "Bandpey (CTO) and Silas Stilling Jørgensen (Cybersecurity Developer). For each of them it "
            "holds a work email address, a work phone number and the FITS office address in Roskilde. "
            "These details are not collected from you. The app's publisher wrote them into the app.",
            "Each QR code contains these details as a vCard (a standard format for a contact card), "
            "together with fits.dk. Whoever scans a code gets that card on their own phone. What the "
            "camera app on that phone does with it is up to that app, not this one.",
        ]),
        ("Servers the app contacts", [
            "None. The app does not contact any server. Two things make this so. The app does not have "
            "Android's internet permission (<code>INTERNET</code>), and without it Android does not let "
            "an app open a network connection. And the app's code has no network calls and no web view "
            "(a built-in browser window).",
            "The About screen is the one place where a web page can open. You reach it with the small "
            "&quot;i&quot; button in the top corner of the contact cards (screen readers call it "
            "&quot;About this app&quot;). The screen is titled &quot;About FITS&quot; and has five "
            "buttons that open a page: &quot;See the latest version&quot;, &quot;Read the privacy "
            "policy&quot;, &quot;Open the website&quot;, &quot;See the source code on GitHub&quot; and "
            "&quot;Report a problem on GitHub&quot;. The app opens a page only when you tap one of "
            "them, and it does not load the page itself. It hands a fixed web address to your phone, "
            "and your phone's browser opens it. The app itself still cannot connect to anything. The "
            "five addresses lead to this project's page for its latest release, this privacy policy, "
            "the project's website, its source code and its list of reported problems, all on GitHub "
            "or GitHub Pages. The app adds nothing to them: no contact details and nothing about you.",
            "The address fits.dk appears only as plain text, on the cards and inside the vCard, "
            "never as a link. The QR codes are drawn on your "
            "phone by ZXing, a library (ready-made code that an app builds on).",
        ]),
        ("Permissions", [
            "The app asks for none. A permission is something Android asks you to allow before an app "
            "may use, for example, your camera or location. FITS shows no permission prompt. Its "
            "manifest, the file where an app lists what it asks for, declares no permission.",
            f"One entry in the finished app is not ours: {PERMISSION}. An Android library adds it "
            "automatically. It is a private permission named after the app. Android calls its protection "
            "level &quot;signature&quot;: only apps signed with the same certificate as FITS can get it. "
            "It gives no access to anything on your phone.",
        ]),
        ("What stays on the phone", [
            "The app saves nothing of its own: no settings, no history, no database and no files. The "
            "cards are part of the app. The app remembers which card is showing, whether the About page is "
            "open and which About button could not open a page. It leaves that to Android's feature for "
            "remembering an app's state, so you land in the same place when you turn the phone or switch "
            "back to the app. Android holds it for the app only while the app is among your recent apps, "
            "and the app writes it to no file.",
            "Android's backup feature (it copies app data when you back up your phone) is left on for "
            "this app in the manifest (<code>allowBackup</code>). Because the app saves no data of its "
            "own, a backup has none of the app's data to copy. If you uninstall the app, the app and "
            "what Android keeps for it are removed.",
        ]),
        ("Third parties", [
            "None receives anything from the app. The app has no analytics, advertising or "
            "crash-reporting library (crash reporting sends error reports to the developer). It is "
            "built from AndroidX and Jetpack Compose (Google's libraries for Android apps) and ZXing. "
            "None of them can send anything out, because the app has no internet permission.",
            "Getting the app happens outside the app. The APK (the installation file for an Android "
            "app) is built and signed by GitHub Actions (GitHub's automated build service) and "
            "published on GitHub Releases. You download it from GitHub directly or through Obtainium, "
            "an app that keeps other apps up to date from their release pages. That download is "
            "between your phone and GitHub.",
            "When you tap a button on the About screen, your browser, not the app, visits GitHub or "
            "GitHub Pages. GitHub can see that visit, as any website sees its visitors. The app "
            "sends it nothing.",
            "This website is hosted on GitHub Pages, GitHub's website hosting. The home page loads "
            "typefaces from Google Fonts, Google's font service, so Google can see that visit. This "
            "privacy page loads nothing from other sites. None of the site's pages contain analytics "
            "code or code that sets cookies (small files a website can leave in your browser).",
        ]),
        ("Your rights", [
            "The app holds no data about you, so there is nothing for you to look at, correct or "
            "delete. The EU's General Data Protection Regulation (GDPR) still lets you ask the "
            "publisher what it holds about you, have it corrected or deleted, and complain to the "
            f'Danish Data Protection Agency, <a href="{DPA}">Datatilsynet</a>.',
            "If you are one of the three people on the cards and want your details changed or removed, "
            "write to the address under Contact. A change reaches a phone only when the app is updated "
            "on that phone.",
        ]),
        ("Contact", [
            "The app FITS is published by Cocode (Babak Bandpey) for the organisation FITS (fits.dk). "
            f"Write to {MAIL}, or open an "
            f'issue on <a href="{ISSUES}">GitHub</a> (a public message on the project\'s page).',
        ]),
        ("Changes", [
            "If the policy changes, we change the date at the top and describe the change here. Older "
            "versions are in the project's history on GitHub.",
            "7 October 2026: first published.",
        ]),
    ],
}

TEXT = {"en": EN}
try:  # the Danish text is a separate file; the site builds the Danish page when it exists
    from privacy_text_da import DA
except ModuleNotFoundError as exc:  # only "the file is not there yet"; a broken Danish text must fail the build
    if exc.name != "privacy_text_da":
        raise
else:
    TEXT["da"] = DA
