# R8 keep rules for the FITS QR app's release build.
#
# The app has no reflection, no JSON model classes, no JNI and no WebView bridge —
# just Compose UI, a static contact list (Fits.kt) and ZXing for QR encoding. ZXing's
# own AAR/jar ships no consumer rules and does no reflection-based lookups (it only
# does bit manipulation and pure encoding), so no library-specific keep rule is needed.
# This file intentionally starts empty of app keep rules; add one here, with a comment
# naming the class/library it protects, only when a real R8 warning demands it.
