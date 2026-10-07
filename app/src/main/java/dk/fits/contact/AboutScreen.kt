package dk.fits.contact

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.systemBarsPadding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp

/**
 * The About page, in the order the cocode-apps standard asks for. [openLink] returns false when no
 * app can open the link, and the page then says so under that button instead of failing silently.
 */
@Composable
fun AboutScreen(version: String, openLink: (AboutLink) -> Boolean, onBack: () -> Unit) {
    var failedLink by rememberSaveable { mutableStateOf<AboutLink?>(null) }

    @Composable
    fun LinkButton(link: AboutLink, label: Int) {
        PillButton(label) { failedLink = if (openLink(link)) null else link }
        if (failedLink == link) Body(R.string.link_no_browser)
    }

    FitsBackdrop {
        Column(
            Modifier
                .fillMaxSize()
                .systemBarsPadding()
                .verticalScroll(rememberScrollState())
                .padding(horizontal = 24.dp, vertical = 14.dp),
            verticalArrangement = Arrangement.spacedBy(10.dp),
        ) {
            PillButton(R.string.action_back, onBack)

            // 1. Name and version
            ScreenTitle(R.string.about_title)
            Body(stringResource(R.string.about_version, version))
            LinkButton(AboutLink.LatestVersion, R.string.about_check_updates)
            Body(R.string.about_update_hint, muted = true)

            // 2. What the app does
            SectionTitle(R.string.about_what_title)
            Body(R.string.about_what)

            // 3. Privacy: the promises, and the policy link once a policy is published
            SectionTitle(R.string.about_privacy_title)
            Body(R.string.about_privacy_permissions)
            Body(R.string.about_privacy_network)
            Body(R.string.about_privacy_scan)
            Body(R.string.about_privacy_data)
            if (aboutUrl(AboutLink.Privacy) != null) LinkButton(AboutLink.Privacy, R.string.about_privacy_link)

            // 4. Links
            SectionTitle(R.string.about_links_title)
            Body(R.string.about_links_hint, muted = true)
            LinkButton(AboutLink.Website, R.string.about_website)
            LinkButton(AboutLink.Source, R.string.about_source)
            LinkButton(AboutLink.Issues, R.string.about_report)

            // 5. Credits and licenses
            SectionTitle(R.string.about_credits_title)
            Body(R.string.credit_license)
            Body(R.string.credit_brand)
            Body(R.string.credit_zxing)
            Body(R.string.credit_androidx)

            // 6. Made by Cocode
            SectionTitle(R.string.about_made_by)
            Body(R.string.about_published_for)

            // 7. Support: intentionally empty until the Support phase (see cocode-apps standard/support.md).
        }
    }
}
