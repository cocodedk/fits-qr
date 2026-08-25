package dk.fits.contact

/** Company-level facts, shared by every contact card. */
object Fits {
    const val ORG = "FITS - Framework for IT Security"
    const val TAGLINE = "AI-Powered Policy Automation"
    const val STREET = "Københavnsvej 19B"
    const val POSTAL_CODE = "4000"
    const val CITY = "Roskilde"
    const val COUNTRY = "Denmark"
    const val WEBSITE = "https://fits.dk"

    const val ADDRESS = "$STREET, $POSTAL_CODE $CITY"
}

data class Contact(
    val firstName: String,
    val lastName: String,
    val role: String?,
    val email: String,
    val phone: String,
) {
    val fullName: String get() = "$firstName $lastName"

    /** The subtitle under the name: their role, or the company when they have none. */
    val subtitle: String get() = role ?: "FITS — Framework for IT Security"

    /**
     * vCard 3.0 — the version both iOS and Android camera apps offer to save as a contact.
     * CRLF line endings are required by RFC 2426.
     */
    val vCard: String
        get() = buildList {
            add("BEGIN:VCARD")
            add("VERSION:3.0")
            add("N:$lastName;$firstName;;;")
            add("FN:$fullName")
            add("ORG:${Fits.ORG}")
            role?.let { add("TITLE:$it") }
            add("TEL;TYPE=WORK,VOICE:$phone")
            add("EMAIL;TYPE=WORK,INTERNET:$email")
            add("ADR;TYPE=WORK:;;${Fits.STREET};${Fits.CITY};;${Fits.POSTAL_CODE};${Fits.COUNTRY}")
            add("URL:${Fits.WEBSITE}")
            add("END:VCARD")
        }.joinToString("\r\n") + "\r\n"
}

val contacts = listOf(
    Contact(
        firstName = "Bassil",
        lastName = "Salameh",
        role = "CEO",
        email = "fits@l7consulting.dk",
        phone = "+45 22 547 547",
    ),
    Contact(
        firstName = "Babak",
        lastName = "Bandpey",
        role = "CTO",
        email = "bba@l7consulting.dk",
        phone = "+45 27 82 30 77",
    ),
    Contact(
        firstName = "Silas Stilling",
        lastName = "Jørgensen",
        role = "Cybersecurity Developer",
        email = "ssj@l7consulting.dk",
        phone = "+45 61 26 89 99",
    ),
)
