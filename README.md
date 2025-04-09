# Renamerged 📜✨

Halo, selamat datang di **Renamerged**! 🎉 Aplikasi ini adalah solusi praktis untuk kamu yang sering ribet ngurusin file PDF, terutama dokumen pajak atau transaksi bisnis. Renamerged (singkatan dari **Rename-Merged**) dirancang untuk **rename** dan **merge** file PDF secara otomatis berdasarkan ID TKU Penjual dan Nama Lawan Transaksi. Dengan Renamerged, dokumenmu bakal rapi terorganisir tanpa harus kerja manual lagi! 🚀

## Apa Itu Renamerged? 🤔💡
Renamerged adalah alat kecil yang aku buat untuk membantu mengelola file PDF dengan cara yang super efisien. Bayangin, kamu punya ratusan PDF dengan ID TKU Penjual dan Nama Partner yang berbeda-beda. Kalau rename satu-satu, bisa seharian! 😅 Nah, Renamerged bakal bantu:  
- **Rename File PDF Otomatis** 📝: Aplikasi ini baca isi PDF, ambil ID TKU Penjual (22 digit) dan Nama Lawan Transaksi, lalu ganti nama file PDF-nya sesuai Nama Partner.  
- **Merge PDF yang Sama** 📚: Kalau ada beberapa PDF dengan ID TKU Penjual dan Nama Partner yang sama, Renamerged bakal gabungin semua file itu jadi satu PDF rapi.  
- **Organisasi File** 🗂️: Semua hasil disimpan di folder `ProcessedPDFs`, diorganisir berdasarkan ID TKU Penjual, jadi gampang dicari kapan aja.  

Aplikasi ini awalnya cuma proyek kecil buat kebutuhan pribadi, tapi sekarang udah siap dipake sama siapa aja, bahkan buat kamu yang nggak paham coding sekalipun! 💻

## Fitur Unggulan 🌟
- Rename PDF otomatis berdasarkan ID TKU Penjual dan Nama Lawan Transaksi. 📂  
- Merge PDF dengan ID TKU yang sama jadi satu file rapi. 📦  
- Simpan hasil di folder `ProcessedPDFs`, terorganisir berdasarkan ID TKU. 🗄️  
- Antarmuka sederhana via terminal, nggak perlu setup ribet. 🖥️  
- Versi executable (`renamerged.exe`) yang tinggal klik, tanpa perlu instal Python! ⚡  
- Logging cantik pake warna di terminal, plus simpan log ke file `log.txt`. 📋  

## Download 📥
Yuk, download versi terbaru Renamerged di [Releases](https://github.com/ssyahbandi/PDF_Renamer/releases)! 🎁  
Ada dua pilihan buat kamu:  
- **`renamerged.exe`**: Versi executable, tinggal download dan run. Nggak perlu instal Python atau library apa pun. Cocok banget buat pengguna awam! 🖱️  
- **Source code (`renamerged.py`)**: Buat kamu yang mau lihat atau edit kode, bisa jalankan manual pake Python (pastikan `pdfplumber`, `PyPDF2`, dan `colorama` udah terinstal). 🖥️  

## Cara Pakai 🚀
Menggunakan Renamerged itu gampang banget, ikutin langkah ini:  
1. Download `renamerged.exe` dari [Releases](https://github.com/ssyahbandi/PDF_Renamer/releases). 📦  
2. Klik 2x `renamerged.exe` buat jalanin aplikasinya. 🖱️  
3. Masukkan path folder tempat file PDF kamu disimpan (contoh: `C:\Dokumen\PDF`). 📂  
4. Tunggu bentar, Renamerged bakal kerja otomatis: rename file PDF, merge kalau ada yang sama, dan simpan hasilnya di folder `ProcessedPDFs`. ✅  
5. Selesai! Cek hasilnya, semua PDF kamu udah rapi terorganisir berdasarkan ID TKU Penjual. 🎉  

## Contoh Penggunaan 📈
Misalnya kamu punya 3 file PDF di folder:  
- `dokumen1.pdf`: ID TKU = `1234567890123456789012`, Nama Partner = `PT ABC`.  
- `dokumen2.pdf`: ID TKU = `1234567890123456789012`, Nama Partner = `PT ABC`.  
- `dokumen3.pdf`: ID TKU = `9876543210987654321098`, Nama Partner = `PT XYZ`.  

Setelah jalankan Renamerged:  
- `dokumen1.pdf` dan `dokumen2.pdf` digabung jadi `PT ABC.pdf`, disimpan di `ProcessedPDFs/1234567890123456789012/PT ABC.pdf`.  
- `dokumen3.pdf` di-rename jadi `PT XYZ.pdf`, disimpan di `ProcessedPDFs/9876543210987654321098/PT XYZ.pdf`.  

Gampang, kan? Nggak perlu repot buka file satu-satu! 😍

## Catatan Penting ⚠️
Sebelum pakai, ada beberapa hal yang perlu kamu tahu:  
- **Keamanan File**: File ini 100% aman dan bebas virus! Tapi, karena dibuat pake PyInstaller, beberapa antivirus (kayak Windows Defender) mungkin flag sebagai "false positive". Jangan khawatir, cukup tambahkan ke exclusion:  
  - Windows Defender: Settings > Virus & Threat Protection > Manage Settings > Add or Remove Exclusions > Tambah `renamerged.exe`. 🛡️  
- **Kendala?**: Kalau ada masalah pas pakai Renamerged, jangan ragu hubungi aku di [Telegram](https://t.me/ssyahbandi). Aku siap bantu kapan aja! 📞  

## Donasi 🎁
Membuat Renamerged butuh waktu dan usaha, dari coding sampe testing biar aplikasi ini bener-bener berguna buat kamu. 💻 Kalau kamu merasa Renamerged membantu, boleh banget dukung aku dengan donasi via QRIS: [Link](https://bit.ly/kiyuris). Donasi kamu bakal bantu aku terus kembangin proyek ini, mungkin nambah fitur baru yang lebih keren lagi! Terima kasih banyak! 😄💖

## Bonus: Behind the Scenes! 😂
Aku pas selesai coding dan nggak nemuin bug:  
![No Bugs](https://github.com/user-attachments/assets/dd877119-bbbb-45af-a974-0e74610ac478)  
Seneng banget rasanya pas semua berjalan lancar! 🎈

## Kontribusi dan Feedback 🙌
Aku sangat terbuka buat masukan! Kalau kamu punya ide fitur baru, seperti tambah fitur sortir PDF berdasarkan tanggal, atau nemuin bug, langsung aja hubungi aku via [Telegram](https://t.me/ssyahbandi). Atau, buka issue di repo ini, aku bakal respon secepat mungkin! 🚀

## Terima Kasih! 💖
Terima kasih udah nyobain Renamerged! Semoga aplikasi ini bikin hidupmu lebih mudah dan dokumenmu lebih rapi. Jangan lupa share ke temen-temen yang butuh, ya! 😊 Aku harap Renamerged bisa jadi temen setia buat urusan PDF-mu! 🌟
