# BYAR BARBER — Lo-Fi Screen Specification

> **Versi:** v0.0.2 | **Diturunkan dari:** `docs/UX_STORYBOARD.md` | **Kendali fitur:** `docs/Byar_Barber_Basic_TSD-v4.md`

## Batasan dan format

- Lo-Fi adalah **spesifikasi layar tekstual** (hierarki konten dan aksi), bukan file desain visual, bitmap, atau UI Flutter yang sudah dibangun.
- ID `SC-*` adalah unit layar atau panel interaksi konseptual; satu ID tidak wajib satu route Flutter.
- Struktur umum minimal: judul layar, konten utama, kontrol yang benar-benar disebut dalam TSD, feedback state, navigasi/kembali. Tata letak final harus mematuhi `docs/Design_System_Mix_UI.md`.
- Jangan menambahkan fields, metode pembayaran, profil barber, reservasi, stok awal, atau kapabilitas bisnis lain yang tidak dijelaskan di TSD.
- Konten yang sumbernya tidak rinci sengaja diberi label **belum dirinci**.

## Inventory Lo-Fi Screen

### SC-01 — Login
- **Referensi TSD:** §3.1
- **Storyboard:** SB-01, SB-02
- **Wireframe hierarchy (atas → bawah):** Header BYAR BARBER; serial number; password; Remember; Masuk; Forget Password; Dapatkan Serial Number Disini; Tutorial
- **Interaksi/transisi:** Masuk → SC-05; pemulihan → SC-02; lisensi → SC-03; tutorial → SC-04
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-02 — Forget Password
- **Referensi TSD:** §3.1
- **Storyboard:** SB-03
- **Wireframe hierarchy (atas → bawah):** Judul pemulihan; area penjelasan tindakan berikutnya (belum dirinci TSD); kembali
- **Interaksi/transisi:** Kembali → SC-01
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-03 — Dapatkan Serial Number
- **Referensi TSD:** §3.1
- **Storyboard:** SB-04
- **Wireframe hierarchy (atas → bawah):** Judul lisensi; link pendaftaran/pembelian (target belum ditentukan); kembali
- **Interaksi/transisi:** Kembali → SC-01
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-04 — Tutorial
- **Referensi TSD:** §3.1
- **Storyboard:** SB-05
- **Wireframe hierarchy (atas → bawah):** Judul tutorial; area konten belum ditentukan TSD; kembali
- **Interaksi/transisi:** Kembali → SC-01
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-05 — Beranda/Dashboard
- **Referensi TSD:** §3.5, 3.8
- **Storyboard:** SB-01, SB-08
- **Wireframe hierarchy (atas → bawah):** Header; Total Penjualan Hari Ini; akses navigasi; panel shortcut Transaksi besar di bagian bawah
- **Interaksi/transisi:** Transaksi → SC-12; menu → SC-07
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-06 — Profil pengguna
- **Referensi TSD:** §3.1
- **Storyboard:** SB-06
- **Wireframe hierarchy (atas → bawah):** Foto profil; nama; email; nomor HP; edit/simpan; ubah password (membutuhkan internet)
- **Interaksi/transisi:** Simpan → profil; kembali → SC-05
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-07 — Sidebar navigasi
- **Referensi TSD:** §3.10
- **Storyboard:** SB-07, SB-34
- **Wireframe hierarchy (atas → bawah):** Usaha Saya; Kelola Produk; pengaturan dan menu aplikasi yang dijelaskan TSD; Logout di bawah
- **Interaksi/transisi:** Usaha Saya → SC-35; produk → SC-08; Logout → SC-01
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-08 — Daftar produk
- **Referensi TSD:** §3.4
- **Storyboard:** SB-09, SB-10, SB-11
- **Wireframe hierarchy (atas → bawah):** Search; sort nama; daftar produk (foto/nama/harga/kategori); tambah produk; kategori; akses barcode
- **Interaksi/transisi:** Tambah/edit → SC-10; kategori → SC-09; barcode → SC-11
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-09 — Kategori produk
- **Referensi TSD:** §3.4
- **Storyboard:** SB-09
- **Wireframe hierarchy (atas → bawah):** Daftar kategori; tambah; edit; hapus
- **Interaksi/transisi:** Kembali → SC-08
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-10 — Form produk
- **Referensi TSD:** §3.4
- **Storyboard:** SB-11, SB-36
- **Wireframe hierarchy (atas → bawah):** Foto kamera/galeri; nama; barcode/QR; satuan; harga jual; kategori; simpan
- **Interaksi/transisi:** Simpan → SC-08; barcode → SC-11
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-11 — Barcode / pemindaian
- **Referensi TSD:** §3.4, 3.5
- **Storyboard:** SB-12, SB-36
- **Wireframe hierarchy (atas → bawah):** Kontrol scan kamera; kode hasil scan; generate barcode; Cetak Barcode; indikator dukungan demo/perangkat
- **Interaksi/transisi:** Kembali → SC-08 atau SC-12 sesuai konteks
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-12 — Transaksi / katalog kasir
- **Referensi TSD:** §3.5
- **Storyboard:** SB-08, SB-13
- **Wireframe hierarchy (atas → bawah):** Search/pilih produk; akses pemindaian burst; indikator keranjang
- **Interaksi/transisi:** Item → SC-13; scan → SC-11
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-13 — Keranjang transaksi
- **Referensi TSD:** §3.5
- **Storyboard:** SB-13, SB-14
- **Wireframe hierarchy (atas → bawah):** Item; kuantitas dapat diubah; subtotal; aksi lanjut checkout
- **Interaksi/transisi:** Checkout → SC-14
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-14 — Checkout dan diskon
- **Referensi TSD:** §3.5
- **Storyboard:** SB-15
- **Wireframe hierarchy (atas → bawah):** Ringkasan belanja; nominal diskon rupiah; checklist Langsung bayar
- **Interaksi/transisi:** Lanjut → SC-15
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-15 — Pembayaran
- **Referensi TSD:** §3.5
- **Storyboard:** SB-16
- **Wireframe hierarchy (atas → bawah):** Total; nominal uang diterima; kalkulasi kembalian/sisa hutang; nama pelanggan opsional; tanggal transaksi dapat diedit; konfirmasi
- **Interaksi/transisi:** Konfirmasi → SC-16
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-16 — Hasil transaksi
- **Referensi TSD:** §3.5
- **Storyboard:** SB-16
- **Wireframe hierarchy (atas → bawah):** Status transaksi; nominal bayar; kembalian atau sisa hutang; akses struk
- **Interaksi/transisi:** Struk → SC-17
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-17 — Struk
- **Referensi TSD:** §3.2, 3.5, 3.6
- **Storyboard:** SB-17, SB-19
- **Wireframe hierarchy (atas → bawah):** Preview struk; ukuran/template dari pengaturan; cetak; share gambar; informasi dukungan platform
- **Interaksi/transisi:** Kembali → transaksi terkait
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-18 — Riwayat transaksi
- **Referensi TSD:** §3.6
- **Storyboard:** SB-18, SB-21, SB-22
- **Wireframe hierarchy (atas → bawah):** Tab Selesai / Belum Bayar / Di Batalkan; search nama/nomor nota; sort A-Z, Z-A, terlama, terbaru; hapus rentang tanggal
- **Interaksi/transisi:** Detail → SC-19; hapus massal → SC-22
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-19 — Detail transaksi
- **Referensi TSD:** §3.6
- **Storyboard:** SB-19, SB-20, SB-21
- **Wireframe hierarchy (atas → bawah):** Rincian order; status; nominal; edit; pelunasan (jika belum lunas); batalkan; cetak ulang; share; hapus tunggal
- **Interaksi/transisi:** Edit → SC-20; pelunasan → SC-21; struk → SC-17
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-20 — Edit Order
- **Referensi TSD:** §3.6
- **Storyboard:** SB-19
- **Wireframe hierarchy (atas → bawah):** Area edit data pesanan; rincian field/editability belum dirinci TSD; simpan/batal
- **Interaksi/transisi:** Kembali → SC-19
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-21 — Pelunasan
- **Referensi TSD:** §3.6
- **Storyboard:** SB-20
- **Wireframe hierarchy (atas → bawah):** Sisa hutang; nominal pembayaran; konfirmasi; hasil status
- **Interaksi/transisi:** Kembali → SC-19
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-22 — Hapus transaksi berdasar tanggal
- **Referensi TSD:** §3.6
- **Storyboard:** SB-22
- **Wireframe hierarchy (atas → bawah):** Tanggal awal/akhir; tindakan hapus permanen; konfirmasi konsekuensi
- **Interaksi/transisi:** Kembali → SC-18
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-23 — Daftar pengeluaran
- **Referensi TSD:** §3.7
- **Storyboard:** SB-23, SB-24
- **Wireframe hierarchy (atas → bawah):** Daftar pengeluaran; pencarian; sortir nama/tanggal; tambah
- **Interaksi/transisi:** Tambah → SC-24
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-24 — Input pengeluaran
- **Referensi TSD:** §3.7
- **Storyboard:** SB-23
- **Wireframe hierarchy (atas → bawah):** Nama pengeluaran; catatan; nominal; tanggal; simpan
- **Interaksi/transisi:** Simpan → SC-23
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-25 — Menu laporan/filter
- **Referensi TSD:** §3.8
- **Storyboard:** SB-25, SB-26, SB-27, SB-28
- **Wireframe hierarchy (atas → bawah):** Tanggal awal/akhir; sortir nama/tanggal; pilihan laporan transaksi/produk/kategori/pengeluaran; ekspor Excel
- **Interaksi/transisi:** Transaksi → SC-26; produk/kategori → SC-27; pengeluaran → SC-28; ekspor → SC-29
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-26 — Laporan transaksi
- **Referensi TSD:** §3.8
- **Storyboard:** SB-25
- **Wireframe hierarchy (atas → bawah):** Total harga; total bayar; detail transaksi; Grand Total; jumlah transaksi
- **Interaksi/transisi:** Kembali → SC-25
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-27 — Laporan produk dan kategori
- **Referensi TSD:** §3.8
- **Storyboard:** SB-26
- **Wireframe hierarchy (atas → bawah):** Mode produk: jumlah terjual per produk; mode kategori: jumlah terjual per kategori
- **Interaksi/transisi:** Kembali → SC-25
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-28 — Laporan pengeluaran
- **Referensi TSD:** §3.8
- **Storyboard:** SB-27
- **Wireframe hierarchy (atas → bawah):** Rekap pengeluaran berdasarkan filter waktu
- **Interaksi/transisi:** Kembali → SC-25
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-29 — Ekspor Excel
- **Referensi TSD:** §3.8
- **Storyboard:** SB-28
- **Wireframe hierarchy (atas → bawah):** Kontrol ekspor .xlsx; status unduh atau berbagi; batas browser ditandai
- **Interaksi/transisi:** Kembali → SC-25
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-30 — Profil toko
- **Referensi TSD:** §3.2
- **Storyboard:** SB-29
- **Wireframe hierarchy (atas → bawah):** Logo; nama toko; alamat; footer struk; simpan
- **Interaksi/transisi:** Kembali → pengaturan
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-31 — Printer dan periferal
- **Referensi TSD:** §3.2
- **Storyboard:** SB-30, SB-36
- **Wireframe hierarchy (atas → bawah):** Pilih printer Bluetooth; Print Test; Cashdrawer; AutoCut; batasan browser
- **Interaksi/transisi:** Template → SC-32
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-32 — Template struk
- **Referensi TSD:** §3.2
- **Storyboard:** SB-30
- **Wireframe hierarchy (atas → bawah):** Pilihan 58/80 mm; Template 1 untuk semua ukuran; Template 2 hanya 80 mm
- **Interaksi/transisi:** Kembali → SC-31
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-33 — Backup & Restore
- **Referensi TSD:** §3.3
- **Storyboard:** SB-31, SB-32
- **Wireframe hierarchy (atas → bawah):** Buat backup .barberdb; histori; share; hapus; pilih restore; catatan format belum diverifikasi
- **Interaksi/transisi:** Kembali → menu
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-34 — Versi dan update
- **Referensi TSD:** §3.9
- **Storyboard:** SB-33
- **Wireframe hierarchy (atas → bawah):** Nomor versi; changelog; Update Sekarang; opsi APK/64-bit diberi konteks Android
- **Interaksi/transisi:** Kembali → menu
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-35 — Usaha Saya
- **Referensi TSD:** §3.10
- **Storyboard:** SB-34
- **Wireframe hierarchy (atas → bawah):** Judul Usaha Saya; isi belum dirinci di TSD (tidak ditambahkan fitur)
- **Interaksi/transisi:** Kembali → SC-07
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

### SC-36 — Laporan Bug kontekstual
- **Referensi TSD:** §3.10
- **Storyboard:** SB-35
- **Wireframe hierarchy (atas → bawah):** Akses terlihat pada pemilih media; konten dan tujuan laporan belum dirinci
- **Interaksi/transisi:** Kembali → pemilih media
- **State visual yang perlu dipertimbangkan:** idle, input/selection, hasil aksi, atau ketidaktersediaan layanan sesuai kebutuhan alur; pesan detail hanya dapat dipastikan setelah aturan teknis ditetapkan.

## Komposisi Lo-Fi ringkas (contoh bukan keputusan final)

```text
[SC-12 TRANSAKSI]
[Header / akses kembali]
[Cari produk              ] [Scan]
[Katalog produk (list/grid responsif)]
[Ringkasan keranjang / akses keranjang]
```

```text
[SC-15 PEMBAYARAN]
[Ringkasan total]
[Nominal diterima         ]
[Nama pelanggan (opsional)]
[Tanggal transaksi       ]
[Kembalian / Sisa hutang ]
[Konfirmasi pembayaran   ]
```

## Matriks pemeriksaan

- 36 storyboard dipetakan ke 36 spesifikasi layar/panel aktif.
- Pengaturan printer dan APK tetap dicatat sebagai alur Android yang tidak otomatis bekerja di GitHub Pages.
- `.barberdb` adalah nomenklatur ekstensi backup; format biner dan kompatibilitas restore belum ditentukan.
- Tidak ada penetapan layout pixel-perfect di dokumen Lo-Fi ini.
