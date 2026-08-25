package dk.fits.contact

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.animation.core.RepeatMode
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.systemBarsPadding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.pager.HorizontalPager
import androidx.compose.foundation.pager.rememberPagerState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.alpha
import androidx.compose.ui.draw.blur
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.FilterQuality
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.toArgb
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlin.math.absoluteValue

private val Navy = Color(0xFF0B1524)
private val NavyMid = Color(0xFF13233E)
private val Indigo = Color(0xFF0818A0)
private val Violet = Color(0xFF586EFF)
private val Teal = Color(0xFF00B2B8)
private val TealLight = Color(0xFF7FEAEF)

/**
 * A large virtual page count makes the pager wrap around endlessly; the real card is
 * `page % contacts.size`. Starting in the middle leaves room to swipe both ways.
 */
private const val VIRTUAL_PAGES = 100_000

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        enableEdgeToEdge()
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme(colorScheme = darkColorScheme(background = Navy, surface = Navy)) {
                Surface(color = Navy) { ContactPager() }
            }
        }
    }
}

@Composable
private fun ContactPager() {
    val pagerState = rememberPagerState(
        initialPage = VIRTUAL_PAGES / 2 - (VIRTUAL_PAGES / 2) % contacts.size,
        pageCount = { VIRTUAL_PAGES },
    )

    Box(
        Modifier
            .fillMaxSize()
            .background(Brush.linearGradient(0f to Navy, 0.42f to NavyMid, 1f to Indigo)),
    ) {
        GlowBlob(Teal.copy(alpha = 0.20f), 420.dp, Alignment.TopStart)
        GlowBlob(Violet.copy(alpha = 0.28f), 380.dp, Alignment.BottomEnd)

        Column(
            Modifier
                .fillMaxSize()
                .systemBarsPadding()
                .padding(top = 14.dp, bottom = 10.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
        ) {
            Header()
            HorizontalPager(
                state = pagerState,
                modifier = Modifier.weight(1f),
                pageSpacing = 8.dp,
            ) { page ->
                val offset = (pagerState.currentPage - page + pagerState.currentPageOffsetFraction)
                    .absoluteValue
                    .coerceIn(0f, 1f)
                Box(
                    Modifier
                        .fillMaxSize()
                        .alpha(1f - offset * 0.6f)
                        .scale(1f - offset * 0.06f),
                ) {
                    ContactCardPage(contacts[page % contacts.size])
                }
            }
            PageDots(pagerState.currentPage % contacts.size)
        }
    }
}

@Composable
private fun ContactCardPage(contact: Contact) {
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

@Composable
private fun Header() {
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        Image(
            painter = painterResource(R.drawable.fits_logo),
            contentDescription = "FITS",
            modifier = Modifier.width(126.dp),
            contentScale = ContentScale.FillWidth,
        )
        Spacer(Modifier.height(9.dp))
        Text(
            Fits.TAGLINE,
            color = TealLight,
            fontSize = 12.sp,
            fontWeight = FontWeight.SemiBold,
            modifier = Modifier
                .clip(RoundedCornerShape(50))
                .background(Teal.copy(alpha = 0.10f))
                .border(1.dp, Teal.copy(alpha = 0.45f), RoundedCornerShape(50))
                .padding(horizontal = 14.dp, vertical = 5.dp),
        )
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
                    contentDescription = "QR code with $name's contact details",
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
            "Scan to save the contact",
            color = Color.White.copy(alpha = 0.86f),
            fontSize = 13.sp,
            fontWeight = FontWeight.SemiBold,
        )
    }
}

@Composable
private fun ContactDetails(contact: Contact) {
    Column(
        Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(20.dp))
            .background(Color.White.copy(alpha = 0.10f)),
        verticalArrangement = Arrangement.spacedBy(1.dp),
    ) {
        Row(
            Modifier
                .fillMaxWidth()
                .background(Navy.copy(alpha = 0.55f))
                .padding(horizontal = 18.dp, vertical = 12.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            PersonIcon()
            Spacer(Modifier.width(14.dp))
            Column {
                Text(
                    contact.fullName,
                    color = Color.White,
                    fontSize = 15.sp,
                    fontWeight = FontWeight.SemiBold,
                )
                Text(
                    contact.subtitle,
                    color = TealLight.copy(alpha = 0.75f),
                    fontSize = 11.sp,
                    fontWeight = FontWeight.Medium,
                )
            }
        }
        ContactRow(contact.email) { MailIcon() }
        ContactRow(contact.phone) { PhoneIcon() }
        ContactRow(Fits.ADDRESS) { PinIcon() }
        Row(
            Modifier
                .fillMaxWidth()
                .background(Navy.copy(alpha = 0.55f))
                .background(Teal.copy(alpha = 0.14f))
                .padding(horizontal = 18.dp, vertical = 13.dp),
            horizontalArrangement = Arrangement.Center,
            verticalAlignment = Alignment.CenterVertically,
        ) {
            Text(
                "fits.dk",
                color = TealLight,
                fontSize = 13.sp,
                fontWeight = FontWeight.SemiBold,
                letterSpacing = 0.8.sp,
            )
            Spacer(Modifier.width(8.dp))
            Box(
                Modifier
                    .size(4.dp)
                    .background(TealLight.copy(alpha = 0.5f), RoundedCornerShape(50)),
            )
            Spacer(Modifier.width(8.dp))
            Text(
                "Danish product · European hosting",
                color = Color.White.copy(alpha = 0.55f),
                fontSize = 12.sp,
                fontWeight = FontWeight.Medium,
            )
        }
    }
}

@Composable
private fun ContactRow(value: String, icon: @Composable () -> Unit) {
    Row(
        Modifier
            .fillMaxWidth()
            .background(Navy.copy(alpha = 0.55f))
            .padding(horizontal = 18.dp, vertical = 12.dp),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        icon()
        Spacer(Modifier.width(14.dp))
        Text(value, color = Color.White, fontSize = 14.sp, fontWeight = FontWeight.Medium)
    }
}

@Composable
private fun PageDots(selected: Int) {
    Row(
        Modifier.padding(top = 12.dp),
        horizontalArrangement = Arrangement.spacedBy(8.dp),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        contacts.forEachIndexed { index, _ ->
            val active = index == selected
            val width by animateFloatAsState(if (active) 22f else 7f, label = "dotWidth")
            Box(
                Modifier
                    .width(width.dp)
                    .height(7.dp)
                    .background(
                        if (active) Teal else Color.White.copy(alpha = 0.25f),
                        RoundedCornerShape(50),
                    ),
            )
        }
    }
}

@Preview(widthDp = 390, heightDp = 844)
@Composable
private fun ContactPagerPreview() {
    MaterialTheme(colorScheme = darkColorScheme()) { ContactPager() }
}
