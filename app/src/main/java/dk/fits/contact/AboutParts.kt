package dk.fits.contact

import androidx.annotation.StringRes
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.IconButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.heading
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

/** The small "i" in the corner of the contact screen that opens the About page. */
@Composable
internal fun AboutButton(onClick: () -> Unit, modifier: Modifier = Modifier) {
    val label = stringResource(R.string.open_about)
    IconButton(onClick, modifier.semantics { contentDescription = label }) { InfoIcon(TealLight) }
}

@Composable
internal fun ScreenTitle(@StringRes title: Int) = Text(
    stringResource(title),
    color = Color.White,
    fontSize = 24.sp,
    fontWeight = FontWeight.SemiBold,
    modifier = Modifier.semantics { heading() },
)

@Composable
internal fun SectionTitle(@StringRes title: Int) = Text(
    stringResource(title),
    color = TealLight,
    fontSize = 14.sp,
    fontWeight = FontWeight.SemiBold,
    letterSpacing = 0.8.sp,
    modifier = Modifier.padding(top = 20.dp).semantics { heading() },
)

@Composable
internal fun Body(text: String, muted: Boolean = false) = Text(
    text,
    color = Color.White.copy(alpha = if (muted) 0.7f else 0.9f),
    fontSize = if (muted) 13.sp else 15.sp,
    lineHeight = if (muted) 18.sp else 21.sp,
)

@Composable
internal fun Body(@StringRes text: Int, muted: Boolean = false) = Body(stringResource(text), muted)

/** A full-width pill, at least 48dp high, in the same teal outline as the tagline on the contact screen. */
@Composable
internal fun PillButton(@StringRes label: Int, onClick: () -> Unit) {
    val shape = RoundedCornerShape(50)
    Box(
        Modifier
            .fillMaxWidth()
            .heightIn(min = 48.dp)
            .clip(shape)
            .background(Teal.copy(alpha = 0.10f))
            .border(1.dp, Teal.copy(alpha = 0.45f), shape)
            .clickable(role = Role.Button, onClick = onClick)
            .padding(horizontal = 18.dp, vertical = 12.dp),
        contentAlignment = Alignment.Center,
    ) {
        Text(
            stringResource(label),
            color = TealLight,
            fontSize = 15.sp,
            fontWeight = FontWeight.SemiBold,
            textAlign = TextAlign.Center,
        )
    }
}
