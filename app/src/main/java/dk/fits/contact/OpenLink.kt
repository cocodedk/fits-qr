package dk.fits.contact

import android.content.ActivityNotFoundException
import android.content.Context
import android.content.Intent
import androidx.core.net.toUri

/**
 * Hands an About link to the phone's browser. The app has no internet permission of its own, so it
 * never loads a page itself. The website and privacy pages follow the language the app shows (its
 * resources' first locale). Returns false when there is no link or no app can open it.
 */
fun openAboutLink(context: Context, link: AboutLink): Boolean {
    val language = context.resources.configuration.locales[0].language
    val url = aboutUrl(link, language) ?: return false
    return try {
        context.startActivity(
            Intent(Intent.ACTION_VIEW, url.toUri()).addCategory(Intent.CATEGORY_BROWSABLE),
        )
        true
    } catch (_: ActivityNotFoundException) {
        false
    }
}
