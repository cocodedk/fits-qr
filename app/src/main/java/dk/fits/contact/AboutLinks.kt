package dk.fits.contact

enum class AboutLink { LatestVersion, Privacy, Website, Source, Issues }

private const val REPO_URL = "https://github.com/cocodedk/fits-qr"
private const val SITE_URL = "https://cocodedk.github.io/fits-qr"

/** Set to true once the app is live on F-Droid (`fdroid: live` in cocode-apps' apps.yml). */
const val ON_FDROID = false

/** The privacy policy page. Null until one is published; the About page then leaves its link out. */
val PRIVACY_URL: String? = null

/**
 * Where an About link leads, or null when there is nowhere to send the person (no privacy
 * policy published yet). Plain strings only, so the unit tests need no Android.
 */
fun aboutUrl(
    link: AboutLink,
    onFdroid: Boolean = ON_FDROID,
    privacyUrl: String? = PRIVACY_URL,
    applicationId: String = BuildConfig.APPLICATION_ID,
): String? = when (link) {
    AboutLink.LatestVersion ->
        if (onFdroid) "https://f-droid.org/packages/$applicationId/" else "$REPO_URL/releases/latest"
    AboutLink.Privacy -> privacyUrl
    AboutLink.Website -> SITE_URL
    AboutLink.Source -> REPO_URL
    AboutLink.Issues -> "$REPO_URL/issues"
}
