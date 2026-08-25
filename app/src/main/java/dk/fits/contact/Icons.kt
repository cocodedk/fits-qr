package dk.fits.contact

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.PathParser
import androidx.compose.ui.graphics.StrokeCap
import androidx.compose.ui.graphics.StrokeJoin
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.graphics.drawscope.scale
import androidx.compose.ui.unit.dp

/** Strokes an icon authored on a 24x24 grid, scaled to the composable's size. */
@Composable
private fun StrokeIcon(pathData: String, sizeDp: Int, color: Color, strokeWidth: Float = 1.6f) {
    val path = remember(pathData) { PathParser().parsePathString(pathData).toPath() }
    Canvas(Modifier.size(sizeDp.dp)) {
        val factor = size.minDimension / 24f
        scale(factor, factor, pivot = Offset.Zero) {
            drawPath(
                path,
                color,
                style = Stroke(width = strokeWidth, cap = StrokeCap.Round, join = StrokeJoin.Round),
            )
        }
    }
}

@Composable
fun MailIcon(color: Color = Color(0xFF00B2B8)) = StrokeIcon(
    "M5 5h14a2.5 2.5 0 0 1 2.5 2.5v9A2.5 2.5 0 0 1 19 19H5a2.5 2.5 0 0 1-2.5-2.5v-9A2.5 2.5 0 0 1 5 5z " +
        "M3.5 7.2 12 13.2 20.5 7.2",
    18,
    color,
)

@Composable
fun PhoneIcon(color: Color = Color(0xFF00B2B8)) = StrokeIcon(
    "M6.2 3.5h3l1.6 4-2 1.4a11.4 11.4 0 0 0 5.3 5.3l1.4-2 4 1.6v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.2 5.7a2 2 0 0 1 2-2.2z",
    18,
    color,
)

@Composable
fun PinIcon(color: Color = Color(0xFF00B2B8)) = StrokeIcon(
    "M12 21c4-4.2 6-7.3 6-10a6 6 0 1 0-12 0c0 2.7 2 5.8 6 10z " +
        "M12 12.8a2.2 2.2 0 1 0 0-4.4 2.2 2.2 0 0 0 0 4.4z",
    18,
    color,
)

@Composable
fun PersonIcon(color: Color = Color(0xFF00B2B8)) = StrokeIcon(
    "M12 11.6a3.6 3.6 0 1 0 0-7.2 3.6 3.6 0 0 0 0 7.2z " +
        "M4.8 20c0-3.6 3.2-5.6 7.2-5.6s7.2 2 7.2 5.6",
    18,
    color,
)

@Composable
fun ScanIcon(color: Color) = StrokeIcon(
    "M3.5 5H20.5V19H3.5Z M7 9.5V7.5h2 M17 9.5V7.5h-2 M7 14.5v2h2 M17 14.5v2h-2",
    16,
    color,
    strokeWidth = 1.5f,
)
