package dk.fits.contact

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxScope
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp

internal val Navy = Color(0xFF0B1524)
internal val NavyMid = Color(0xFF13233E)
internal val Indigo = Color(0xFF0818A0)
internal val Violet = Color(0xFF586EFF)
internal val Teal = Color(0xFF00B2B8)
internal val TealLight = Color(0xFF7FEAEF)

/** The navy gradient with two soft glows that every screen of the app sits on. */
@Composable
internal fun FitsBackdrop(content: @Composable BoxScope.() -> Unit) {
    Box(
        Modifier
            .fillMaxSize()
            .background(Brush.linearGradient(0f to Navy, 0.42f to NavyMid, 1f to Indigo)),
    ) {
        GlowBlob(Teal.copy(alpha = 0.20f), 420.dp, Alignment.TopStart)
        GlowBlob(Violet.copy(alpha = 0.28f), 380.dp, Alignment.BottomEnd)
        content()
    }
}

@Composable
private fun GlowBlob(color: Color, size: Dp, alignment: Alignment) {
    Box(Modifier.fillMaxSize(), contentAlignment = alignment) {
        Box(
            Modifier
                .size(size)
                .background(
                    Brush.radialGradient(listOf(color, Color.Transparent)),
                    RoundedCornerShape(50),
                ),
        )
    }
}
