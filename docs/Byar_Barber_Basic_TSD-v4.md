
# Technical Specification Document: Byar Barber

## 1. Pendahuluan
Dokumen ini merupakan Technical Specification Document (TSD) untuk aplikasi "Byar Barber", disusun berdasarkan fitur dan alur kerja yang secara eksplisit didemonstrasikan maupun yang secara visual terlihat pada antarmuka (UI) dalam rekaman video tutorial. Spesifikasi ini mencakup fungsionalitas yang ada dan tidak mencakup asumsi fitur di luar yang ditampilkan.

## 2. Gambaran Umum Sistem
Aplikasi "Byar Barber" adalah sistem Point of Sale (POS) berbasis Android (mendukung OS 14+ versi 64-bit) yang dirancang untuk mengelola operasional kasir secara mandiri. Fitur utama mencakup manajemen produk, pemrosesan transaksi dengan dukungan *barcode scanner* kamera, pencetakan struk via printer thermal Bluetooth, manajemen pengeluaran, serta pelaporan data yang dapat diekspor ke Excel. Aplikasi memiliki dukungan *offline* dengan mekanisme pencadangan (*backup*) data secara manual.

## 3. Spesifikasi Fitur Utama

### 3.1. Instalasi, Akses, dan Otentikasi
- **Instalasi & Lisensi:** Menggunakan link unduhan eksternal via email dan otentikasi menggunakan kombinasi *Serial Number* dan *Password*. Terdapat fallback link 64-bit untuk perangkat Android terbaru.
- **Dapatkan Lisensi:** Terdapat menu tombol "Dapatkan Serial Number Disini" untuk pendaftaran/pembelian bagi pengguna baru.
- **Login & Profil:** Login menggunakan *Serial Number*. Pengguna dapat mengedit nama, email, nomor HP, serta foto profil pengguna.
- **Manajemen Sesi:** Terdapat opsi *checkbox* "Remember" pada layar login untuk menyimpan sesi pengguna.
- **Pemulihan Kredensial:** Terdapat tautan "Forget Password" pada layar login.
- **Akses Bantuan Tambahan:** Tersedia ikon jalan pintas "Tutorial" di pojok kanan bawah layar login.
- **Keamanan:** Fasilitas untuk mengubah *Password* dari dalam aplikasi (membutuhkan koneksi internet).
- **Perizinan (Permissions):** Memerlukan akses ke Kamera (untuk barcode), Penyimpanan/Media (untuk produk/logo), Lokasi, dan Perangkat di Sekitar (untuk Bluetooth Printer).

### 3.2. Pengaturan Toko dan Pencetakan
- **Profil Toko:** Konfigurasi logo toko, nama toko, alamat, dan pesan *footer* (pesan di bagian bawah struk).
- **Koneksi Printer Thermal:** Mendukung koneksi via Bluetooth ke printer thermal. Memiliki fungsi "Print Test" untuk memverifikasi koneksi.
- **Pengaturan Perangkat Kasir (Peripherals):**
  - Opsi aktivasi pembukaan laci kasir (*Cashdrawer*).
  - Opsi *Printer AutoCut* untuk memotong kertas otomatis (opsi ini dapat dimatikan untuk menghemat kertas jika hasil cetakan terlalu panjang).
- **Template Struk:** Pengaturan ukuran kertas (58 mm dan 80 mm) dan pilihan *layout* template struk (Template 1 untuk semua ukuran, Template 2 eksklusif untuk 80 mm).

### 3.3. Manajemen Data (Backup & Restore)
- **Backup Data:** Fasilitas pencadangan pangkalan data (format file *.barberdb*). File dapat dibagikan/disimpan ke penyimpanan eksternal atau *cloud* (seperti Google Drive).
- **Histori Backup:** Daftar riwayat pencadangan untuk memudahkan pengelolaan (opsi *share*, hapus, dan *restore*).
- **Restore Data:** Pemulihan data aplikasi menggunakan file backup yang telah dibuat sebelumnya.

### 3.4. Manajemen Inventaris (Kelola Produk)
- **Kategori Produk:** Fitur untuk menambah, mengedit, dan menghapus kategori.
- **Data Produk:** Menambah produk dengan detail: foto (galeri/kamera), nama, *barcode/QR code*, satuan ukuran (pcs, kg, dll), harga jual, dan kategori.
- **Pemindai & Pembuat Barcode:**
  - Mendukung pemindaian barcode fisik melalui kamera perangkat.
  - Jika produk tidak memiliki barcode, sistem dapat men-*generate* kode barcode unik yang dapat langsung dicetak (*Cetak Barcode*) menggunakan printer thermal untuk ditempel pada barang.
- **Navigasi & Pencarian:** Pengurutan (sortir) daftar produk berdasarkan nama, serta tersedianya kolom pencarian (*search bar*) untuk menemukan produk atau kategori secara spesifik.

### 3.5. Transaksi Kasir
- **Akses Kasir Cepat:** Terdapat panel tombol *shortcut* "Transaksi" berukuran besar di bagian bawah beranda utama aplikasi.
- **Proses Pesanan:** 
  - Penambahan produk ke keranjang melalui pemilihan manual dari katalog atau melalui *scan barcode* menggunakan mode beruntun (*burst mode*) via kamera perangkat.
  - Opsi modifikasi kuantitas pesanan.
- **Checkout & Diskon:**
  - Penambahan nominal diskon keseluruhan (dalam satuan Rupiah).
  - Sistem *Checklist* "Langsung bayar" untuk membedakan antara transaksi lunas dan transaksi yang masih tertunda/berhutang (DP).
- **Pembayaran:**
  - Konfirmasi pembayaran dengan input nominal uang yang diserahkan. Sistem menghitung kembalian atau sisa hutang secara otomatis.
  - Input nama kustomer (opsional).
  - Pilihan modifikasi/edit tanggal transaksi.
- **Penyelesaian:** Cetak struk fisik atau bagikan struk digital berupa gambar (*share*) melalui aplikasi pihak ketiga.

### 3.6. Riwayat Transaksi
- **Filter Status:** Kategorisasi transaksi berdasarkan tab: "Selesai", "Belum Bayar" (untuk DP/Hutang), dan "Di Batalkan".
- **Filter Pengurutan (Sorting):** Fasilitas untuk mengurutkan daftar berdasarkan parameter: "Nama A-Z", "Nama Z-A", "Tanggal Terlama", dan "Tanggal Terbaru".
- **Detail & Tindakan:**
  - Melihat detail order dan mencetak ulang struk atau membagikan ulang struk digital.
  - Opsi *Edit Order*.
  - Opsi Pelunasan (pembayaran sisa tagihan untuk transaksi yang belum lunas/kurang bayar).
  - Membatalkan transaksi (memindahkan ke tab "Di Batalkan", mengembalikan stok).
  - Hapus permanen transaksi tunggal atau massal (berdasarkan rentang tanggal).
- **Navigasi:** Fitur pencarian (*search bar*) berdasarkan nama atau nomor nota.

### 3.7. Manajemen Pengeluaran
- Pencatatan biaya operasional toko dengan input: nama pengeluaran, catatan, nominal, dan tanggal pengeluaran. 
- Fasilitas sortir data pengeluaran berdasarkan nama atau tanggal. Tersedia juga fitur pencarian (*search bar*).

### 3.8. Pelaporan & Dasbor
Sistem menyediakan antarmuka dasbor dan modul pelaporan komprehensif:
- **Dasbor Real-Time:** Menampilkan *widget* "Total Penjualan Hari ini" pada halaman muka (beranda) aplikasi.
- **Modul Laporan:** Sistem menyediakan filter rentang waktu (tanggal awal & akhir), serta fitur sortir lanjutan (berdasarkan nama dan tanggal).
  - **Laporan Transaksi:** Ringkasan total harga, total bayar, dan rincian transaksi individu. Menampilkan *Grand Total* penjualan dan jumlah transaksi.
  - **Laporan Produk:** Rincian produk terjual beserta kuantitas (*pcs/unit*).
  - **Laporan Kategori:** Rincian kuantitas produk terjual yang dikelompokkan berdasarkan kategori.
  - **Laporan Pengeluaran:** Rekapitulasi pencatatan pengeluaran.
  - **Ekspor ke Excel:** Fungsi untuk menghasilkan (*generate*) dan menyimpan file laporan berformat `.xlsx` yang berisi detail transaksi dan pengeluaran. File Excel dapat langsung dibuka atau dibagikan.

### 3.9. Pembaruan Aplikasi (Update)
- **Menu Versi:** Melihat versi aplikasi saat ini dan riwayat log pembaruan (*changelog*).
- **In-App Update:** Tombol "Update Sekarang" untuk mengunduh dan menginstal paket pembaruan (*.apk*) secara langsung dari dalam aplikasi (termasuk opsi *link* alternatif untuk versi 64-bit).

### 3.10. Menu Tambahan Terlihat
- **Usaha Saya:** Terletak pada navigasi samping (*sidebar*), menu ini terpisah dari menu Pengaturan utama.
- **Kelola Produk:** Terdapat jalan pintas "Kelola Produk" di sidebar.
- **Laporan Bug:** Terdapat ikon "Laporan Bug" yang terlihat secara sekilas di menu saat memilih file di galeri (bukan dari menu utama, tetapi terlihat sebagai opsi pelaporan tambahan).
- **Keluar Sesi (Logout):** Tersedia tombol "Logout" di bagian terbawah daftar navigasi *sidebar*.

---
*Catatan TSD: Spesifikasi ini diturunkan sepenuhnya dari alur demonstrasi visual dan elemen UI eksplisit/implisit Byar Barber.*
