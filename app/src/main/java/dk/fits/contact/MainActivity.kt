package dk.fits.contact

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.BackHandler
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.systemBarsPadding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.pager.HorizontalPager
import androidx.compose.foundation.pager.PagerState
import androidx.compose.foundation.pager.rememberPagerState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.alpha
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlin.math.absoluteValue

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
                Surface(color = Navy) { FitsApp() }
            }
        }
    }
}

/** The contact pager, or the About page on top of it. The pager keeps its place while About is open. */
@Composable
private fun FitsApp() {
    val context = LocalContext.current
    var showAbout by rememberSaveable { mutableStateOf(false) }
    val pagerState = rememberPagerState(
        initialPage = VIRTUAL_PAGES / 2 - (VIRTUAL_PAGES / 2) % contacts.size,
        pageCount = { VIRTUAL_PAGES },
    )
    if (showAbout) {
        BackHandler { showAbout = false }
        AboutScreen(
            version = BuildConfig.VERSION_NAME,
            openLink = { openAboutLink(context, it) },
            onBack = { showAbout = false },
        )
    } else {
        ContactPager(pagerState, onAbout = { showAbout = true })
    }
}

@Composable
private fun ContactPager(pagerState: PagerState, onAbout: () -> Unit) {
    FitsBackdrop {
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
        AboutButton(
            onAbout,
            Modifier
                .align(Alignment.TopEnd)
                .systemBarsPadding()
                .padding(end = 4.dp),
        )
    }
}

@Composable
private fun Header() {
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        Image(
            painter = painterResource(R.drawable.fits_logo),
            contentDescription = stringResource(R.string.app_name),
            modifier = Modifier.width(126.dp),
            contentScale = ContentScale.FillWidth,
        )
        Spacer(Modifier.height(9.dp))
        Text(
            stringResource(R.string.tagline),
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
    MaterialTheme(colorScheme = darkColorScheme()) { FitsApp() }
}
