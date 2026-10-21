# BYAR BARBER — UX Storyboard

> **Versi:** v0.0.2 | **Sumber otoritatif:** `docs/Byar_Barber_Basic_TSD-v4.md` | **Turunan:** `docs/LOFI_SCREEN_SPEC.md`

## Aturan derivasi

- Setiap `SB-*` dipetakan ke subbab TSD; urutan langkah hanya merepresentasikan aksi yang tersurat atau diperlukan untuk mengakses fitur yang disebutkan.
- Hasil yang tidak dispesifikasikan secara eksplisit diberi penanda **belum dirinci TSD**, bukan dianggap keputusan produk.
- Interaksi hardware, tautan eksternal, autentikasi server, APK, dan share bukan jaminan dukungan Flutter Web. Saat demo boleh disimulasikan dengan penanda jelas; jangan klaim integrasi nyata.
- Rute/ID layar adalah artefak dokumentasi, bukan kontrak URL atau implementasi.

## Daftar storyboard

### SB-01 — Masuk dengan Serial Number dan Password
- **TSD:** §3.1
- **Tujuan:** Masuk dengan Serial Number dan Password
- **Kondisi awal:** Layar login
- **Aksi pengguna:** Isi kredensial dan pilih masuk
- **Respons sistem:** Permintaan autentikasi; hasil validasi server tidak dirinci TSD
- **State/navigasi akhir:** Beranda bila autentikasi berhasil
- **Lo-Fi terkait:** SC-01, SC-05

### SB-02 — Mempertahankan sesi
- **TSD:** §3.1
- **Tujuan:** Mempertahankan sesi
- **Kondisi awal:** Layar login
- **Aksi pengguna:** Centang Remember
- **Respons sistem:** Preferensi remember tersimpan; mekanisme sesi tidak dirinci
- **State/navigasi akhir:** Login / Beranda
- **Lo-Fi terkait:** SC-01

### SB-03 — Memulihkan akses
- **TSD:** §3.1
- **Tujuan:** Memulihkan akses
- **Kondisi awal:** Layar login
- **Aksi pengguna:** Pilih Forget Password
- **Respons sistem:** Membuka alur pemulihan; langkah lanjutan tidak dirinci
- **State/navigasi akhir:** Pemulihan
- **Lo-Fi terkait:** SC-02

### SB-04 — Memperoleh serial number
- **TSD:** §3.1
- **Tujuan:** Memperoleh serial number
- **Kondisi awal:** Layar login
- **Aksi pengguna:** Pilih Dapatkan Serial Number Disini
- **Respons sistem:** Membuka pendaftaran/pembelian; tujuan tautan tidak dirinci
- **State/navigasi akhir:** Lisensi
- **Lo-Fi terkait:** SC-03

### SB-05 — Mengakses tutorial
- **TSD:** §3.1
- **Tujuan:** Mengakses tutorial
- **Kondisi awal:** Layar login
- **Aksi pengguna:** Tekan ikon Tutorial
- **Respons sistem:** Membuka akses tutorial; konten tidak dirinci
- **State/navigasi akhir:** Tutorial
- **Lo-Fi terkait:** SC-04

### SB-06 — Memperbarui profil dan password
- **TSD:** §3.1
- **Tujuan:** Memperbarui profil dan password
- **Kondisi awal:** Sesi aktif
- **Aksi pengguna:** Buka profil, edit nama/email/HP/foto; akses ubah password
- **Respons sistem:** Perubahan profil; ubah password membutuhkan internet
- **State/navigasi akhir:** Profil
- **Lo-Fi terkait:** SC-06

### SB-07 — Keluar dari aplikasi
- **TSD:** §3.10
- **Tujuan:** Keluar dari aplikasi
- **Kondisi awal:** Sesi aktif, sidebar
- **Aksi pengguna:** Pilih Logout
- **Respons sistem:** Sesi keluar
- **State/navigasi akhir:** Login
- **Lo-Fi terkait:** SC-07, SC-01

### SB-08 — Melihat omzet dan mulai transaksi
- **TSD:** §3.8, 3.5
- **Tujuan:** Melihat omzet dan mulai transaksi
- **Kondisi awal:** Beranda
- **Aksi pengguna:** Lihat Total Penjualan Hari Ini lalu tekan shortcut Transaksi
- **Respons sistem:** Menampilkan alur kasir
- **State/navigasi akhir:** Transaksi
- **Lo-Fi terkait:** SC-05, SC-12

### SB-09 — Mengelola kategori
- **TSD:** §3.4
- **Tujuan:** Mengelola kategori
- **Kondisi awal:** Kelola Produk
- **Aksi pengguna:** Tambahkan / edit / hapus kategori
- **Respons sistem:** Daftar kategori berubah
- **State/navigasi akhir:** Kategori
- **Lo-Fi terkait:** SC-08, SC-09

### SB-10 — Mencari dan mengurutkan produk
- **TSD:** §3.4
- **Tujuan:** Mencari dan mengurutkan produk
- **Kondisi awal:** Kelola Produk
- **Aksi pengguna:** Masukkan kata kunci atau urutkan nama
- **Respons sistem:** Daftar terfilter/terurut
- **State/navigasi akhir:** Daftar produk
- **Lo-Fi terkait:** SC-08

### SB-11 — Membuat atau mengubah produk
- **TSD:** §3.4
- **Tujuan:** Membuat atau mengubah produk
- **Kondisi awal:** Kelola Produk
- **Aksi pengguna:** Isi foto, nama, barcode/QR, satuan, harga, kategori; simpan
- **Respons sistem:** Daftar produk diperbarui
- **State/navigasi akhir:** Daftar produk
- **Lo-Fi terkait:** SC-10, SC-08

### SB-12 — Memindai / membuat barcode
- **TSD:** §3.4
- **Tujuan:** Memindai / membuat barcode
- **Kondisi awal:** Kelola Produk
- **Aksi pengguna:** Aktifkan scan kamera atau generate dan cetak kode
- **Respons sistem:** Kode ditemukan/dihasilkan; hardware bergantung platform
- **State/navigasi akhir:** Barcode
- **Lo-Fi terkait:** SC-11

### SB-13 — Menambahkan produk ke keranjang
- **TSD:** §3.5
- **Tujuan:** Menambahkan produk ke keranjang
- **Kondisi awal:** Transaksi
- **Aksi pengguna:** Pilih produk katalog atau scan beruntun
- **Respons sistem:** Baris item muncul dalam keranjang
- **State/navigasi akhir:** Keranjang
- **Lo-Fi terkait:** SC-12, SC-13

### SB-14 — Mengubah jumlah item
- **TSD:** §3.5
- **Tujuan:** Mengubah jumlah item
- **Kondisi awal:** Keranjang berisi produk
- **Aksi pengguna:** Ubah kuantitas
- **Respons sistem:** Jumlah dan subtotal diperbarui
- **State/navigasi akhir:** Keranjang
- **Lo-Fi terkait:** SC-13

### SB-15 — Menerapkan diskon dan memilih jenis bayar
- **TSD:** §3.5
- **Tujuan:** Menerapkan diskon dan memilih jenis bayar
- **Kondisi awal:** Keranjang
- **Aksi pengguna:** Isi diskon rupiah dan checklist Langsung bayar
- **Respons sistem:** Nilai pembayaran dan mode lunas/tertunda disiapkan
- **State/navigasi akhir:** Checkout
- **Lo-Fi terkait:** SC-14

### SB-16 — Menyelesaikan pembayaran
- **TSD:** §3.5
- **Tujuan:** Menyelesaikan pembayaran
- **Kondisi awal:** Checkout
- **Aksi pengguna:** Masukkan nominal uang, opsional nama pelanggan, edit tanggal, konfirmasi
- **Respons sistem:** Kembalian atau sisa hutang dihitung
- **State/navigasi akhir:** Hasil transaksi
- **Lo-Fi terkait:** SC-15, SC-16

### SB-17 — Mencetak atau membagikan struk
- **TSD:** §3.5
- **Tujuan:** Mencetak atau membagikan struk
- **Kondisi awal:** Transaksi selesai
- **Aksi pengguna:** Pilih cetak struk atau share gambar
- **Respons sistem:** Struk disiapkan; printer/share eksternal platform-dependent
- **State/navigasi akhir:** Struk
- **Lo-Fi terkait:** SC-17

### SB-18 — Menemukan transaksi
- **TSD:** §3.6
- **Tujuan:** Menemukan transaksi
- **Kondisi awal:** Riwayat
- **Aksi pengguna:** Pilih tab status, sortir A-Z/Z-A/terlama/terbaru, cari nama/nota
- **Respons sistem:** Hasil riwayat disaring
- **State/navigasi akhir:** Riwayat
- **Lo-Fi terkait:** SC-18

### SB-19 — Melihat/mengedit pesanan dan cetak ulang
- **TSD:** §3.6
- **Tujuan:** Melihat/mengedit pesanan dan cetak ulang
- **Kondisi awal:** Riwayat
- **Aksi pengguna:** Buka detail lalu pilih Edit Order / cetak / share
- **Respons sistem:** Detail dapat ditinjau; perubahan order sesuai tindakan
- **State/navigasi akhir:** Detail order
- **Lo-Fi terkait:** SC-19, SC-20, SC-17

### SB-20 — Melunasi sisa tagihan
- **TSD:** §3.6
- **Tujuan:** Melunasi sisa tagihan
- **Kondisi awal:** Transaksi Belum Bayar
- **Aksi pengguna:** Pilih Pelunasan, masukkan nominal pembayaran
- **Respons sistem:** Sisa tagihan diperbarui; status sesuai hasil pelunasan
- **State/navigasi akhir:** Detail order
- **Lo-Fi terkait:** SC-21, SC-19

### SB-21 — Membatalkan transaksi
- **TSD:** §3.6
- **Tujuan:** Membatalkan transaksi
- **Kondisi awal:** Detail transaksi
- **Aksi pengguna:** Pilih batalkan
- **Respons sistem:** Status Di Batalkan; stok dikembalikan
- **State/navigasi akhir:** Riwayat
- **Lo-Fi terkait:** SC-19, SC-18

### SB-22 — Menghapus transaksi tunggal/massal
- **TSD:** §3.6
- **Tujuan:** Menghapus transaksi tunggal/massal
- **Kondisi awal:** Riwayat
- **Aksi pengguna:** Pilih hapus tunggal atau hapus berdasarkan rentang tanggal
- **Respons sistem:** Riwayat terkait dihapus permanen
- **State/navigasi akhir:** Riwayat
- **Lo-Fi terkait:** SC-18, SC-22

### SB-23 — Mencatat pengeluaran
- **TSD:** §3.7
- **Tujuan:** Mencatat pengeluaran
- **Kondisi awal:** Pengeluaran
- **Aksi pengguna:** Isi nama, catatan, nominal, tanggal
- **Respons sistem:** Catatan pengeluaran ditambahkan
- **State/navigasi akhir:** Daftar pengeluaran
- **Lo-Fi terkait:** SC-23, SC-24

### SB-24 — Menemukan pengeluaran
- **TSD:** §3.7
- **Tujuan:** Menemukan pengeluaran
- **Kondisi awal:** Pengeluaran
- **Aksi pengguna:** Cari nama atau sortir nama/tanggal
- **Respons sistem:** Daftar pengeluaran diperbarui
- **State/navigasi akhir:** Daftar pengeluaran
- **Lo-Fi terkait:** SC-23

### SB-25 — Melihat laporan transaksi
- **TSD:** §3.8
- **Tujuan:** Melihat laporan transaksi
- **Kondisi awal:** Menu laporan
- **Aksi pengguna:** Pilih rentang tanggal, sortir, buka laporan transaksi
- **Respons sistem:** Total harga, total bayar, grand total dan jumlah transaksi ditampilkan
- **State/navigasi akhir:** Laporan transaksi
- **Lo-Fi terkait:** SC-25, SC-26

### SB-26 — Melihat laporan produk/kategori
- **TSD:** §3.8
- **Tujuan:** Melihat laporan produk/kategori
- **Kondisi awal:** Menu laporan
- **Aksi pengguna:** Pilih laporan produk atau kategori
- **Respons sistem:** Kuantitas terjual per produk/kategori ditampilkan
- **State/navigasi akhir:** Laporan produk/kategori
- **Lo-Fi terkait:** SC-25, SC-27

### SB-27 — Melihat laporan pengeluaran
- **TSD:** §3.8
- **Tujuan:** Melihat laporan pengeluaran
- **Kondisi awal:** Menu laporan
- **Aksi pengguna:** Pilih laporan pengeluaran
- **Respons sistem:** Rekap biaya ditampilkan
- **State/navigasi akhir:** Laporan pengeluaran
- **Lo-Fi terkait:** SC-25, SC-28

### SB-28 — Mengekspor Excel
- **TSD:** §3.8
- **Tujuan:** Mengekspor Excel
- **Kondisi awal:** Laporan
- **Aksi pengguna:** Pilih ekspor Excel
- **Respons sistem:** File .xlsx dihasilkan/dibagikan bila browser mendukung
- **State/navigasi akhir:** Laporan
- **Lo-Fi terkait:** SC-25, SC-29

### SB-29 — Memperbarui profil toko
- **TSD:** §3.2
- **Tujuan:** Memperbarui profil toko
- **Kondisi awal:** Pengaturan toko
- **Aksi pengguna:** Ubah logo, nama, alamat, footer
- **Respons sistem:** Pengaturan toko berubah
- **State/navigasi akhir:** Profil toko
- **Lo-Fi terkait:** SC-30

### SB-30 — Mengonfigurasi printer/struk
- **TSD:** §3.2
- **Tujuan:** Mengonfigurasi printer/struk
- **Kondisi awal:** Pengaturan printer
- **Aksi pengguna:** Pilih Bluetooth printer, Print Test, cashdrawer, AutoCut, 58/80 mm, template
- **Respons sistem:** Pengaturan tersimpan; pengujian hardware tergantung platform
- **State/navigasi akhir:** Printer dan template
- **Lo-Fi terkait:** SC-31, SC-32

### SB-31 — Membuat dan mengelola backup
- **TSD:** §3.3
- **Tujuan:** Membuat dan mengelola backup
- **Kondisi awal:** Backup
- **Aksi pengguna:** Buat file .barberdb, lihat histori, bagikan/hapus
- **Respons sistem:** File/histori backup terkelola
- **State/navigasi akhir:** Backup
- **Lo-Fi terkait:** SC-33

### SB-32 — Memulihkan backup
- **TSD:** §3.3
- **Tujuan:** Memulihkan backup
- **Kondisi awal:** Backup
- **Aksi pengguna:** Pilih file backup dan restore
- **Respons sistem:** Data dipulihkan jika format valid; skema file tidak dirinci
- **State/navigasi akhir:** Backup
- **Lo-Fi terkait:** SC-33

### SB-33 — Melihat versi dan opsi update
- **TSD:** §3.9
- **Tujuan:** Melihat versi dan opsi update
- **Kondisi awal:** Menu versi
- **Aksi pengguna:** Buka changelog dan Update Sekarang
- **Respons sistem:** Informasi versi/update APK Android ditampilkan
- **State/navigasi akhir:** Versi aplikasi
- **Lo-Fi terkait:** SC-34

### SB-34 — Membuka Usaha Saya
- **TSD:** §3.10
- **Tujuan:** Membuka Usaha Saya
- **Kondisi awal:** Sidebar
- **Aksi pengguna:** Pilih Usaha Saya
- **Respons sistem:** Menu terbuka; isi rinci tidak ditetapkan oleh TSD
- **State/navigasi akhir:** Usaha Saya
- **Lo-Fi terkait:** SC-07, SC-35

### SB-35 — Akses laporan bug kontekstual
- **TSD:** §3.10
- **Tujuan:** Akses laporan bug kontekstual
- **Kondisi awal:** Pemilih gambar/galeri
- **Aksi pengguna:** Pilih ikon Laporan Bug
- **Respons sistem:** Akses laporan bug kontekstual; alur rinci tidak ditetapkan
- **State/navigasi akhir:** Laporan Bug kontekstual
- **Lo-Fi terkait:** SC-36

### SB-36 — Mengakses perizinan perangkat
- **TSD:** §3.1
- **Tujuan:** Mengakses perizinan perangkat
- **Kondisi awal:** Scan, media, printer
- **Aksi pengguna:** Mulai operasi yang memerlukan izin kamera/media/lokasi/perangkat sekitar
- **Respons sistem:** Prompt izin sesuai kemampuan platform
- **State/navigasi akhir:** Layar pemicu
- **Lo-Fi terkait:** SC-11, SC-10, SC-31

## Coverage dan hal yang belum diputuskan

- **Total storyboard:** 36; mencakup TSD §3.1 sampai §3.10.
- Tidak mengarang urutan detail reset password, proses pembelian lisensi, konten tutorial, isi Usaha Saya, atau laporan bug; TSD tidak merincinya.
- Perangkat Bluetooth, cashdrawer, permission Android, install APK, scan fisik, dan share eksternal memerlukan batas kemampuan browser yang harus ditandai dalam demo.
- Skema file `.barberdb`, metode autentikasi asli, detail edit order, dan aturan bayar parsial tidak ditentukan secara mendalam oleh sumber. Jangan mengasumsikan kompatibilitas atau formula tambahan.
