package dk.fits.contact

enum class AboutLink { LatestVersion, Privacy, Website, Source, Issues }

private const val REPO_URL = "https://github.com/cocodedk/fits-qr"
private const val SITE_URL = "https://cocodedk.github.io/fits-qr"

/** Set to true once the app is live on F-Droid (`fdroid: live` in cocode-apps' apps.yml). */
const val ON_FDROID = false

/** The privacy policy page. When this is null, the About page leaves the privacy link out. */
val PRIVACY_URL: String? = "https://cocodedk.github.io/fits-qr/privacy/"

/**
 * Languages the site has both a home page and a privacy page for, at `<site>/<code>/` and
 * `<site>/<code>/privacy/` (the site lives under the /fits-qr/ sub-path of cocodedk.github.io).
 * Every other language opens the English pages.
 */
private val SITE_LANGUAGES = setOf("da")

/** [url] on the site in [language], or [url] itself when the site has no pages in that language. */
private fun inLanguage(url: String, language: String): String =
    if (language in SITE_LANGUAGES && url.startsWith("$SITE_URL/")) {
        "$SITE_URL/$language/${url.removePrefix("$SITE_URL/")}"
    } else {
        url
    }

/**
 * Where an About link leads, or null when there is nowhere to send the person (no privacy
 * policy published yet). The website and privacy links follow [language] (a code such as "da"
 * from the app's current locale) and open the English pages when the site has none in that
 * language. Plain strings only, so the unit tests need no Android.
 */
fun aboutUrl(
    link: AboutLink,
    language: String = "en",
    onFdroid: Boolean = ON_FDROID,
    privacyUrl: String? = PRIVACY_URL,
    applicationId: String = BuildConfig.APPLICATION_ID,
): String? = when (link) {
    AboutLink.LatestVersion ->
        if (onFdroid) "https://f-droid.org/packages/$applicationId/" else "$REPO_URL/releases/latest"
    AboutLink.Privacy -> privacyUrl?.let { inLanguage(it, language) }
    AboutLink.Website -> if (language in SITE_LANGUAGES) "$SITE_URL/$language/" else SITE_URL
    AboutLink.Source -> REPO_URL
    AboutLink.Issues -> "$REPO_URL/issues"
}
