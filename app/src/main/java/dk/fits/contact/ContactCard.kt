package dk.fits.contact

import androidx.compose.animation.core.RepeatMode
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.blur
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.FilterQuality
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.toArgb
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
internal fun ContactCardPage(contact: Contact) {
    val qr = remember(contact) {
        encodeQr(contact.vCard, dark = Navy.toArgb(), light = Color.White.toArgb())
    }

    Column(
        Modifier
            .fillMaxSize()
            .padding(horizontal = 24.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
    ) {
        // The QR takes the leftover height, so a short screen shrinks the code
        // instead of clipping the details below it.
        QrCard(qr, contact.fullName, Modifier.weight(1f).fillMaxWidth())
        Spacer(Modifier.height(6.dp))
        ScanHint()
        Spacer(Modifier.height(16.dp))
        ContactDetails(contact)
    }
}

@Composable
private fun QrCard(qr: ImageBitmap, name: String, modifier: Modifier = Modifier) {
    val pulse by rememberInfiniteTransition(label = "glow").animateFloat(
        initialValue = 1f,
        targetValue = 1.08f,
        animationSpec = infiniteRepeatable(tween(2250), RepeatMode.Reverse),
        label = "pulse",
    )

    Box(modifier, contentAlignment = Alignment.Center) {
        Box(
            Modifier
                .fillMaxHeight()
                .heightIn(max = 296.dp)
                .aspectRatio(1f, matchHeightConstraintsFirst = true),
            contentAlignment = Alignment.Center,
        ) {
            Box(
                Modifier
                    .matchParentSize()
                    .scale(pulse * 1.14f)
                    .blur(20.dp)
                    .background(
                        Brush.radialGradient(listOf(Teal.copy(alpha = 0.55f), Color.Transparent)),
                        RoundedCornerShape(40.dp),
                    ),
            )
            Box(
                Modifier
                    .matchParentSize()
                    .clip(RoundedCornerShape(26.dp))
                    .background(Color.White)
                    .padding(14.dp),
            ) {
                Image(
                    bitmap = qr,
                    contentDescription = stringResource(R.string.qr_description, name),
                    modifier = Modifier.fillMaxSize(),
                    contentScale = ContentScale.Fit,
                    filterQuality = FilterQuality.None,
                )
            }
        }
    }
}

@Composable
private fun ScanHint() {
    Row(verticalAlignment = Alignment.CenterVertically) {
        ScanIcon(TealLight)
        Spacer(Modifier.width(8.dp))
        Text(
            stringResource(R.string.scan_hint),
            color = Color.White.copy(alpha = 0.86f),
            fontSize = 13.sp,
            fontWeight = FontWeight.SemiBold,
        )
    }
}
