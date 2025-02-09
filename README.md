# PDF Renamer
PDF Renamer adalah sebuah script Python yang digunakan untuk mengganti nama file PDF faktur pajak secara otomatis berdasarkan informasi yang diekstrak dari isi dokumen.

JIka ada kendala silahkan hubungi saya di [Whatsapp](wa.me/6285155018808)

## 📌 Fitur

- Ekstraksi Informasi Otomatis: Mengambil nama lawan transaksi, tanggal, dan nomor referensi dari dokumen PDF.

- Penamaan Ulang File: Mengganti nama file PDF sesuai dengan format: Nama_Pembeli DD-MM-YYYY Referensi.pdf.

- Log File: Menyimpan catatan proses renaming dalam file log.txt.

- Penanganan Nama File Duplikat: Jika nama file yang baru sudah ada, maka ditambahkan angka -2, -3, dan seterusnya.

- Dukungan Multi-Halaman: Bisa membaca dokumen PDF yang memiliki lebih dari 1 halaman.

## 🛠️ Instalasi

1. Install Python (jika belum terpasang)

   - Pastikan Python 3.8 atau versi yang lebih baru sudah terinstal di sistem kamu. Bisa dicek dengan perintah: (Buka CMD kemudian tekan (Windows + R) lalu ketik CMD)

   - ```python --version```
  
   - Jika python sudah terinstal maka outputnya akan seperti ini :
     ![image](https://github.com/user-attachments/assets/7536e43e-d14e-4468-af9d-48e446c9452d)


   - Jika belum ada, download dan install dari [python.org](https://www.python.org/downloads/)
  
   - Setelah unduhan selesai, buka file installer yang telah diunduh.
     
   - Pastikan untuk mencentang opsi **"Add Python to PATH"** sebelum mengklik "Install Now". Ini akan memudahkan Anda untuk menjalankan Python dari command prompt.

3. Clone Repository

    - ```git clone https://github.com/ssyahbandi/PDF_Renamer.git```

      ![image](https://github.com/user-attachments/assets/7b01bf70-ceb6-42a5-b385-69686f29660f)
      

    - ```cd PDF_Renamer```
  
      ![image](https://github.com/user-attachments/assets/4f1e0bf9-867b-4e99-81d0-4c9446d628b0)
      

    - Atau kamu bisa mendownloadnya menjadi folder zip (Jika pakai download ZIP abaikan git clone dan cd PDF Renamer jika pakai metode Download ZIP, jangan lupa diekstrak ya)

      ![image](https://github.com/user-attachments/assets/7ed32c5c-e9e5-44de-9cc3-0a5874cb397b)
      

3. Install Dependencies

   - Gunakan pip untuk menginstal library yang diperlukan:

   - ```pip install -r requirements.txt```
  
     ![image](https://github.com/user-attachments/assets/bfc81b5c-ae3b-4592-8862-2477ad68870d)

  - Jika pip tidak dikenali, coba gunakan pip3.


## 🚀 Cara Penggunaan

   Sebelum ke tahap selanjutnya, saya anggap kamu sudah mendownload semua PDF Faktur Pajak yang dari Coretax, dan memindahkannya ke Folder (Nama bebas) saya disini menggunakan nama Folder "PDF" (Supaya nanti mudah, bisa diesuaikan dengan kebutuhanmu ya"

   ![image](https://github.com/user-attachments/assets/7be5f098-e152-4a55-ad2b-9c46871f0775)


   Dan ini file pdf hasil download yang sudah saya pindahkan ke folder PDF

   ![image](https://github.com/user-attachments/assets/767489f0-a909-4d0c-ae65-6ae18fd6132b)


1. Jalankan script dengan perintah:

   - ```python rename.py```

     ![image](https://github.com/user-attachments/assets/68f1d89f-ad24-4780-8720-81221b488213)


2. Masukkan path folder yang berisi file PDF faktur pajak.

   - Pilih folder PATH yang berisi Faktur Pajak PDF yang didownload tadi, sebagai contoh saya menggunakan ini (lokasi folder dimana PDF nya itu berada)
  
     ![image](https://github.com/user-attachments/assets/fac552bf-d124-47f9-8364-875401f5929f)

   - Pilih antara pakai Refrensi (yang ada di dalam PDF Efaktur atau tidak)

     ![image](https://github.com/user-attachments/assets/004c8131-4e37-467a-aae8-fcdbd80b2f40)

4. Script akan memproses semua file PDF dalam folder tersebut.

   ![image](https://github.com/user-attachments/assets/5c5fb383-7cc2-4f16-8578-260021796125)

   - Nanti ada folder Nomor IDTKU jika di dalam PDF tersebut ada Nomor IDTKU Penjual yang berbeda, jadi sangat cocok untuk perusahaan dengan banyak cabang yang berbeda Nomor IDTKU nya

   ![image](https://github.com/user-attachments/assets/82ef609c-b688-4491-9f48-07df9806d10f)


5. Hasil rename akan disimpan di folder RenamedPDFs/Nomor IDTKU.

 ![image](https://github.com/user-attachments/assets/ad6086c8-0a24-4fda-b46c-3e5dbb35bf75)

6. Output hasil PDF yang sudah di Rename adalah

   ***PT Abc Def 04002500015206238 01/01/2025 INV-CV2501001***


## 📝 Catatan

File log disimpan dalam log.txt untuk melihat daftar file yang berhasil atau gagal diproses.

Pastikan folder input berisi file PDF yang valid.

## 📌 Lisensi

Script ini bersifat open-source, silakan digunakan dan dimodifikasi sesuai kebutuhan. 🚀
