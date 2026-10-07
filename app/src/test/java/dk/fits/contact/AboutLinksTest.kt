package dk.fits.contact

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Test

class AboutLinksTest {
    private val appId = "dk.fits.contact"

    @Test
    fun latestVersionOpensTheGitHubReleaseUntilTheAppIsOnFdroid() {
        assertEquals(
            "https://github.com/cocodedk/fits-qr/releases/latest",
            aboutUrl(AboutLink.LatestVersion, onFdroid = false, applicationId = appId),
        )
    }

    @Test
    fun latestVersionOpensTheFdroidPageOnceTheAppIsLive() {
        assertEquals(
            "https://f-droid.org/packages/dk.fits.contact/",
            aboutUrl(AboutLink.LatestVersion, onFdroid = true, applicationId = appId),
        )
    }

    @Test
    fun privacyLinkIsPresentWhenAPolicyIsPublished() {
        val url = "https://cocodedk.github.io/fits-qr/privacy/"
        assertEquals(url, aboutUrl(AboutLink.Privacy, privacyUrl = url))
    }

    @Test
    fun privacyLinkDefaultsToThePublishedPolicy() {
        assertEquals("https://cocodedk.github.io/fits-qr/privacy/", aboutUrl(AboutLink.Privacy))
    }

    @Test
    fun englishOpensTheEnglishWebsiteAndPrivacyPages() {
        assertEquals("https://cocodedk.github.io/fits-qr", aboutUrl(AboutLink.Website, "en"))
        assertEquals("https://cocodedk.github.io/fits-qr/privacy/", aboutUrl(AboutLink.Privacy, "en"))
    }

    @Test
    fun danishOpensTheDanishWebsiteAndPrivacyPages() {
        assertEquals("https://cocodedk.github.io/fits-qr/da/", aboutUrl(AboutLink.Website, "da"))
        assertEquals("https://cocodedk.github.io/fits-qr/da/privacy/", aboutUrl(AboutLink.Privacy, "da"))
    }

    @Test
    fun aLanguageTheSiteLacksFallsBackToTheEnglishPages() {
        for (language in listOf("fa", "fr")) {
            assertEquals("https://cocodedk.github.io/fits-qr", aboutUrl(AboutLink.Website, language))
            assertEquals("https://cocodedk.github.io/fits-qr/privacy/", aboutUrl(AboutLink.Privacy, language))
        }
    }

    @Test
    fun sourceIssuesAndLatestVersionDoNotFollowTheLanguage() {
        for (language in listOf("en", "da", "fa")) {
            assertEquals("https://github.com/cocodedk/fits-qr", aboutUrl(AboutLink.Source, language))
            assertEquals("https://github.com/cocodedk/fits-qr/issues", aboutUrl(AboutLink.Issues, language))
            assertEquals(
                "https://github.com/cocodedk/fits-qr/releases/latest",
                aboutUrl(AboutLink.LatestVersion, language, onFdroid = false),
            )
        }
    }

    @Test
    fun anAddressOutsideTheSiteIsNeverRewritten() {
        val url = "https://example.org/privacy/"
        assertEquals(url, aboutUrl(AboutLink.Privacy, "da", privacyUrl = url))
    }

    @Test
    fun privacyLinkIsLeftOutWhenThereIsNoPolicy() {
        assertNull(aboutUrl(AboutLink.Privacy, privacyUrl = null))
        assertNull(aboutUrl(AboutLink.Privacy, "da", privacyUrl = null))
    }

    @Test
    fun websiteSourceAndIssuesPointAtTheProject() {
        assertEquals("https://cocodedk.github.io/fits-qr", aboutUrl(AboutLink.Website))
        assertEquals("https://github.com/cocodedk/fits-qr", aboutUrl(AboutLink.Source))
        assertEquals("https://github.com/cocodedk/fits-qr/issues", aboutUrl(AboutLink.Issues))
    }

    @Test
    fun everyLinkHasATargetByDefault() {
        for (link in AboutLink.entries) assertNotNull(link.name, aboutUrl(link))
    }
}
