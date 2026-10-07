"""The privacy pages: website/privacy/index.html (English) and website/da/privacy/index.html (Danish).

build-site.py calls `page(lang, base)` and writes the result, so the policy is regenerated with the
rest of the site and the cocode-apps blocks (navigation, footer) are carried over like on the home page.
The pages sit one folder deeper than the home page, so every asset and the language switch are relative
to that depth; the shared navigation block (written by `python3 -m tools.render`) uses the /fits-qr/ prefix.

No web fonts are loaded here: a privacy page should not call out to Google just to be read.
"""
from __future__ import annotations

from privacy_common import WEBSITE
from privacy_text import TEXT


def page(lang: str, base: str) -> str:
    s = TEXT[lang]
    pre = "../" if lang == "en" else "../../"
    here = f"{base}/privacy/" if lang == "en" else f"{base}/da/privacy/"
    other_url = f"{base}/da/privacy/" if lang == "en" else f"{base}/privacy/"
    switch = "../da/privacy/" if lang == "en" else "../../privacy/"
    en_url, da_url = (here, other_url) if lang == "en" else (other_url, here)
    body = "\n".join(
        f"    <h2>{heading}</h2>\n" + "\n".join(f"    <p>{p}</p>" for p in paragraphs)
        for heading, paragraphs in s["sections"]
    )
    return f"""<!doctype html>
<html lang="{lang}" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{s['title']}</title>
<meta name="description" content="{s['description']}">
<meta name="author" content="Babak Bandpey">
<meta name="theme-color" content="#0b1524">
<link rel="canonical" href="{here}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="da" href="{da_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<link rel="icon" type="image/png" sizes="32x32" href="{pre}favicon-32.png">
<link rel="icon" type="image/png" sizes="180x180" href="{pre}favicon-180.png">
<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="FITS QR">
<meta property="og:locale" content="{s['locale']}">
<meta property="og:url" content="{here}">
<meta property="og:title" content="{s['title']}">
<meta property="og:description" content="{s['description']}">
<meta property="og:image" content="{base}/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="{pre}styles.css">
</head>
<body>

<header class="masthead">
  <div class="shell">
    <!-- cocode-apps:nav:start --><!-- cocode-apps:nav:end -->
    <a class="lang-switch" href="{switch}" hreflang="{s['other']}" lang="{s['other']}">{s['other_label']}</a>
  </div>
</header>

<main id="main" tabindex="-1" class="legal">
  <div class="shell">
    <h1>{s['title']}</h1>
    <p class="meta">{s['effective']}</p>
{body}
    <p class="back"><a href="../">{s['back']}</a></p>
  </div>
</main>

<div class="site-foot">
  <div class="shell">
    <!-- cocode-apps:footer:start --><!-- cocode-apps:footer:end -->
    <a class="foot-about" href="{WEBSITE}" target="_blank" rel="noreferrer">{s['about']}</a>
  </div>
</div>

</body>
</html>
"""
