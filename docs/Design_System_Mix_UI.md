# BYAR BARBER — Design System Mix UI (Flutter Web PWA)

**Sinkronisasi dokumentasi:** 20 Oktober 2026  
**Sasaran:** Realistic UX Product Demo Flutter Web PWA  
**Dependency yang diverifikasi:** `mix` versi **2.2.2** pada pub.dev; Flutter >= **3.44.0**, Dart >= **3.12.0** (sesuai prasyarat paket yang dipublikasikan).  
**Status contoh:** rujukan implementasi untuk Codex; **belum diuji compile di proyek BYAR BARBER**.

Dokumen ini memperbarui **API teknis Mix** tanpa mengubah keputusan visual pada design system semula. Implementasi menggunakan `package:mix/mix.dart`, bukan nama paket `flutter_mix`. Gunakan versi kompatibel yang benar-benar di-resolve oleh `flutter pub get`; verifikasi lagi API pada versi terpilih sebelum build.

## 1. Identitas dan desain yang tetap dipertahankan

- **Brand aplikasi:** BYAR BARBER.
- **Estetika:** minimalis, zero-elevation (tanpa bayangan dekoratif), bidang putih, garis tepi tipis, hierarki visual jelas.
- **Warna utama:** hitam `#000000`.
- **Scaffold/background:** `#F8F9FA`.
- **Surface/card:** `#FFFFFF`.
- **Border:** `#E2E8F0` (padanan grey.shade200 yang dahulu digunakan).
- **Teks utama:** `#0F172A` (hitam tetap untuk judul/CTA sebagaimana rancangan asli).
- **Teks sekunder:** `#64748B`.
- **Sukses:** nuansa emerald muda untuk latar, emerald tua untuk teks.
- **Typeface pilihan lama:** Plus Jakarta Sans **atau** Inter; aset dan lisensi font harus disiapkan bila dipakai. Jangan menganggap font terpasang otomatis.
- **H1:** 32 logical px, w700, letterSpacing -1.0.
- **H2:** 18–20 logical px, w600/w700.
- **Body:** 14 logical px, w400/w500.
- **Label:** 12 logical px, w400.
- **Radius card:** 16; tombol utama: 12; tombol outline: 8; input: 12; badge pill: 100.
- **Padding:** card 20; tombol utama horizontal 24 vertikal 16; outline horizontal 16 vertikal 12; input horizontal 16 vertikal 14; halaman utama 24 apabila ruang cukup.

Angka di atas merupakan **keputusan desain dari dokumen awal**, bukan ketentuan Flutter atau Mix.

## 2. Integrasi teknis Mix 2.x

Instalasi melalui `flutter pub add mix` dan impor:

```dart
import 'package:flutter/material.dart';
import 'package:mix/mix.dart';
```

Gunakan `BoxStyler` untuk `Box`, `TextStyler` untuk `StyledText`, dan `PressableBox` untuk area interaktif apabila sesuai API terpasang. Gaya direpresentasikan melalui chain bertipe, bukan `Style(bg.white(), rounded(...))` dari contoh lama.

### Contoh token nilai warna yang konsisten

```dart
abstract final class ByarColors {
  static const primary = Color(0xFF000000);
  static const background = Color(0xFFF8F9FA);
  static const surface = Color(0xFFFFFFFF);
  static const border = Color(0xFFE2E8F0);
  static const textPrimary = Color(0xFF0F172A);
  static const textSecondary = Color(0xFF64748B);
  static const successBackground = Color(0xFFECFDF5);
  static const successText = Color(0xFF047857);
}
```

Nilai emerald eksplisit di atas adalah representasi teknis dari maksud emerald-light/emerald-dark dalam sumber; konfirmasi tampilan di browser saat implementasi. Mix juga mendukung `ColorToken`, `SpaceToken`, dan `MixScope` untuk theming terpusat. Gunakan itu jika sesuai implementasi dan versi Mix aktual; nilai brand tidak boleh berubah.

## 3. Definisi dasar styler (API terkini)

### A. Surface / Card

```dart
final surfaceStyle = BoxStyler()
    .color(ByarColors.surface)
    .borderRadius(.circular(16))
    .border(.color(ByarColors.border).width(1).style(.solid))
    .padding(.all(20));
```

### B. Tombol utama — Transaksi Baru

```dart
final primaryButtonStyle = BoxStyler()
    .color(ByarColors.primary)
    .borderRadius(.circular(12))
    .padding(.horizontal(24).vertical(16))
    .onHovered(.color(const Color(0xFF171717)))
    .onPressed(.color(const Color(0xFF262626)));

final primaryButtonLabel = TextStyler()
    .color(Colors.white)
    .fontSize(16)
    .fontWeight(.bold);
```

Render dengan `PressableBox` dan `StyledText`; gunakan callback aksi nyata. Perilaku hover dan pressed adalah **state variants** Mix, bukan fungsi `onPress(bg(...))`. Verifikasi signature `PressableBox` pada versi dependency yang di-resolve.

### C. Tombol sekunder/outline

```dart
final outlineButtonStyle = BoxStyler()
    .color(Colors.transparent)
    .borderRadius(.circular(8))
    .border(.color(const Color(0xFFD1D5DB)).width(1).style(.solid))
    .padding(.horizontal(16).vertical(12))
    .onHovered(.color(const Color(0xFFF9FAFB)));
```

### D. Kontainer input

```dart
final inputContainerStyle = BoxStyler()
    .color(ByarColors.surface)
    .borderRadius(.circular(12))
    .border(.color(ByarColors.border).width(1).style(.solid))
    .padding(.horizontal(16).vertical(14))
    .onFocused(.border(.color(ByarColors.primary).width(1.5).style(.solid)));
```

**Catatan:** Interaksi form, focus handling, keyboard, validasi dan semantics tetap memerlukan kontrol input Flutter yang benar; border fokus Mix tidak menggantikan `TextField`, `Form`, atau pengelolaan `FocusNode`.

### E. Badge status selesai

```dart
final successBadgeStyle = BoxStyler()
    .color(ByarColors.successBackground)
    .borderRadius(.circular(100))
    .padding(.horizontal(12).vertical(6));

final successBadgeTextStyle = TextStyler()
    .color(ByarColors.successText)
    .fontSize(12)
    .fontWeight(.w600);
```

## 4. Komposisi widget dan tata letak

- Pakai `Box`, `StyledText`, `PressableBox` serta layout `RowBox`/`ColumnBox`/`FlexBox` ketika memang didukung versi Mix yang terpasang.
- Flutter `Row`, `Column`, `Expanded`, `Form`, `TextField`, `MediaQuery`, `LayoutBuilder`, dan elemen Material lainnya **tetap dapat digunakan**. Mix adalah sistem styling, bukan larangan terhadap widget Flutter.
- Gunakan gap/spacing yang konsisten. Jangan mengandalkan sintaks lama `gap(16)` tanpa memeriksa versi API.
- Padding halaman dasar 24 logical px pada viewport yang memadai; hindari overflow di layar mobile.
- Responsivitas dapat memakai `onMobile`, `onTablet`, `onDesktop`, `onBreakpoint` atau constraint-based style sesuai kebutuhan layout yang benar-benar ditentukan oleh implementasi.
- Hover harus tetap fungsional pada desktop; interaksi utama juga wajib dapat dipakai melalui sentuhan dan keyboard.

## 5. Contoh render ringkas

```dart
Box(
  style: surfaceStyle,
  child: Column(
    crossAxisAlignment: CrossAxisAlignment.start,
    children: [
      StyledText(
        'Pendapatan Hari Ini',
        style: TextStyler()
            .color(ByarColors.textSecondary)
            .fontSize(14),
      ),
      const SizedBox(height: 8),
      StyledText(
        'Rp 2.450.000',
        style: TextStyler()
            .color(ByarColors.textPrimary)
            .fontSize(32)
            .fontWeight(.bold)
            .letterSpacing(-1.0),
      ),
    ],
  ),
)
```

Nilai `Rp 2.450.000` hanya contoh tampilan dari dokumen lama, **bukan sumber laporan penjualan atau data transaksi nyata**. UI produk harus memakai state demo terpadu sebagaimana TSD.

## 6. Sinkronisasi Flutter Web/PWA

- Validasi menggunakan Flutter dan Dart yang memenuhi batas versi paket Mix terpilih.
- `flutter build web --release` menghasilkan output pada `build/web`.
- Di GitHub Pages, pastikan `--base-href` sesuai path repository agar asset termuat.
- PWA installability perlu `manifest.json`, ikon, metadata, HTTPS, serta pengujian browser yang sesungguhnya.
- Flutter modern **tidak lagi mengelola caching service worker otomatis**. Jika demo memerlukan offline, implementasikan dan uji service worker khusus; jangan mengklaim offline berdasarkan hasil build saja.
- Untuk GitHub Pages statis, cek strategi routing agar deep-link/refresh tidak menghasilkan 404.
- Fitur native Android (misalnya printer Bluetooth, APK updater) tidak otomatis tersedia sebagai kemampuan browser; pisahkan simulasi demo dari integrasi hardware nyata.
- Uji resize desktop/mobile, fokus keyboard, scroll, overflow, dan perilaku transaksi di browser.

## 7. Verifikasi wajib oleh Codex Cloud

1. Konfirmasi versi Flutter/Dart tersedia dan versi `mix` yang dapat di-resolve.
2. Pastikan contoh API sesuai API dependency terkunci di `pubspec.lock`; jangan menyebut contoh dokumentasi sebagai **compile-verified** sebelum diuji.
3. Jalankan `flutter pub get`, `dart format`, `flutter analyze`, `flutter test`, `flutter build web --release`.
4. Periksa hasil build di browser dan catat keterbatasan test otomatis/visual yang tidak dapat dijalankan.
5. Jangan mengganti token desain atau menambah fitur bisnis di luar TSD.

## 8. Rujukan teknis (diakses 20 Oktober 2026)

- Paket Mix / persyaratan terkini: https://pub.dev/packages/mix (terpantau versi 2.2.2).
- Dokumentasi Mix: https://www.fluttermix.com/documentation/mix/guides/styling
- Komponen Mix: https://www.fluttermix.com/documentation/mix/widgets/stylewidgets
- Pola `PressableBox`: https://www.fluttermix.com/documentation/mix/guides/common-patterns
- Flutter Web deployment: https://docs.flutter.dev/deployment/web
- Flutter Web FAQ / service worker: https://docs.flutter.dev/platform-integration/web/faq

**Batas audit:** Ini sinkronisasi spesifikasi dan contoh API terhadap dokumentasi publik, bukan hasil build Flutter. Tidak ada source code aplikasi yang dimodifikasi.
