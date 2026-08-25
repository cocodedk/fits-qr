#!/usr/bin/env python3
"""Render website/index.html and website/da/index.html from one template.

The phone block is a one-to-one replica of the app screen, so the card markup and the
contact data live here once and both languages are generated from them. Run after any
change to the app screen or the contacts:

    python3 scripts/build-site.py
"""
from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "website"
OWNER = "cocodedk"
REPO = "fits-qr"
BASE = f"https://{OWNER}.github.io/{REPO}"
RELEASES = f"https://github.com/{OWNER}/{REPO}/releases/latest"
REPO_URL = f"https://github.com/{OWNER}/{REPO}"
APK = "FITS-QR.apk"

ORG = "FITS - Framework for IT Security"
STREET, CITY, POSTAL, COUNTRY = "Københavnsvej 19B", "Roskilde", "4000", "Denmark"
ADDRESS = f"{STREET}, {POSTAL} {CITY}"
WEBSITE = "https://fits.dk"

PEOPLE = [
    {
        "first": "Bassil", "last": "Salameh", "role": "CEO",
        "email": "fits@l7consulting.dk", "phone": "+45 22 547 547", "qr": "qr-bassil.png",
    },
    {
        "first": "Babak", "last": "Bandpey", "role": "CTO",
        "email": "bba@l7consulting.dk", "phone": "+45 27 82 30 77", "qr": "qr-babak.png",
    },
    {
        "first": "Silas Stilling", "last": "Jørgensen", "role": "Cybersecurity Developer",
        "email": "ssj@l7consulting.dk", "phone": "+45 61 26 89 99", "qr": "qr-silas.png",
    },
]


def vcard(p: dict) -> str:
    """Byte-for-byte the string Contact.vCard builds in app/.../Fits.kt."""
    return "\r\n".join([
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"N:{p['last']};{p['first']};;;",
        f"FN:{p['first']} {p['last']}",
        f"ORG:{ORG}",
        f"TITLE:{p['role']}",
        f"TEL;TYPE=WORK,VOICE:{p['phone']}",
        f"EMAIL;TYPE=WORK,INTERNET:{p['email']}",
        f"ADR;TYPE=WORK:;;{STREET};{CITY};;{POSTAL};{COUNTRY}",
        f"URL:{WEBSITE}",
        "END:VCARD",
    ]) + "\r\n"


ICON_SCAN = (
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<rect x="3.5" y="5" width="17" height="14" stroke="#7FEAEF" stroke-width="1.5"/>'
    '<path d="M7 9.5V7.5h2M17 9.5V7.5h-2M7 14.5v2h2M17 14.5v2h-2" stroke="#7FEAEF" '
    'stroke-width="1.5" stroke-linecap="round"/></svg>'
)
ICON_PERSON = (
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<circle cx="12" cy="8" r="3.6" stroke="#00B2B8" stroke-width="1.6"/>'
    '<path d="M4.8 20c0-3.6 3.2-5.6 7.2-5.6s7.2 2 7.2 5.6" stroke="#00B2B8" '
    'stroke-width="1.6" stroke-linecap="round"/></svg>'
)
ICON_MAIL = (
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<rect x="2.5" y="5" width="19" height="14" rx="2.5" stroke="#00B2B8" stroke-width="1.6"/>'
    '<path d="M3.5 7l8.5 6 8.5-6" stroke="#00B2B8" stroke-width="1.6" stroke-linecap="round" '
    'stroke-linejoin="round"/></svg>'
)
ICON_PHONE = (
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<path d="M6.2 3.5h3l1.6 4-2 1.4a11.4 11.4 0 0 0 5.3 5.3l1.4-2 4 1.6v3a2 2 0 0 1-2.2 2'
    'A16.5 16.5 0 0 1 4.2 5.7a2 2 0 0 1 2-2.2Z" stroke="#00B2B8" stroke-width="1.6" '
    'stroke-linejoin="round"/></svg>'
)
ICON_PIN = (
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<path d="M12 21c4-4.2 6-7.3 6-10a6 6 0 1 0-12 0c0 2.7 2 5.8 6 10Z" stroke="#00B2B8" '
    'stroke-width="1.6" stroke-linejoin="round"/>'
    '<circle cx="12" cy="10.6" r="2.2" stroke="#00B2B8" stroke-width="1.6"/></svg>'
)
ICON_DOWNLOAD = (
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<path d="M12 3.5v11m0 0 4-4m-4 4-4-4M4.5 18.5h15" stroke="currentColor" '
    'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
)
ICON_CODE = (
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<path d="M9 6.5 3.5 12 9 17.5M15 6.5 20.5 12 15 17.5" stroke="currentColor" '
    'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
)
ICON_OFFLINE = (
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<path d="M12 3.5 20 7v6.2c0 4.6-3.3 8.1-8 9.3-4.7-1.2-8-4.7-8-9.3V7l8-3.5Z" '
    'stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>'
    '<path d="M8.6 12.4l2.4 2.4 4.4-4.7" stroke="currentColor" stroke-width="1.8" '
    'stroke-linecap="round" stroke-linejoin="round"/></svg>'
)
ICON_QR = (
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<rect x="3.5" y="3.5" width="7" height="7" stroke="currentColor" stroke-width="1.6"/>'
    '<rect x="13.5" y="3.5" width="7" height="7" stroke="currentColor" stroke-width="1.6"/>'
    '<rect x="3.5" y="13.5" width="7" height="7" stroke="currentColor" stroke-width="1.6"/>'
    '<path d="M13.5 13.5h3v3h-3zM18 18h2.5v2.5H18z" stroke="currentColor" stroke-width="1.6"/>'
    '</svg>'
)
ICON_OSS = (
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.6"/>'
    '<path d="M12 7.5v5.2l3.4 2" stroke="currentColor" stroke-width="1.7" '
    'stroke-linecap="round" stroke-linejoin="round"/></svg>'
)

STRINGS = {
    "en": {
        "lang": "en",
        "dir": "ltr",
        "prefix": "",
        "other_href": "da/",
        "other_label": "Dansk",
        "title": "FITS QR — three FITS contacts, one scan",
        "description": (
            "An open-source Android app for FITS. Swipe between three FITS contact cards and "
            "scan the QR code to save the contact — offline, no permissions, no tracking."
        ),
        "eyebrow": "Open source · Android",
        "h1_a": "Three FITS contacts.",
        "h1_b": "One scan each.",
        "lede": (
            "A single screen, three swipeable cards. Each card's QR code carries a full vCard, "
            "so any phone camera saves the contact in one tap. The codes below are live — point "
            "your phone at your screen right now."
        ),
        "cta_apk": "Download the APK",
        "cta_src": "Read the source",
        "cta_note": (
            "Android 8.0 and up · ~6.8 MB · Apache-2.0 · built and signed by GitHub Actions"
        ),
        "scan": "Scan to save the contact",
        "foot_note": "Danish product · European hosting",
        "dots_label": "Choose a contact card",
        "phone_label": "The FITS QR app screen — swipe or use the arrow keys",
        "payload_h2": "What the QR actually contains",
        "payload_p": (
            "No shortlink, no redirect, no server in the middle. The code encodes a vCard 3.0 "
            "in plain UTF-8, generated on your device. This is the exact text the card on the "
            "left is showing right now."
        ),
        "facts": [
            (ICON_OFFLINE, "No permissions, no network",
             "The app asks for nothing and talks to nobody. QR codes are generated on-device "
             "with ZXing, so it works in airplane mode."),
            (ICON_QR, "A real vCard, not a link",
             "Name, role, organisation, work phone, work email, the Roskilde office address and "
             "fits.dk — all inside the code itself."),
            (ICON_OSS, "Yours to read and rebuild",
             "Apache-2.0, Kotlin and Jetpack Compose. Change a contact in one file and the QR "
             "regenerates from it."),
        ],
        "install_h2": "Install it",
        "install_p": (
            "The APK is built and signed by GitHub Actions on every release, so what you "
            "download is what the workflow produced from this source."
        ),
        "steps": [
            ("Download the APK",
             f"Grab <code>{APK}</code> from the latest release on GitHub."),
            ("Allow the install",
             "Android will ask once whether to trust an app from outside the Play Store. This "
             "is the normal prompt for a sideloaded APK."),
            ("Open and swipe",
             "Swipe left or right between the three cards. Hand your phone over, or let "
             "someone scan straight off your screen."),
        ],
        "footer_by": "Created by",
        "footer_about": "About FITS",
        "footer_src": "Source",
        "footer_license": "Apache-2.0",
        "fullscreen": "Fullscreen",
        "exit_fullscreen": "Leave fullscreen",
        "kiosk_link": "Open the app on its own page",
        "kiosk_title": "FITS QR — the app, fullscreen",
        "kiosk_desc": (
            "The FITS QR app screen on its own, filling the display. Swipe between the three "
            "contacts and scan a code to save it."
        ),
        "back_label": "Back to the site",
    },
    "da": {
        "lang": "da",
        "dir": "ltr",
        "prefix": "../",
        "other_href": "../",
        "other_label": "English",
        "title": "FITS QR — tre FITS-kontakter, ét scan",
        "description": (
            "En open source Android-app til FITS. Skift mellem tre FITS-kontaktkort og scan "
            "QR-koden for at gemme kontakten — offline, uden tilladelser, uden sporing."
        ),
        "eyebrow": "Open source · Android",
        "h1_a": "Tre FITS-kontakter.",
        "h1_b": "Ét scan hver.",
        "lede": (
            "Én skærm, tre kort du skifter mellem. Hvert korts QR-kode indeholder et helt "
            "visitkort, så et hvilket som helst telefonkamera gemmer kontakten med ét tryk. "
            "Koderne herunder er ægte — hold telefonen op foran skærmen nu."
        ),
        "cta_apk": "Hent APK-filen",
        "cta_src": "Læs kildekoden",
        "cta_note": (
            "Android 8.0 og nyere · ~6.8 MB · Apache-2.0 · bygget og signeret af GitHub Actions"
        ),
        "scan": "Scan for at gemme kontakten",
        "foot_note": "Dansk produkt · Europæisk hosting",
        "dots_label": "Vælg et kontaktkort",
        "phone_label": "FITS QR-appens skærm — skift med swipe eller piletasterne",
        "payload_h2": "Hvad QR-koden faktisk indeholder",
        "payload_p": (
            "Ingen kort link, ingen omdirigering, ingen server undervejs. Koden indeholder et "
            "vCard 3.0 i almindelig UTF-8, genereret på din egen telefon. Det er præcis den "
            "tekst, kortet til venstre viser lige nu."
        ),
        "facts": [
            (ICON_OFFLINE, "Ingen tilladelser, intet netværk",
             "Appen beder ikke om noget og kontakter ingen. QR-koderne genereres på telefonen "
             "med ZXing, så den virker i flytilstand."),
            (ICON_QR, "Et rigtigt vCard, ikke et link",
             "Navn, rolle, organisation, arbejdstelefon, arbejdsmail, adressen i Roskilde og "
             "fits.dk — alt ligger inde i selve koden."),
            (ICON_OSS, "Din at læse og bygge om",
             "Apache-2.0, Kotlin og Jetpack Compose. Ret en kontakt i én fil, og QR-koden "
             "bliver genereret på ny ud fra den."),
        ],
        "install_h2": "Sådan installerer du den",
        "install_p": (
            "APK-filen bygges og signeres af GitHub Actions ved hver udgivelse, så det du "
            "henter, er præcis det workflowet byggede ud fra denne kildekode."
        ),
        "steps": [
            ("Hent APK-filen",
             f"Hent <code>{APK}</code> fra den nyeste udgivelse på GitHub."),
            ("Tillad installationen",
             "Android spørger én gang, om du vil stole på en app uden for Play Store. Det er "
             "den normale besked for en APK, du selv installerer."),
            ("Åbn og skift kort",
             "Skift mellem de tre kort med en swipe til højre eller venstre. Ræk telefonen "
             "frem, eller lad folk scanne direkte fra skærmen."),
        ],
        "footer_by": "Udviklet af",
        "footer_about": "Om FITS",
        "footer_src": "Kildekode",
        "footer_license": "Apache-2.0",
        "fullscreen": "Fuldskærm",
        "exit_fullscreen": "Forlad fuldskærm",
        "kiosk_link": "Åbn appen på sin egen side",
        "kiosk_title": "FITS QR — appen i fuldskærm",
        "kiosk_desc": (
            "FITS QR-appens skærm alene, i fuld størrelse. Skift mellem de tre kontakter og "
            "scan en kode for at gemme den."
        ),
        "back_label": "Tilbage til siden",
    },
}


def card_html(p: dict, s: dict) -> str:
    pre = s["prefix"]
    name = f"{p['first']} {p['last']}"
    return f"""        <article class="card" role="group" aria-roledescription="slide" aria-label="{name}">
          <div class="qr-wrap">
            <div class="qr-glow"></div>
            <div class="qr-card">
              <img src="{pre}{p['qr']}" width="568" height="568" alt="QR code holding {name}'s contact details" loading="lazy" decoding="async">
            </div>
          </div>
          <p class="scan-hint">{ICON_SCAN}{s['scan']}</p>
          <div class="rows">
            <div class="row">{ICON_PERSON}<div><div class="row-name">{name}</div><div class="row-role">{p['role']}</div></div></div>
            <div class="row">{ICON_MAIL}<div class="row-value">{p['email']}</div></div>
            <div class="row">{ICON_PHONE}<div class="row-value">{p['phone']}</div></div>
            <div class="row">{ICON_PIN}<div class="row-value">{ADDRESS}</div></div>
            <div class="row-foot"><b>fits.dk</b><i></i>{s['foot_note']}</div>
          </div>
        </article>"""


def vcard_markup(p: dict) -> str:
    out = []
    for line in vcard(p).strip().split("\r\n"):
        key, _, value = line.partition(":")
        if value:
            out.append(f'<span class="k">{key}:</span><span class="v">{value}</span>')
        else:
            out.append(f'<span class="k">{key}</span>')
    return "\n".join(out)


ICON_EXPAND = (
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<path d="M9 4.5H4.5V9M15 4.5H19.5V9M9 19.5H4.5V15M15 19.5H19.5V15" '
    'stroke="currentColor" stroke-width="1.9" stroke-linecap="round" '
    'stroke-linejoin="round"/></svg>'
)


def phone_block(s: dict, indent: str = "      ") -> str:
    """The app screen, 390x844 exactly. Shared by the landing hero and the fullscreen page."""
    cards = "\n".join(card_html(p, s) for p in PEOPLE)
    dots = "\n".join(
        f'          <button type="button" data-go="{i}" aria-current="{"true" if i == 0 else "false"}"'
        f' aria-label="{p["first"]} {p["last"]}"></button>'
        for i, p in enumerate(PEOPLE)
    )
    block = f"""<div class="phone" id="phone">
  <div class="phone-screen" id="screen" aria-label="{s['phone_label']}" tabindex="0" role="region">
    <div class="screen-grid"></div>
    <div class="app">
      <img class="app-logo" src="{s['prefix']}fits-logo-white.png" width="336" height="261" alt="FITS">
      <p class="app-tagline">AI-Powered Policy Automation</p>
      <div class="pager">
        <div class="track" id="track">
{cards}
        </div>
      </div>
      <div class="dots" id="dots" role="tablist" aria-label="{s['dots_label']}">
{dots}
      </div>
    </div>
  </div>
</div>"""
    return "\n".join(indent + line if line else line for line in block.split("\n"))


def vcards_json(indent: str = "  ") -> str:
    body = ",\n".join(
        "{}{}: {!r}".format(indent + "  ", i, vcard(p).strip()).replace("'", '"')
        for i, p in enumerate(PEOPLE)
    )
    return "{\n" + body + "\n" + indent + "}"


# Plain string, not an f-string: braces are JS, not placeholders.
PAGER_JS = """
(() => {
  const track = document.getElementById("track");
  const screen = document.getElementById("screen");
  const dots = [...document.querySelectorAll("#dots button")];
  const out = document.getElementById("vcard");
  const cards = [...track.children];
  const VCARDS = window.__FITS_VCARDS;

  let index = 0;

  const paint = () => {
    track.style.transform = `translate3d(${-index * 100}%, 0, 0)`;
    dots.forEach((d, i) => d.setAttribute("aria-current", String(i === index)));
    cards.forEach((c, i) => c.toggleAttribute("inert", i !== index));
    if (!out) return;
    out.innerHTML = VCARDS[index]
      .split("\r\n")
      .map((line) => {
        const at = line.indexOf(":");
        if (at < 0) return `<span class="k">${line}</span>`;
        return `<span class="k">${line.slice(0, at + 1)}</span><span class="v">${line.slice(at + 1)}</span>`;
      })
      .join("\n");
  };

  const go = (next) => {
    index = (next + cards.length) % cards.length;
    paint();
  };

  dots.forEach((d) => d.addEventListener("click", () => go(Number(d.dataset.go))));

  screen.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") { go(index - 1); e.preventDefault(); }
    if (e.key === "ArrowRight") { go(index + 1); e.preventDefault(); }
  });

  // Drag / swipe, mirroring the app's pager: follow the finger, then settle.
  let startX = null;
  let delta = 0;
  const move = (x) => {
    if (startX === null) return;
    delta = x - startX;
    track.style.transform = `translate3d(calc(${-index * 100}% + ${delta}px), 0, 0)`;
  };
  const up = () => {
    if (startX === null) return;
    track.classList.remove("dragging");
    const threshold = Math.min(90, track.getBoundingClientRect().width * 0.22);
    if (delta <= -threshold) go(index + 1);
    else if (delta >= threshold) go(index - 1);
    else paint();
    startX = null;
  };

  screen.addEventListener("pointerdown", (e) => {
    if (e.pointerType === "mouse" && e.button !== 0) return;
    startX = e.clientX;
    delta = 0;
    track.classList.add("dragging");
    screen.setPointerCapture(e.pointerId);
  });
  screen.addEventListener("pointermove", (e) => move(e.clientX));
  screen.addEventListener("pointerup", up);
  screen.addEventListener("pointercancel", up);
  screen.addEventListener("dragstart", (e) => e.preventDefault());

  paint();
})();
"""

# The app screen is a fixed 390x844 box, so it is scaled — never reflowed — to fill a
# viewport. That keeps it pixel-for-pixel the layout the phone shows.
FIT_JS = """
(() => {
  const phone = document.getElementById("phone");
  const fit = () => {
    const narrow = window.matchMedia("(max-width: 520px)").matches;
    // Bare 390x844 screen on small viewports; the framed 412x866 device elsewhere.
    const w = narrow ? 390 : 412;
    const h = narrow ? 844 : 866;
    const pad = narrow ? 0 : 56;
    const scale = Math.min(
      (window.innerWidth - pad) / w,
      (window.innerHeight - pad) / h,
    );
    phone.style.setProperty("--fit", String(Math.max(0.3, scale)));
  };
  fit();
  window.addEventListener("resize", fit);
  window.addEventListener("orientationchange", fit);
})();
"""

FULLSCREEN_JS = """
(() => {
  const btn = document.getElementById("go-fullscreen");
  const phone = document.getElementById("phone");
  if (!btn || !phone || !phone.requestFullscreen) return;

  const fit = () => {
    if (!document.fullscreenElement) {
      phone.style.removeProperty("--fit");
      return;
    }
    const scale = Math.min(window.innerWidth / 412, window.innerHeight / 866);
    phone.style.setProperty("--fit", String(Math.max(0.3, scale)));
  };

  btn.hidden = false;
  btn.addEventListener("click", () => {
    if (document.fullscreenElement) document.exitFullscreen();
    else phone.requestFullscreen().catch(() => {});
  });
  document.addEventListener("fullscreenchange", () => {
    btn.setAttribute("aria-pressed", String(Boolean(document.fullscreenElement)));
    fit();
  });
  window.addEventListener("resize", fit);
})();
"""


def page(lang: str) -> str:
    s = STRINGS[lang]
    pre = s["prefix"]
    canonical = f"{BASE}/" if lang == "en" else f"{BASE}/{lang}/"
    og_alt = "The FITS QR app screen, showing a contact card and its QR code"
    facts = "\n".join(
        f"""      <div class="fact">{icon}<h3>{title}</h3><p>{body}</p></div>"""
        for icon, title, body in s["facts"]
    )
    steps = "\n".join(
        f"""        <li><h3>{title}</h3><p>{body}</p></li>""" for title, body in s["steps"]
    )
    year = 2026
    phone = phone_block(s, indent="        ")
    vcards = vcards_json()
    app_href = "app/" if lang == "en" else "app/"

    return f"""<!doctype html>
<html lang="{s['lang']}" dir="{s['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{s['title']}</title>
<meta name="description" content="{s['description']}">
<meta name="author" content="Babak Bandpey">
<meta name="theme-color" content="#0b1524">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{BASE}/">
<link rel="alternate" hreflang="da" href="{BASE}/da/">
<link rel="alternate" hreflang="x-default" href="{BASE}/">
<link rel="icon" type="image/png" sizes="32x32" href="{pre}favicon-32.png">
<link rel="icon" type="image/png" sizes="180x180" href="{pre}favicon-180.png">
<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="FITS QR">
<meta property="og:locale" content="{'en_GB' if lang == 'en' else 'da_DK'}">
<meta property="og:locale:alternate" content="{'da_DK' if lang == 'en' else 'en_GB'}">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{s['title']}">
<meta property="og:description" content="{s['description']}">
<meta property="og:image" content="{BASE}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{og_alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{s['title']}">
<meta name="twitter:description" content="{s['description']}">
<meta name="twitter:image" content="{BASE}/og.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Inter+Tight:wght@700;800&family=IBM+Plex+Mono:wght@400;600&display=swap">
<link rel="stylesheet" href="{pre}styles.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "FITS QR",
  "operatingSystem": "Android 8.0+",
  "applicationCategory": "BusinessApplication",
  "url": "{canonical}",
  "downloadUrl": "{RELEASES}",
  "installUrl": "{RELEASES}",
  "codeRepository": "{REPO_URL}",
  "license": "https://www.apache.org/licenses/LICENSE-2.0",
  "isAccessibleForFree": true,
  "inLanguage": ["en", "da"],
  "description": "{s['description']}",
  "author": {{"@type": "Person", "name": "Babak Bandpey", "url": "https://cocode.dk"}},
  "publisher": {{"@type": "Organization", "name": "Cocode", "url": "https://cocode.dk"}},
  "offers": {{"@type": "Offer", "price": "0", "priceCurrency": "EUR"}},
  "about": {{"@type": "Organization", "name": "{ORG}", "url": "{WEBSITE}"}}
}}
</script>
</head>
<body>

<header class="masthead">
  <div class="shell">
    <a class="brand" href="{pre if lang != 'en' else ''}">
      <img src="{pre}fits-logo-white.png" width="336" height="261" alt="">
      FITS QR
    </a>
    <nav>
      <a class="lang-switch" href="{s['other_href']}" hreflang="{'da' if lang == 'en' else 'en'}">{s['other_label']}</a>
      <a class="btn btn-primary btn-sm" href="{RELEASES}">{ICON_DOWNLOAD}<span>{s['cta_apk']}</span></a>
    </nav>
  </div>
</header>

<main>
  <section class="hero">
    <div class="shell">
      <div>
        <p class="eyebrow">{s['eyebrow']}</p>
        <h1>{s['h1_a']}<br><em>{s['h1_b']}</em></h1>
        <p class="lede">{s['lede']}</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="{RELEASES}">{ICON_DOWNLOAD}{s['cta_apk']}</a>
          <a class="btn btn-ghost" href="{REPO_URL}">{ICON_CODE}{s['cta_src']}</a>
        </div>
        <p class="cta-note">{s['cta_note']}</p>
      </div>

      <div class="stage">
{phone}
        <div class="stage-controls">
          <button class="btn btn-ghost btn-sm" type="button" id="go-fullscreen" aria-pressed="false" hidden>{ICON_EXPAND}{s['fullscreen']}</button>
          <a class="stage-link" href="{app_href}">{s['kiosk_link']}</a>
        </div>
      </div>
    </div>
  </section>

  <section class="payload">
    <div class="shell">
      <div>
        <h2>{s['payload_h2']}</h2>
        <p>{s['payload_p']}</p>
      </div>
      <pre class="vcard" id="vcard" aria-live="polite">{vcard_markup(PEOPLE[0])}</pre>
    </div>
  </section>

  <section class="facts">
    <div class="shell">
{facts}
    </div>
  </section>

  <section class="install">
    <div class="shell">
      <h2>{s['install_h2']}</h2>
      <p>{s['install_p']}</p>
      <ol class="steps">
{steps}
      </ol>
    </div>
  </section>
</main>

<footer>
  <div class="shell">
    <span>© {year} <a href="https://cocode.dk" target="_blank" rel="noreferrer">Cocode</a></span>
    <span>{s['footer_by']} <a href="https://linkedin.com/in/babakbandpey" target="_blank" rel="noreferrer">Babak Bandpey</a></span>
    <span class="spacer"><a href="{WEBSITE}" target="_blank" rel="noreferrer">{s['footer_about']}</a></span>
    <span><a href="{REPO_URL}">{s['footer_src']}</a></span>
    <span><a href="{REPO_URL}/blob/main/LICENSE">{s['footer_license']}</a></span>
  </div>
</footer>

<script>
window.__FITS_VCARDS = {vcards};
</script>
<script>{PAGER_JS}</script>
<script>{FULLSCREEN_JS}</script>
</script>

</body>
</html>
"""


def kiosk(lang: str) -> str:
    """The app on its own page: no site chrome, the screen scaled to fill the viewport."""
    s = dict(STRINGS[lang])
    s["prefix"] = "../" if lang == "en" else "../../"
    pre = s["prefix"]
    canonical = f"{BASE}/app/" if lang == "en" else f"{BASE}/{lang}/app/"
    home = "../" if lang == "en" else "../"

    return f"""<!doctype html>
<html lang="{s['lang']}" dir="{s['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{s['kiosk_title']}</title>
<meta name="description" content="{s['kiosk_desc']}">
<meta name="theme-color" content="#0b1524">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{BASE}/app/">
<link rel="alternate" hreflang="da" href="{BASE}/da/app/">
<link rel="alternate" hreflang="x-default" href="{BASE}/app/">
<link rel="icon" type="image/png" sizes="32x32" href="{pre}favicon-32.png">
<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{s['kiosk_title']}">
<meta property="og:description" content="{s['kiosk_desc']}">
<meta property="og:image" content="{BASE}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{pre}styles.css">
</head>
<body class="kiosk">

<a class="kiosk-back" href="{home}">&#8592; {s['back_label']}</a>
<button class="kiosk-fs btn btn-ghost btn-sm" type="button" id="go-fullscreen" aria-pressed="false" hidden>{ICON_EXPAND}<span>{s['fullscreen']}</span></button>

<main class="kiosk-stage">
{phone_block(s, indent="  ")}
</main>

<script>
window.__FITS_VCARDS = {vcards_json()};
</script>
<script>{PAGER_JS}</script>
<script>{FIT_JS}</script>
<script>{FULLSCREEN_JS}</script>

</body>
</html>
"""


def main() -> None:
    (SITE / "index.html").write_text(page("en"), encoding="utf-8")
    (SITE / "da").mkdir(exist_ok=True)
    (SITE / "da" / "index.html").write_text(page("da"), encoding="utf-8")
    (SITE / "app").mkdir(exist_ok=True)
    (SITE / "app" / "index.html").write_text(kiosk("en"), encoding="utf-8")
    (SITE / "da" / "app").mkdir(exist_ok=True)
    (SITE / "da" / "app" / "index.html").write_text(kiosk("da"), encoding="utf-8")
    for rel in ("index.html", "da/index.html", "app/index.html", "da/app/index.html"):
        print(f"wrote {SITE / rel}")


if __name__ == "__main__":
    main()
