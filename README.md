# PDF Renamer 📜✨

Selamat datang di **PDF Renamer**, aplikasi sederhana tapi powerful untuk membantu kamu mengelola file PDF dengan mudah! 🎉 Aplikasi ini dirancang khusus untuk rename dan merge file PDF berdasarkan ID TKU Penjual dan Nama Lawan Transaksi, cocok buat kamu yang sering deal sama dokumen pajak atau transaksi bisnis. Dengan PDF Renamer, urusan dokumen jadi lebih rapi dan hemat waktu! 🚀

## Apa Itu PDF Renamer? 🤔
PDF Renamer adalah alat kecil yang aku buat untuk membantu:
- **Rename** file PDF berdasarkan informasi di dalamnya (ID TKU Penjual dan Nama Partner). 📝
- **Merge** beberapa PDF yang punya ID TKU dan nama partner yang sama jadi satu file. 📚
- Bikin hidupmu lebih mudah dengan mengotomatiskan proses yang biasanya ribet! 😎

Aplikasi ini awalnya cuma proyek kecil, tapi sekarang udah siap dipake sama siapa aja, termasuk kamu yang nggak paham coding! 💻

## Fitur Unggulan 🌟
- Rename PDF otomatis berdasarkan konten (ID TKU dan Nama Partner). 📂
- Merge PDF dengan ID TKU yang sama jadi satu file rapi. 📦
- Simpan hasil di folder `ProcessedPDFs`, terorganisir berdasarkan ID TKU. 🗂️
- Antarmuka sederhana via terminal, nggak perlu ribet setup GUI. 🖥️
- Versi executable (`renamerged.exe`) yang tinggal klik, tanpa perlu instal Python! ⚡

## Download 📥
Yuk, download versi terbaru di [Releases](https://github.com/ssyahbandi/PDF_Renamer/releases)! 🎁  
Ada dua pilihan buat kamu:  
- **`renamerged.exe`**: Versi executable, tinggal download dan run. Nggak perlu instal Python atau library apa pun. Cocok buat pengguna awam! 🖱️  
- **Source code (`renamerged.py`)**: Buat kamu yang mau lihat atau edit kode, bisa jalankan manual pake Python (pastikan `pdfplumber`, `PyPDF2`, dan `colorama` udah terinstal). 🖥️  

## Cara Pakai 🚀
Menggunakan PDF Renamer itu gampang banget, ikutin langkah ini:  
1. Download `renamerged.exe` dari [Releases](https://github.com/ssyahbandi/PDF_Renamer/releases). 📦  
2. Klik 2x `renamerged.exe` buat jalanin aplikasinya. 🖱️  
3. Masukkan path folder tempat file PDF kamu disimpan (contoh: `C:\Dokumen\PDF`). 📂  
4. Tunggu bentar, PDF Renamer bakal kerja otomatis: rename file PDF, merge kalau ada yang sama, dan simpan hasilnya di folder `ProcessedPDFs`. ✅  
5. Selesai! Cek hasilnya, semua PDF kamu udah rapi terorganisir berdasarkan ID TKU Penjual. 🎉  

## Catatan Penting ⚠️
Sebelum pakai, ada beberapa hal yang perlu kamu tahu:  
- **Keamanan File**: File ini 100% aman dan bebas virus! Tapi, karena dibuat pake PyInstaller, beberapa antivirus (kayak Windows Defender) mungkin flag sebagai "false positive". Jangan khawatir, cukup tambahkan ke exclusion:  
  - Windows Defender: Settings > Virus & Threat Protection > Manage Settings > Add or Remove Exclusions > Tambah `renamerged.exe`. 🛡️  
- **Kendala?**: Kalau ada masalah pas pakai aplikasi ini, jangan ragu hubungi aku di [Telegram](https://t.me/ssyahbandi). Aku siap bantu kapan aja! 📞  

## Donasi 🎁
Membuat PDF Renamer butuh waktu dan usaha, dari coding sampe testing biar aplikasi ini bener-bener berguna buat kamu. 💻 Kalau kamu merasa aplikasi ini membantu, boleh banget dukung aku dengan donasi via QRIS: [Link](https://bit.ly/kiyuris). Donasi kamu bakal bantu aku terus kembangin proyek ini. Terima kasih banyak! 😄💖

## Bonus: Behind the Scenes! 😂
Aku pas selesai coding dan nggak nemuin bug:  
![No Bugs](https://github.com/user-attachments/assets/dd877119-bbbb-45af-a974-0e74610ac478)  
Seneng banget rasanya pas semua berjalan lancar! 🎈

## Kontribusi dan Feedback 🙌
Aku sangat terbuka buat masukan! Kalau kamu punya ide fitur baru, atau nemuin bug, langsung aja hubungi aku via [Telegram](https://t.me/ssyahbandi). Atau, buka issue di repo ini, aku bakal respon secepat mungkin! 🚀

## Terima Kasih! 💖
Terima kasih udah nyobain PDF Renamer! Semoga aplikasi ini bikin hidupmu lebih mudah dan dokumenmu lebih rapi. Jangan lupa share ke temen-temen yang butuh, ya! 😊
