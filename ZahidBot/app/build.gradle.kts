plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("com.chaquo.python")
}

android {
    namespace = "com.zahid.bot"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.zahid.bot"
        minSdk = 26
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"

        ndk {
            // معظم الهواتف arm64؛ x86_64 للمحاكي. اضف "armeabi-v7a" للهواتف القديمة (32 بت).
            abiFilters += listOf("arm64-v8a", "x86_64")
        }
    }

    buildTypes {
        release { isMinifyEnabled = false }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions { jvmTarget = "17" }
}

chaquopy {
    defaultConfig {
        version = "3.11"
        pip {
            // pyrogram يسحب pyaes و pysocks تلقائياً
            install("pyrogram")
            install("redis")
            install("fakeredis")
            install("telegraph")
            install("yt-dlp")
            install("youtube-search-python")
            install("httpx<0.28")          // youtube-search-python يتعطل مع httpx >= 0.28
            install("Pillow")
            install("requests")
            install("beautifulsoup4")
            install("pytz")
            install("pyfiglet")
            install("aiohttp")
            install("URLExtract")
            install("qrcode")
            install("emoji")
            install("cowpy")
            install("speedtest-cli")
            install("prettytable")
            install("geopy")
            install("gTTS")
            install("python-barcode")
            install("pySmartDL")
            install("cloudscraper")
            install("psutil")
            // اذا فشل Gradle بسبب حزمة (لا يوجد لها wheel لأندرويد) احذف سطرها؛
            // الاوامر المعتمدة عليها تختفي من القائمة تلقائياً.
        }
    }
}

dependencies {
    implementation("androidx.core:core-ktx:1.13.1")
    implementation("androidx.appcompat:appcompat:1.7.0")
    implementation("com.google.android.material:material:1.12.0")
    implementation("androidx.security:security-crypto:1.1.0-alpha06")
}
