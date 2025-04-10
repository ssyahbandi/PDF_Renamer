# Renamerged 😊📜✨

Halo, teman-teman! Selamat datang di Renamerged! 🎉 Aplikasi ini adalah solusi praktis untuk kamu yang sering kerepotan mengelola file PDF, terutama dokumen pajak atau transaksi bisnis yang menumpuk. Renamerged (singkatan dari Rename-Merged) dirancang untuk rename dan merge file PDF secara otomatis berdasarkan ID TKU Penjual dan Nama Lawan Transaksi. Dengan Renamerged, dokumenmu akan rapi terorganisir tanpa perlu kerja manual yang melelahkan! 😍

Kini, Renamerged hadir dengan GUI modern yang membuat penggunaan jauh lebih mudah, bahkan untuk kamu yang tidak suka mengetik di terminal! 🖥️ Yuk, simak lebih lanjut apa yang bisa Renamerged lakukan untukmu! 🌟

## Apa Itu Renamerged? 🤔💡

Renamerged adalah alat sederhana namun powerful yang dibuat untuk membantu mengelola file PDF dengan cara yang efisien. Bayangkan, kamu punya ratusan PDF dengan ID TKU Penjual dan Nama Partner yang berbeda-beda. Jika harus rename satu per satu, bisa memakan waktu seharian! 😅 Renamerged hadir untuk membantu:  
- Rename File PDF Otomatis 📝: Aplikasi ini membaca isi PDF, mengambil ID TKU Penjual (22 digit) dan Nama Lawan Transaksi, lalu mengganti nama file PDF sesuai Nama Partner.  
- Merge PDF yang Sama 📚: Jika ada beberapa PDF dengan ID TKU Penjual dan Nama Partner yang sama, Renamerged akan menggabungkan semua file tersebut menjadi satu PDF yang rapi.  
- Organisasi File 🗂️: Semua hasil disimpan di folder ProcessedPDFs (atau folder yang kamu pilih), diorganisir berdasarkan ID TKU Penjual, sehingga mudah dicari kapan saja.  

Aplikasi ini sangat cocok untuk kamu yang sering menangani dokumen pajak, transaksi bisnis, atau file PDF yang perlu dirapikan. Renamerged akan membuat hidupmu lebih mudah tanpa harus bekerja manual lagi! 🚀

## Fitur Unggulan 🌟

Renamerged dilengkapi dengan fitur-fitur keren yang membuatnya unggul:  
- GUI Modern 🖥️: Antarmuka grafis yang intuitif dengan desain futuristik, tombol rounded, dan progress bar untuk memantau proses.  
- Pratinjau File PDF 📄: Lihat daftar file PDF yang akan diproses sebelum memulai, sehingga kamu bisa memastikan file yang tepat.  
- Rename PDF Otomatis 📂: Rename file PDF berdasarkan ID TKU Penjual dan Nama Lawan Transaksi tanpa perlu membuka file satu per satu.  
- Merge PDF yang Sama 📦: Gabungkan semua PDF dengan ID TKU Penjual dan Nama Partner yang sama menjadi satu file rapi. Hemat ruang, hemat waktu!  
- Organisasi File 🗄️: Simpan hasil di folder ProcessedPDFs (atau folder pilihanmu), terorganisir berdasarkan ID TKU Penjual.  
- Validasi File PDF ✅: Aplikasi memeriksa apakah file PDF valid (tidak korup) sebelum diproses, mencegah error selama pemrosesan.  
- Kustomisasi Tema 🎨: Pilih tema dark atau light mode untuk pengalaman visual yang lebih nyaman.  
- Versi Executable ⚡: Tersedia renamerged.exe yang tinggal klik, tanpa perlu instal Python atau library apa pun. Cocok untuk pengguna awam! 🖱️  
- Logging Cantik 📋: Output di terminal menggunakan warna-warni agar mudah dibaca, plus simpan log ke file log.txt untuk catatan.  
- Error Handling 🛠️: Jika ada PDF yang gagal dibaca (misalnya korup), Renamerged akan memberi tahu, tetapi tetap melanjutkan proses file lain.  
- Tombol Donasi 💖: Dukung pengembangan proyek ini dengan donasi via tombol di GUI!  

## Sistem Persyaratan 🖥️

Untuk versi executable (renamerged.exe):  
- Sistem Operasi: Windows 10 atau lebih baru (versi macOS/Linux akan menyusul). 😊  
- RAM: Minimal 2 GB.  
- Penyimpanan: Minimal 50 MB ruang kosong untuk aplikasi dan file log. 📂  
- Catatan: Pastikan antivirus tidak memblokir renamerged.exe (lihat bagian "Catatan Penting").  

Untuk menjalankan source code:  
- Python: Versi 3.8 atau lebih baru. 🐍  
- Library: pdfplumber, PyPDF2, colorama, customtkinter.  

## Download 📥

Yuk, download versi terbaru Renamerged di [Releases](https://github.com/ssyahbandi/PDF_Renamer/releases)! 🎁  
Ada dua pilihan untukmu:  
- renamerged.exe: Versi executable dengan GUI, tinggal download dan jalankan. Tidak perlu instal Python atau library apa pun. Cocok untuk pengguna awam! 🖱️  
- Source Code: Clone repo ini jika kamu ingin melihat atau mengedit kode. Pastikan Python dan library berikut sudah terinstal:  
  pip install pdfplumber PyPDF2 colorama customtkinter

## Cara Pakai 🚀

Menggunakan Renamerged sangat mudah berkat GUI-nya! Ikuti langkah berikut:  
1. Download renamerged.exe dari [Releases](https://github.com/ssyahbandi/PDF_Renamer/releases). 📦  
2. Klik dua kali renamerged.exe untuk menjalankan aplikasi. 🖱️  
3. Di jendela yang muncul:  
   - Klik "Browse" di bagian "Pilih Folder Input PDF", lalu pilih folder tempat file PDF kamu disimpan (contoh: C:/Dokumen/PDF). 📂  
   - Lihat pratinjau daftar file PDF yang terdeteksi di bawah "Daftar File PDF". 👀  
   - (Opsional) Klik "Browse" untuk pilih folder output tempat hasil disimpan. Jika tidak dipilih, hasil akan disimpan di ProcessedPDFs di folder input. 🗄️  
   - (Opsional) Klik "Ganti Tema" untuk beralih antara dark/light mode sesuai preferensi visualmu. 🎨  
4. Klik tombol "Proses" untuk memulai. Progress bar akan menunjukkan kemajuan proses. ✅  
5. Tunggu hingga proses selesai. Renamerged akan:  
   - Memvalidasi file PDF untuk memastikan tidak ada file korup. ✅  
   - Rename file PDF berdasarkan Nama Partner. ✍️  
   - Merge file PDF dengan ID TKU Penjual dan Nama Partner yang sama. 📚  
   - Menyimpan hasil di folder yang terorganisir berdasarkan ID TKU Penjual. 🗂️  
6. Selesai! Klik "Buka Folder Hasil" untuk melihat hasilnya. Semua PDF kamu sudah rapi terorganisir! 🎉  

## Contoh Penggunaan 📈

Berikut adalah contoh cara kerja Renamerged:  
Misalnya kamu punya 3 file PDF di folder:  
- '''dokumen1.pdf''': ID TKU = 1234567890123456789012, Nama Partner = '''PT ABC'''.  
- '''dokumen2.pdf''': ID TKU = 1234567890123456789012, Nama Partner = '''PT ABC'''.  
- '''dokumen3.pdf''': ID TKU = 9876543210987654321098, Nama Partner = '''PT XYZ'''.  

Setelah menjalankan Renamerged:  
- '''dokumen1.pdf''' dan '''dokumen2.pdf''' digabung menjadi PT ABC.pdf, disimpan di '''ProcessedPDFs/1234567890123456789012/PT ABC.pdf'''.  
- '''dokumen3.pdf''' di-rename menjadi '''PT XYZ.pdf''', disimpan di '''ProcessedPDFs/9876543210987654321098/PT XYZ.pdf'''.  

Mudah, bukan? Tidak perlu repot membuka file satu per satu! 😍

## Catatan Penting ⚠️

Sebelum menggunakan Renamerged, perhatikan hal berikut:  
- Keamanan File: File ini 100% aman dan bebas virus! Namun, karena dibuat menggunakan PyInstaller, beberapa antivirus (seperti Windows Defender) mungkin mendeteksi sebagai "false positive". Jangan khawatir, tambahkan ke exclusion:  
  - Windows Defender: Settings > Virus & Threat Protection > Manage Settings > Add or Remove Exclusions > Tambah renamerged.exe. 🛡️  
- Kendala?: Jika ada masalah saat menggunakan Renamerged, jangan ragu hubungi saya di [Telegram](https://t.me/ssyahbandi). Saya siap membantu kapan saja! 📞  

## Donasi 🎁

Membuat Renamerged membutuhkan waktu dan usaha, dari coding hingga testing agar aplikasi ini benar-benar berguna untukmu. 💻 Jika kamu merasa Renamerged membantu, dukung saya dengan donasi via tombol "Donasi" di aplikasi, atau langsung ke link ini: [Donasi via QRIS](https://bit.ly/kiyuris). Donasi kamu akan membantu saya terus mengembangkan proyek ini, mungkin menambah fitur baru yang lebih keren lagi! Terima kasih banyak! 😄💖

## Kontribusi dan Feedback 🙌

Saya sangat terbuka untuk masukan! Jika kamu punya ide fitur baru (misalnya, sortir PDF berdasarkan tanggal) atau menemukan bug, langsung hubungi saya via [Telegram](https://t.me/ssyahbandi). Kamu juga bisa membuka issue di repo ini, saya akan merespons secepat mungkin! 🚀

## Changelog 📅

### Versi 1.1.0  
- GUI Modern: Ditambahkan antarmuka grafis dengan progress bar untuk memantau proses. 🖥️  
- Pratinjau File PDF: Menampilkan daftar file PDF yang terdeteksi sebelum diproses. 📄  
- Validasi File PDF: Memeriksa apakah file PDF valid (tidak korup) sebelum diproses. ✅  
- Kustomisasi Tema: Menambahkan opsi untuk beralih antara dark dan light mode. 🎨  
- Penghapusan Log Proses di GUI: Log proses di GUI dihapus untuk menyederhanakan tampilan, tetapi tetap disimpan di file log.txt. 📋  
- Penjajaran Tombol: Tombol "Donasi" dan "Ganti Tema" disusun rapi di sisi kanan atas, sejajar dengan tombol "Browse". 🖱️  

### Versi 1.0.0
- First Realese
- GUI Based

## Terima Kasih! 💖

Terima kasih sudah mencoba Renamerged! Semoga aplikasi ini membuat hidupmu lebih mudah dan dokumenmu lebih rapi. Jangan lupa share ke teman-teman yang membutuhkan, ya! 😊 Saya harap Renamerged bisa menjadi teman setia untuk urusan PDF-mu! 🌟