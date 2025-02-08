import pdfplumber
import re
import os
import shutil
from datetime import datetime
from colorama import Fore, Style, init
import time

init(autoreset=True)

def welcome_message():
    print(Fore.MAGENTA + "==============================================")
    print(Fore.CYAN + "✨ Selamat Datang di PDF Renamer ✨")
    print(Fore.CYAN + "📜 Script by Syahbandi - PT BBN SURABAYA")
    print(Fore.MAGENTA + "==============================================")
    time.sleep(2)

def extract_info_from_pdf(pdf_path, debug=False):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    
    if debug:
        print(Fore.YELLOW + "========== RAW TEXT ==========")
        print(text)
        print(Fore.YELLOW + "==============================")

    # Ekstrak Nama Lawan Transaksi
    partner_name_match = re.search(r'Pembeli Barang Kena Pajak\s*/\s*Penerima Jasa Kena Pajak:\s*Nama\s*:\s*(.+?)\s*Alamat', text)
    partner_name = partner_name_match.group(1).strip().title() if partner_name_match else "Nama Tidak Ditemukan"

    # Ekstrak Tanggal
    date_match = re.search(r'(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})', text)
    month_dict = {
        "Januari": "01", "Februari": "02", "Maret": "03", "April": "04",
        "Mei": "05", "Juni": "06", "Juli": "07", "Agustus": "08",
        "September": "09", "Oktober": "10", "November": "11", "Desember": "12"
    }
    date = f"{date_match.group(1)}-{month_dict.get(date_match.group(2), '00')}-{date_match.group(3)}" if date_match else "Tanggal Tidak Ditemukan"

    # Ekstrak Referensi
    reference_match = re.search(r'Referensi:\s*([^)]*)', text)
    reference = reference_match.group(1).strip() if reference_match and reference_match.group(1).strip() else "Tidak Ada Referensi"

    # Ekstrak Nomor Faktur Pajak
    faktur_match = re.search(r'Kode dan Nomor Seri Faktur Pajak:\s*(\d+)', text)
    faktur_number = faktur_match.group(1) if faktur_match else "No Faktur"

    return partner_name, faktur_number, date, reference

def get_unique_filename(directory, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base} - {counter}{ext}"
        counter += 1
    return new_filename

def rename_pdf_files(input_directory, use_reference, use_faktur, debug=False):
    output_directory = os.path.join(input_directory, "RenamedPDFs")
    log_file = os.path.join(input_directory, "log.txt")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    total_files = len([f for f in os.listdir(input_directory) if f.endswith('.pdf')])
    processed_files = 0
    error_files = 0

    with open(log_file, "a", encoding="utf-8") as log:
        log.write("\n======================================\n")
        log.write(f"Log proses pada {datetime.now()}\n")
        log.write("======================================\n")

    print(Fore.CYAN + "\n================= Proses Dimulai =================")
    print(f"Total file ditemukan: {total_files}\n")

    for filename in os.listdir(input_directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_directory, filename)
            try:
                partner_name, faktur_number, date, reference = extract_info_from_pdf(pdf_path, debug)

                # Bangun nama file berdasarkan pilihan user
                parts = [partner_name]
                if use_faktur == 'Y':
                    parts.append(faktur_number)
                parts.append(date)
                if use_reference == 'Y':
                    parts.append(reference)

                new_filename = " ".join(parts) + ".pdf"
                unique_filename = get_unique_filename(output_directory, new_filename)
                new_pdf_path = os.path.join(output_directory, unique_filename)

                shutil.copy(pdf_path, new_pdf_path)
                processed_files += 1
                print(Fore.GREEN + f"✔ Berhasil: {filename} -> {unique_filename}")

                with open(log_file, "a", encoding="utf-8") as log:
                    log.write(f"✔ {filename} -> {unique_filename}\n")
            except Exception as e:
                error_files += 1
                print(Fore.RED + f"✖ Error processing {filename}: {e}")
                with open(log_file, "a", encoding="utf-8") as log:
                    log.write(f"✖ Error {filename}: {e}\n")

    print(Fore.CYAN + "\n================= Proses Selesai =================")
    print(Fore.YELLOW + f"Total sampel: {total_files}")
    print(Fore.GREEN + f"Total diproses: {processed_files}")
    print(Fore.RED + f"Total error: {error_files}")

def main():
    welcome_message()
    
    # Pilihan untuk menggunakan Referensi
    use_reference = input(Fore.BLUE + "Apakah kamu ingin pakai referensi? (Y/N) (Default Y): ").strip().upper()
    if use_reference not in ['Y', 'N', '']:
        print(Fore.RED + "Input tidak valid. Pilih Y atau N.")
        return
    use_reference = use_reference if use_reference else 'Y'

    # Pilihan untuk menggunakan Nomor Faktur Pajak
    use_faktur = input(Fore.BLUE + "Apakah kamu ingin pakai Nomor Faktur? (Y/N) (Default Y): ").strip().upper()
    if use_faktur not in ['Y', 'N', '']:
        print(Fore.RED + "Input tidak valid. Pilih Y atau N.")
        return
    use_faktur = use_faktur if use_faktur else 'Y'

    input_directory = input(Fore.BLUE + "Masukkan path direktori input: ")

    if not os.path.exists(input_directory):
        print(Fore.RED + f"Direktori '{input_directory}' tidak ditemukan.")
        return

    rename_pdf_files(input_directory, use_reference, use_faktur, debug=False)

if __name__ == "__main__":
    main()
