# PDF Renamer
PDF Renamer adalah sebuah script Python yang digunakan untuk mengganti nama file PDF faktur pajak secara otomatis berdasarkan informasi yang diekstrak dari isi dokumen.

## 📌 Fitur

- Ekstraksi Informasi Otomatis: Mengambil nama lawan transaksi, tanggal, dan nomor referensi dari dokumen PDF.

- Penamaan Ulang File: Mengganti nama file PDF sesuai dengan format: Nama_Pembeli DD-MM-YYYY Referensi.pdf.

- Log File: Menyimpan catatan proses renaming dalam file log.txt.

- Mode Debugging: Menampilkan teks mentah dari PDF untuk analisis jika diaktifkan.

- Penanganan Nama File Duplikat: Jika nama file yang baru sudah ada, maka ditambahkan angka -2, -3, dan seterusnya.

- Dukungan Multi-Halaman: Bisa membaca dokumen PDF yang memiliki lebih dari 1 halaman.

## 🛠️ Instalasi

1. Install Python (jika belum terpasang)

   - Pastikan Python 3.8 atau versi yang lebih baru sudah terinstal di sistem kamu. Bisa dicek dengan perintah:

   - ```python --version```

   - Jika belum ada, download dan install dari [python.org](https://www.python.org/downloads/)

3. Clone Repository

    - ```git clone https://github.com/ssyahbandi/PDF_Renamer.git```

    - ```cd PDF-Renamer```

3. Install Dependencies

   - Gunakan pip untuk menginstal library yang diperlukan:

   - ```pip install -r requirements.txt```

  - Jika pip tidak dikenali, coba gunakan pip3.


## 🚀 Cara Penggunaan

1. Jalankan script dengan perintah:

   - ```python rename.py```

2. Masukkan path folder yang berisi file PDF faktur pajak.

3. Script akan memproses semua file PDF dalam folder tersebut.

4. Hasil rename akan disimpan di folder RenamedPDFs.

   - Jika ingin menjalankan mode debugging:

   - ```python rename.py --debug```
   

## 📝 Catatan

File log disimpan dalam log.txt untuk melihat daftar file yang berhasil atau gagal diproses.

Pastikan folder input berisi file PDF yang valid.

## 📌 Lisensi

Script ini bersifat open-source, silakan digunakan dan dimodifikasi sesuai kebutuhan. 🚀
