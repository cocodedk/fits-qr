"""The words of the privacy policy, in English and Danish.

Both languages carry the same nine sections in the same order, so the two pages stay one policy.
Every claim here is backed by the app's manifest, source or build files; if the app changes (a
permission, a network call, a library), change the text here and re-run `python3 scripts/build-site.py`.
"""
from __future__ import annotations

ISSUES = "https://github.com/cocodedk/fits-qr/issues"
DPA = "https://www.datatilsynet.dk/english"
MAIL = '<a href="mailto:bb@cocode.dk">bb@cocode.dk</a>'
PERMISSION = "<code>dk.fits.contact.DYNAMIC_RECEIVER_<wbr>NOT_EXPORTED_<wbr>PERMISSION</code>"

EN = {
    "lang": "en", "locale": "en_GB", "other": "da", "other_label": "Dansk",
    "title": "Privacy policy: FITS",
    "description": ("Privacy policy for the FITS Android app: it collects nothing, has no internet "
                    "permission and sends no data anywhere."),
    "effective": 'Effective <time datetime="2026-10-07">7 October 2026</time>. This policy covers the '
                 "Android app FITS (package <code>dk.fits.contact</code>, called FITS QR on this website).",
    "back": "Back to the front page", "about": "About FITS",
    "sections": [
        ("Summary", [
            "FITS collects nothing about you. The app shows three work contact cards, each with a QR "
            "code, and everything on them is built into the app. It has no permission to use the "
            "internet, so it cannot send anything anywhere. It has no account, no analytics and no ads.",
        ]),
        ("What is collected", [
            "Nothing. The app has no sign-up, no input fields and no settings, so it never receives "
            "anything from you. It asks for no access to your contacts, camera, location, microphone or files.",
            "The only personal details in the app are those of the three people on its cards: Bassil "
            "Salameh (CEO), Babak Bandpey (CTO) and Silas Stilling Jørgensen (Cybersecurity Developer). "
            "For each of them the app holds a work email address, a work phone number and the FITS office "
            "address in Roskilde. They are not collected from you. The app's publisher wrote them into "
            "the app, and each QR code carries them as a vCard together with fits.dk.",
            "Whoever scans a code gets that card on their own phone. What the scanning phone's camera app "
            "does with it is up to that app, not this one.",
        ]),
        ("Servers the app contacts", [
            "None. The app does not hold Android's internet permission (<code>INTERNET</code>), and "
            "without it Android does not let an app open a network connection. The code has no network "
            "calls and no web view, and it never opens a link. The address fits.dk appears only as text "
            "inside the vCard. The QR codes are drawn on the phone itself with the ZXing library.",
        ]),
        ("Permissions", [
            "The app asks for none, and Android shows no permission prompt for it. Its own manifest "
            "declares no permission.",
            f"The finished app lists one entry that is not ours, {PERMISSION}. An Android library adds "
            "it automatically. It is a private permission named after the app, of the kind only the app "
            "itself can use (protection level &quot;signature&quot;), and it gives no access to anything "
            "on your phone.",
        ]),
        ("What stays on the phone", [
            "The app saves nothing of its own: no settings, no history, no database and no files. The "
            "cards are part of the app. Which card is showing is remembered only while the app is open.",
            "Android's backup switch is left on in the manifest (<code>allowBackup</code>). Since the app "
            "saves no data of its own, a backup has none of the app's data to copy. Uninstalling the app "
            "removes the app and what Android keeps for it.",
        ]),
        ("Third parties", [
            "None receives anything from the app. The app has no analytics, advertising or "
            "crash-reporting library. It is built from AndroidX and Jetpack Compose (Google's libraries "
            "for Android apps) and ZXing, which draws the QR codes. With no internet permission, none of "
            "them can send anything out.",
            "Getting the app is outside the app. The APK is built and signed by GitHub Actions and "
            "published on GitHub Releases, and you download it from GitHub directly or through Obtainium. "
            "That download is between your phone and GitHub.",
            "This website is hosted on GitHub Pages. Its home page loads typefaces from Google Fonts, so "
            "Google can see that visit. This privacy page loads nothing from other sites, and none of the "
            "site's pages contain analytics code or code that sets cookies.",
        ]),
        ("Your rights", [
            "The app holds no data about you, so there is nothing for you to access, correct or delete. "
            "Under the General Data Protection Regulation (GDPR) you may still ask the publisher what it "
            f'holds about you, have it corrected or deleted, and complain to the Danish Data Protection '
            f'Agency, <a href="{DPA}">Datatilsynet</a>.',
            "If you are one of the three people on the cards and want your details changed or removed, "
            "write to the address under Contact. A change reaches a phone only when the app is updated on it.",
        ]),
        ("Contact", [
            f"FITS is published by Cocode (Babak Bandpey) for FITS (fits.dk). Write to {MAIL}, or open an "
            f'issue on <a href="{ISSUES}">GitHub</a>.',
        ]),
        ("Changes", [
            "If the policy changes, the date at the top changes and the change is described here. Older "
            "versions are in the project's history on GitHub.",
            "7 October 2026: first published.",
        ]),
    ],
}

DA = {
    "lang": "da", "locale": "da_DK", "other": "en", "other_label": "English",
    "title": "Privatlivspolitik: FITS",
    "description": ("Privatlivspolitik for Android-appen FITS: den indsamler ingenting, har ingen "
                    "internettilladelse og sender ingen data nogen steder hen."),
    "effective": 'Gælder fra <time datetime="2026-10-07">7. oktober 2026</time>. Politikken gælder '
                 "Android-appen FITS (pakkenavn <code>dk.fits.contact</code>, kaldet FITS QR på denne hjemmeside).",
    "back": "Tilbage til forsiden", "about": "Om FITS",
    "sections": [
        ("Resumé", [
            "FITS indsamler ingenting om dig. Appen viser tre kontaktkort med arbejdsoplysninger, hver "
            "med en QR-kode, og alt på dem er bygget ind i appen. Den har ikke tilladelse til at bruge "
            "internettet og kan derfor ikke sende noget nogen steder hen. Den har ingen konto, ingen "
            "statistik og ingen reklamer.",
        ]),
        ("Hvad der indsamles", [
            "Ingenting. Appen har ingen tilmelding, ingen indtastningsfelter og ingen indstillinger, så "
            "den modtager aldrig noget fra dig. Den beder ikke om adgang til dine kontakter, dit kamera, "
            "din placering, din mikrofon eller dine filer.",
            "De eneste personoplysninger i appen er dem om de tre personer på kortene: Bassil Salameh "
            "(CEO), Babak Bandpey (CTO) og Silas Stilling Jørgensen (Cybersecurity Developer). For hver "
            "af dem har appen en arbejdsmail, et arbejdstelefonnummer og FITS' adresse i Roskilde. "
            "Oplysningerne er ikke indsamlet fra dig. Appens udgiver har skrevet dem ind i appen, og "
            "hver QR-kode indeholder dem som et vCard sammen med fits.dk.",
            "Den, der scanner en kode, får kortet på sin egen telefon. Hvad scannerens kamera-app "
            "derefter gør med det, bestemmer den app, ikke denne.",
        ]),
        ("Servere appen kontakter", [
            "Ingen. Appen har ikke Androids internettilladelse (<code>INTERNET</code>), og uden den "
            "lader Android ikke en app åbne en netforbindelse. Koden indeholder ingen netværkskald og "
            "ingen webvisning, og den åbner aldrig et link. Adressen fits.dk står kun som tekst inde i "
            "vCardet. QR-koderne tegnes på selve telefonen med biblioteket ZXing.",
        ]),
        ("Tilladelser", [
            "Appen beder ikke om nogen, og Android viser ingen tilladelsesbesked for den. Appens egen "
            "manifestfil erklærer ingen tilladelser.",
            f"I den færdige app står der alligevel én post, som ikke er vores: {PERMISSION}. Den tilføjes "
            "automatisk af et Android-bibliotek. Det er en privat tilladelse opkaldt efter appen, af den "
            "slags kun appen selv kan bruge (beskyttelsesniveau &quot;signature&quot;), og den giver ikke "
            "adgang til noget på din telefon.",
        ]),
        ("Hvad der bliver på telefonen", [
            "Appen gemmer ikke noget selv: ingen indstillinger, ingen historik, ingen database og ingen "
            "filer. Kortene er en del af selve appen. Hvilket kort der vises, huskes kun så længe appen "
            "er åben.",
            "Androids sikkerhedskopiering er ikke slået fra i manifestfilen (<code>allowBackup</code>). "
            "Da appen ikke gemmer data selv, har en sikkerhedskopi ingen data fra appen at tage med. "
            "Afinstallerer du appen, forsvinder appen og det, Android har gemt til den.",
        ]),
        ("Tredjeparter", [
            "Ingen får noget fra appen. Appen har intet bibliotek til statistik, reklamer eller "
            "fejlrapportering. Den er bygget af AndroidX og Jetpack Compose (Googles biblioteker til "
            "Android-apps) og ZXing, som tegner QR-koderne. Uden internettilladelse kan ingen af dem "
            "sende noget ud.",
            "At hente appen sker uden for appen. APK-filen bygges og signeres af GitHub Actions og ligger "
            "på GitHub Releases, og du henter den direkte fra GitHub eller gennem Obtainium. Den "
            "overførsel foregår mellem din telefon og GitHub.",
            "Denne hjemmeside ligger på GitHub Pages. Forsiden henter skrifttyper fra Google Fonts, så "
            "Google kan se det besøg. Denne privatlivsside henter intet fra andre hjemmesider, og ingen af "
            "hjemmesidens sider indeholder statistikkode eller kode, der sætter cookies.",
        ]),
        ("Dine rettigheder", [
            "Appen har ingen oplysninger om dig, så der er intet at få indsigt i, rette eller slette. "
            "Efter databeskyttelsesforordningen (GDPR) kan du alligevel spørge udgiveren, hvad der er "
            f'gemt om dig, få det rettet eller slettet og klage til <a href="{DPA}">Datatilsynet</a>.',
            "Er du en af de tre personer på kortene og vil have dine oplysninger ændret eller fjernet, så "
            "skriv til adressen under Kontakt. En ændring når først en telefon, når appen opdateres dér.",
        ]),
        ("Kontakt", [
            f"FITS udgives af Cocode (Babak Bandpey) til FITS (fits.dk). Skriv til {MAIL}, eller opret "
            f'en sag på <a href="{ISSUES}">GitHub</a>.',
        ]),
        ("Ændringer", [
            "Ændres politikken, ændrer vi datoen øverst og beskriver ændringen her. Ældre versioner kan "
            "ses i projektets historik på GitHub.",
            "7. oktober 2026: første udgave af siden.",
        ]),
    ],
}

TEXT = {"en": EN, "da": DA}
