plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.kotlin.compose)
}

// Version: the git tag (vMAJOR.MINOR.PATCH) is the single source of truth. The release
// workflow passes it as an environment variable; a Gradle property overrides it locally.
// Local/debug builds have neither and fall back to a dev version.
val appVersionName: String =
    providers.gradleProperty("VERSION_NAME").filter { it.isNotBlank() }
        .orElse(providers.environmentVariable("VERSION_NAME").filter { it.isNotBlank() })
        .getOrElse("0.1.0")
        .removePrefix("v")
val semver: List<String> = appVersionName.split(".")
val appVersionCode: Int = (semver.getOrNull(0)?.toIntOrNull() ?: 0) * 1_000_000 +
    (semver.getOrNull(1)?.toIntOrNull() ?: 0) * 1_000 +
    (semver.getOrNull(2)?.toIntOrNull() ?: 0)

// Optional release signing — supplied via env in CI; absent locally so debug still builds.
val ksFile = System.getenv("KEYSTORE_PATH")?.takeIf { it.isNotBlank() }
    ?.let { rootProject.file(it).absoluteFile }?.takeIf { it.isFile }
val ksPassword = System.getenv("KEYSTORE_PASSWORD")?.takeIf { it.isNotBlank() }
val ksAlias = System.getenv("KEY_ALIAS")?.takeIf { it.isNotBlank() }
val ksKeyPassword = System.getenv("KEY_PASSWORD")?.takeIf { it.isNotBlank() }
val hasSigning = ksFile != null && ksPassword != null && ksAlias != null && ksKeyPassword != null

android {
    namespace = "dk.fits.contact"
    compileSdk = 35

    defaultConfig {
        applicationId = "dk.fits.contact"
        minSdk = 26
        targetSdk = 35
        versionCode = appVersionCode
        versionName = appVersionName
    }
    signingConfigs {
        if (hasSigning) {
            create("release") {
                storeFile = ksFile
                storePassword = ksPassword
                keyAlias = ksAlias
                keyPassword = ksKeyPassword
            }
        }
    }
    buildTypes {
        release {
            isMinifyEnabled = false
            if (hasSigning) signingConfig = signingConfigs.getByName("release")
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = "17"
    }

    buildFeatures {
        compose = true
    }
}

dependencies {
    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.activity.compose)
    implementation(platform(libs.androidx.compose.bom))
    implementation(libs.androidx.ui)
    implementation(libs.androidx.foundation)
    implementation(libs.androidx.ui.graphics)
    implementation(libs.androidx.ui.tooling.preview)
    implementation(libs.androidx.material3)
    implementation(libs.zxing.core)
}
