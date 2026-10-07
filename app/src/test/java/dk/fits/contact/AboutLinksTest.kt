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
    fun privacyLinkIsLeftOutWhenThereIsNoPolicy() {
        assertNull(aboutUrl(AboutLink.Privacy, privacyUrl = null))
    }

    @Test
    fun websiteSourceAndIssuesPointAtTheProject() {
        assertEquals("https://cocodedk.github.io/fits-qr", aboutUrl(AboutLink.Website))
        assertEquals("https://github.com/cocodedk/fits-qr", aboutUrl(AboutLink.Source))
        assertEquals("https://github.com/cocodedk/fits-qr/issues", aboutUrl(AboutLink.Issues))
    }

    @Test
    fun everyLinkButPrivacyAlwaysHasATarget() {
        for (link in AboutLink.entries - AboutLink.Privacy) assertNotNull(link.name, aboutUrl(link))
    }
}
