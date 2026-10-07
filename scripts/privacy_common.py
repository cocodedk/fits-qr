"""Links and fragments shared by the privacy text (English and Danish) and the site builder."""
from __future__ import annotations

WEBSITE = "https://fits.dk"  # FITS's own site; build-site.py and privacy_pages.py both link it
ISSUES = "https://github.com/cocodedk/fits-qr/issues"
DPA = "https://www.datatilsynet.dk/english"
MAIL = '<a href="mailto:bb@cocode.dk">bb@cocode.dk</a>'
# <wbr> lets the long name break at an underscore on a narrow screen.
PERMISSION = "<code>dk.fits.contact.DYNAMIC_RECEIVER_<wbr>NOT_EXPORTED_<wbr>PERMISSION</code>"
