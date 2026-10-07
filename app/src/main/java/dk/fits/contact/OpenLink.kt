package dk.fits.contact

import android.content.ActivityNotFoundException
import android.content.Context
import android.content.Intent
import androidx.core.net.toUri

/**
 * Hands an About link to the phone's browser. The app has no internet permission of its own, so it
 * never loads a page itself. Returns false when there is no link or no app can open it.
 */
fun openAboutLink(context: Context, link: AboutLink): Boolean {
    val url = aboutUrl(link) ?: return false
    return try {
        context.startActivity(
            Intent(Intent.ACTION_VIEW, url.toUri()).addCategory(Intent.CATEGORY_BROWSABLE),
        )
        true
    } catch (_: ActivityNotFoundException) {
        false
    }
}
