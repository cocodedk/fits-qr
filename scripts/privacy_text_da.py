"""The Danish privacy text. Same nine sections, same facts and same order as the English in
privacy_text.py; change both together. Written to the humanizer-da rules (no dashes as pauses)."""
from __future__ import annotations

from privacy_common import DPA, ISSUES, MAIL, PERMISSION

DA = {
    "lang": "da", "locale": "da_DK", "other": "en", "other_label": "English",
    "title": "Privatlivspolitik: FITS",
    "description": ("Privatlivspolitik for Android-appen FITS: den indsamler ingenting, har ingen "
                    "internettilladelse og sender ingen data nogen steder hen."),
    "effective": 'Gælder fra <time datetime="2026-10-07">7. oktober 2026</time>. Politikken gælder '
                 "Android-appen FITS. Appens pakkenavn, dens unikke ID på Android, er "
                 "<code>dk.fits.contact</code>. På denne hjemmeside hedder appen FITS QR.",
    "back": "Tilbage til forsiden", "about": "Om FITS",
    "sections": [
        ("Resumé", [
            "FITS indsamler ikke noget om dig. Appen kan ikke sende noget over internettet, fordi den "
            "ikke har tilladelse til at bruge internettet. Siden &quot;Om FITS&quot; har knapper, der "
            "åbner websider, men kun når du trykker på en, og det er din telefons browser, ikke appen, "
            "der åbner siden. Appen viser kun tre kontaktkort med "
            "arbejdsoplysninger, hvert med en QR-kode (en firkantet stregkode, som et telefonkamera "
            "kan læse). Alt på kortene er bygget ind i appen. Appen har ingen konto, ingen "
            "analyseværktøjer (som måler, hvordan folk bruger en app) og ingen reklamer.",
        ]),
        ("Hvad der indsamles", [
            "Ingenting. Appen har ingen tilmelding, ingen indtastningsfelter og ingen indstillinger, "
            "så du giver den aldrig noget. Den beder ikke om adgang til dine kontakter, dit kamera, "
            "din placering, din mikrofon eller dine filer.",
            "Appen indeholder dog personoplysninger om tre personer: Bassil Salameh (CEO), Babak "
            "Bandpey (CTO) og Silas Stilling Jørgensen (Cybersecurity Developer). For hver af dem har "
            "appen en arbejdsmail, et arbejdstelefonnummer og FITS' adresse i Roskilde. Oplysningerne "
            "er ikke indsamlet fra dig. Appens udgiver har skrevet dem ind i appen.",
            "Hver QR-kode indeholder oplysningerne som et vCard (et standardformat til et kontaktkort) "
            "sammen med fits.dk. Den, der scanner en kode, får kortet på sin egen telefon. Hvad "
            "kamera-appen på den telefon gør med det, bestemmer den app, ikke denne.",
        ]),
        ("Servere appen kontakter", [
            "Ingen. Appen kontakter ingen servere. Det skyldes to ting. Appen har ikke Androids "
            "internettilladelse (<code>INTERNET</code>), og uden den lader Android ikke en app åbne en "
            "netforbindelse. Desuden indeholder appens kode ingen netværkskald og ingen webvisning (et "
            "indbygget browservindue).",
            "Siden &quot;Om FITS&quot; er det eneste sted, hvor en webside kan blive åbnet. Du kommer "
            "til den med den lille &quot;i&quot;-knap i hjørnet øverst på kontaktkortene (for "
            "skærmlæsere hedder knappen &quot;Om denne app&quot;). Siden har fem knapper, der åbner "
            "en webside: &quot;Se den nyeste version&quot;, &quot;Læs privatlivspolitikken&quot;, "
            "&quot;Åbn hjemmesiden&quot;, &quot;Se kildekoden på GitHub&quot; og &quot;Meld en fejl "
            "på GitHub&quot;. Appen åbner kun en side, når du trykker på en af dem, og den henter ikke "
            "siden selv. Den giver en fast webadresse videre til din telefon, og telefonens browser "
            "åbner den. Appen kan stadig ikke oprette forbindelse til noget. De fem adresser fører til "
            "projektets side med den nyeste udgave, denne privatlivspolitik, projektets hjemmeside, "
            "dets kildekode og dets liste over meldte fejl, alle på GitHub eller GitHub Pages. Appen "
            "tilføjer intet til dem: ingen kontaktoplysninger og intet om dig.",
            "Adressen fits.dk står kun som almindelig tekst, på kortene og inde i vCardet, aldrig som "
            "et link. QR-koderne tegnes på din telefon af "
            "ZXing, et bibliotek (færdig kode, som en app bygger på).",
        ]),
        ("Tilladelser", [
            "Appen beder ikke om nogen. En tilladelse er noget, Android spørger dig om, før en app må "
            "bruge for eksempel dit kamera eller din placering. FITS viser ingen tilladelsesbesked. "
            "Appens manifestfil, filen hvor en app skriver, hvad den beder om, erklærer ingen "
            "tilladelser.",
            f"Én post i den færdige app er ikke vores: {PERMISSION}. Et Android-bibliotek tilføjer den "
            "automatisk. Det er en privat tilladelse opkaldt efter appen. Android kalder dens "
            "beskyttelsesniveau &quot;signature&quot;: kun apps, der er signeret med det samme "
            "certifikat som FITS, kan få den. Den giver ikke adgang til noget på din telefon.",
        ]),
        ("Hvad der bliver på telefonen", [
            "Appen gemmer ikke noget selv: ingen indstillinger, ingen historik, ingen "
            "database og ingen filer. Kortene er en del af selve appen. Appen husker, hvilket kort "
            "der vises, om siden &quot;Om FITS&quot; er åben, og hvilken knap på den side der ikke kunne "
            "åbne en webside. Det overlader den til Androids funktion til at huske en apps tilstand, så "
            "du lander samme sted, når du vender telefonen eller skifter tilbage til appen. Android "
            "holder på det, så længe appen ligger blandt dine seneste apps, og appen skriver det ikke "
            "til nogen fil.",
            "Androids sikkerhedskopiering (som kopierer appdata, når du tager backup af telefonen) er "
            "ikke slået fra for appen i manifestfilen (<code>allowBackup</code>). Da appen ikke gemmer "
            "data selv, har en sikkerhedskopi ingen data fra appen at tage med. Afinstallerer du "
            "appen, forsvinder appen og det, Android har gemt til den.",
        ]),
        ("Tredjeparter", [
            "Ingen får noget fra appen. Appen har intet bibliotek til analyse, reklamer eller "
            "fejlrapportering (som sender fejlmeldinger til udvikleren). Den er bygget af AndroidX og "
            "Jetpack Compose (Googles biblioteker til Android-apps) og ZXing. Ingen af dem kan sende "
            "noget ud, fordi appen ikke har internettilladelse.",
            "At hente appen sker uden for appen. APK-filen (installationsfilen til en Android-app) "
            "bygges og signeres af GitHub Actions (GitHubs automatiske byggetjeneste) og ligger på "
            "GitHub Releases. Du henter den direkte fra GitHub eller gennem Obtainium, en app, der "
            "holder andre apps opdateret fra deres udgivelsessider. Den overførsel foregår mellem din "
            "telefon og GitHub.",
            "Når du trykker på en knap på siden &quot;Om FITS&quot;, er det din browser, ikke appen, "
            "der besøger GitHub eller GitHub Pages. GitHub kan se besøget, som en hjemmeside kan se "
            "alle sine besøgende. Appen sender intet til GitHub.",
            "Denne hjemmeside ligger på GitHub Pages, GitHubs hosting af hjemmesider. Forsiden henter "
            "skrifttyper fra Google Fonts, Googles skrifttjeneste, så Google kan se det besøg. Denne "
            "privatlivsside henter intet fra andre hjemmesider. Ingen af hjemmesidens sider indeholder "
            "analysekode eller kode, der sætter cookies (små filer, en hjemmeside kan lægge i din "
            "browser).",
        ]),
        ("Dine rettigheder", [
            "Appen har ingen oplysninger om dig, så der er intet at få indsigt i, rette eller slette. "
            "EU's databeskyttelsesforordning (GDPR) giver dig alligevel ret til at spørge udgiveren, "
            "hvad der er gemt om dig, få det rettet eller slettet og klage til "
            f'<a href="{DPA}">Datatilsynet</a>.',
            "Er du en af de tre personer på kortene og vil have dine oplysninger ændret eller fjernet, "
            "så skriv til adressen under Kontakt. En ændring når først en telefon, når appen er "
            "opdateret på den telefon.",
        ]),
        ("Kontakt", [
            f"Appen FITS udgives af Cocode (Babak Bandpey) til organisationen FITS (fits.dk). Skriv til {MAIL}, eller opret et "
            f'issue på <a href="{ISSUES}">GitHub</a> (en offentlig henvendelse på projektets side).',
        ]),
        ("Ændringer", [
            "Ændres politikken, ændrer vi datoen øverst og beskriver ændringen her. Ældre versioner "
            "kan ses i projektets historik på GitHub.",
            "7. oktober 2026: første udgave af siden.",
        ]),
    ],
}
