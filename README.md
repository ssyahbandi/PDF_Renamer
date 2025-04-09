# Renamerged 📜✨

Halo, temen-temen! Selamat datang di **Renamerged**! 🎉 Aplikasi ini adalah solusi praktis buat kamu yang sering pusing ngurusin file PDF, apalagi dokumen pajak atau transaksi bisnis yang numpuk. Renamerged (singkatan dari **Rename-Merged**) dirancang untuk **rename** dan **merge** file PDF secara otomatis berdasarkan ID TKU Penjual dan Nama Lawan Transaksi. Dengan Renamerged, dokumenmu bakal rapi terorganisir tanpa harus kerja manual yang bikin capek! 😍

Sekarang Renamerged hadir dengan **GUI sederhana** yang bikin penggunaan jauh lebih gampang, bahkan buat kamu yang nggak suka ketik-ketik di terminal! 🖥️ Yuk, simak lebih lanjut apa yang bisa Renamerged lakuin buat kamu! 🌟

## Apa Itu Renamerged? 🤔💡
Renamerged adalah alat kecil yang aku buat untuk membantu mengelola file PDF dengan cara yang super efisien. Bayangin, kamu punya ratusan PDF dengan ID TKU Penjual dan Nama Partner yang berbeda-beda. Kalau rename satu-satu, bisa seharian! 😅 Nah, Renamerged bakal bantu:  
- **Rename File PDF Otomatis** 📝: Aplikasi ini baca isi PDF, ambil ID TKU Penjual (22 digit) dan Nama Lawan Transaksi, lalu ganti nama file PDF-nya sesuai Nama Partner.  
- **Merge PDF yang Sama** 📚: Kalau ada beberapa PDF dengan ID TKU Penjual dan Nama Partner yang sama, Renamerged bakal gabungin semua file itu jadi satu PDF rapi.  
- **Organisasi File** 🗂️: Semua hasil disimpan di folder `ProcessedPDFs` (atau folder yang kamu pilih), diorganisir berdasarkan ID TKU Penjual, jadi gampang dicari kapan aja.  

Aplikasi ini cocok banget buat kamu yang sering deal sama dokumen pajak, transaksi bisnis, atau file PDF yang butuh dirapiin. Renamerged bakal bikin hidupmu lebih mudah, tanpa harus kerja manual lagi! 🚀

## Fitur Unggulan 🌟
Renamerged punya beberapa fitur keren yang bikin dia beda dari alat lain:  
- **GUI Sederhana** 🖥️: Antarmuka grafis yang gampang dipake, tinggal klik untuk pilih folder, nggak perlu ketik path manual!  
- **Rename PDF Otomatis** 📂: Rename file PDF berdasarkan ID TKU Penjual dan Nama Lawan Transaksi, jadi nggak perlu buka file satu-satu.  
- **Merge PDF yang Sama** 📦: Gabungin semua PDF dengan ID TKU Penjual dan Nama Partner yang sama jadi satu file rapi. Hemat ruang, hemat waktu!  
- **Organisasi File** 🗄️: Simpan hasil di folder `ProcessedPDFs` (atau folder pilihanmu), terorganisir berdasarkan ID TKU Penjual.  
- **Versi Executable** ⚡: Ada `renamerged.exe` yang tinggal klik, nggak perlu instal Python atau library apa pun. Cocok buat pengguna awam!  
- **Logging Cantik** 📋: Output di terminal pake warna-warni biar gampang dibaca, plus simpan log ke file `log.txt` buat catatan.  
- **Error Handling** 🛠️: Kalau ada PDF yang gagal dibaca (misalnya corrupt), Renamerged bakal kasih tau, tapi tetap lanjut proses file lain.  

## Download 📥
Yuk, download versi terbaru Renamerged di [Releases](https://github.com/ssyahbandi/PDF_Renamer/releases)! 🎁  
Ada dua pilihan buat kamu:  
- **`renamerged.exe`**: Versi executable dengan GUI, tinggal download dan run. Nggak perlu instal Python atau library apa pun. Cocok banget buat pengguna awam! 🖱️  
- **Source code**: Clone repo ini kalau kamu mau lihat atau edit kode. Pastikan Python dan library (`pdfplumber`, `PyPDF2`, `colorama`) udah terinstal. 🖥️  

## Cara Pakai 🚀
Menggunakan Renamerged sekarang jauh lebih gampang berkat GUI-nya! Ikutin langkah ini:  
1. Download `renamerged.exe` dari [Releases](https://github.com/ssyahbandi/PDF_Renamer/releases). 📦  
2. Klik 2x `renamerged.exe` buat jalanin aplikasinya. 🖱️  
3. Di jendela yang muncul, klik "Browse" di bagian "Pilih File PDF", lalu pilih salah satu file PDF di folder yang berisi file PDF kamu (contoh: pilih `dokumen1.pdf` di `C:/Users/Download/PDF`). Aplikasi akan otomatis memproses semua file PDF di folder itu. 📂  
4. (Opsional) Klik "Browse" untuk pilih folder output tempat hasil disimpan. Kalau nggak pilih, hasil bakal disimpan di `ProcessedPDFs` di folder input. 🗄️  
5. Klik tombol "Process PDFs", tunggu bentar, Renamerged bakal kerja otomatis: rename file PDF, merge kalau ada yang sama, dan simpan hasilnya. ✅  
6. Selesai! Cek hasilnya, semua PDF kamu udah rapi terorganisir berdasarkan ID TKU Penjual. 🎉  

## Contoh Penggunaan 📈
Biar lebih jelas, ini contoh gimana Renamerged kerja:  
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