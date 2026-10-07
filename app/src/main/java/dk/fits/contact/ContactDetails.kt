package dk.fits.contact

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
internal fun ContactDetails(contact: Contact) {
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
                    contact.role ?: stringResource(R.string.fits_full_name),
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
                stringResource(R.string.fits_domain),
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
                stringResource(R.string.fits_product_note),
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
