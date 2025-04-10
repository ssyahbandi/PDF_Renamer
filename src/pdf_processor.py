import pdfplumber
import re
import os
import shutil
from PyPDF2 import PdfMerger
from src.utils import log_message, Fore

def validate_pdf(pdf_path):
    """Memvalidasi apakah file PDF dapat dibaca (tidak korup)."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            # Coba baca halaman pertama untuk memastikan file valid
            if pdf.pages:
                return True
        return False
    except Exception as e:
        return False

def extract_info_from_pdf(pdf_path, log_callback=None):
    """Mengambil nama partner dan ID TKU Penjual dari PDF."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = "".join(page.extract_text() + "\n" for page in pdf.pages if page.extract_text())

        # Ekstrak Nama Partner (Lawan Transaksi)
        partner_match = re.search(r'Pembeli Barang Kena Pajak\s*/\s*Penerima Jasa Kena Pajak:\s*Nama\s*:\s*(.+?)\s*Alamat', text, re.DOTALL)
        partner_name = partner_match.group(1).strip().title() if partner_match else "Nama tidak ditemukan"

        # Ekstrak ID TKU Penjual (22 Digit)
        id_tku_seller_match = re.search(r'#?(\d{22})', text)
        id_tku_seller = id_tku_seller_match.group(1).strip() if id_tku_seller_match else "IDTKU_Tidak_Ditemukan"

        return id_tku_seller, partner_name
    except Exception as e:
        if log_callback:
            log_callback(f"❌ Error membaca {os.path.basename(pdf_path)}: {str(e)}")
        raise

def process_pdfs(input_directory, output_directory=None, progress_callback=None, log_callback=None):
    """Memproses file PDF: rename jika 1, merge jika lebih dari 1, dengan dukungan progress callback."""
    if output_directory is None or output_directory.strip() == "":
        output_directory = os.path.join(input_directory, "ProcessedPDFs")
    os.makedirs(output_directory, exist_ok=True)
    
    # Tahap 1: Perhitungan file PDF (tidak ada progress callback)
    pdf_files = [f for f in os.listdir(input_directory) if f.endswith('.pdf')]
    total_files = len(pdf_files)
    log_message(f"Total file ditemukan: {total_files}", Fore.CYAN, log_callback)

    # Tahap 2: Pembacaan dan pengelompokan (40%)
    idtku_seller_groups = {}
    processed_files = 0
    error_files = 0
    for filename in pdf_files:
        pdf_path = os.path.join(input_directory, filename)
        # Validasi file PDF sebelum diproses
        if not validate_pdf(pdf_path):
            error_files += 1
            log_message(f"⚠️ File {filename} korup atau tidak valid, dilewati.", Fore.YELLOW, log_callback)
            continue

        try:
            id_tku_seller, partner_name = extract_info_from_pdf(pdf_path, log_callback)
            
            if partner_name == "Nama tidak ditemukan":
                log_message(f"⚠️ Nama tidak ditemukan di {filename}, dilewati.", Fore.YELLOW, log_callback)
                continue
            
            if id_tku_seller not in idtku_seller_groups:
                idtku_seller_groups[id_tku_seller] = {}
            if partner_name not in idtku_seller_groups[id_tku_seller]:
                idtku_seller_groups[id_tku_seller][partner_name] = []
            
            idtku_seller_groups[id_tku_seller][partner_name].append(pdf_path)
        
        except Exception as e:
            error_files += 1
            # Pesan error sudah ditangani di extract_info_from_pdf

        processed_files += 1
        if progress_callback:
            progress_callback("reading", processed_files, total_files)

    # Tahap 3: Pemrosesan (rename atau merge) (50%)
    total_groups = sum(len(partner_files) for partner_files in idtku_seller_groups.values())
    processed_groups = 0
    renamed_files = 0
    merged_files = 0

    for id_tku_seller, partner_files in idtku_seller_groups.items():
        idtku_folder = os.path.join(output_directory, id_tku_seller)
        os.makedirs(idtku_folder, exist_ok=True)
        
        for partner_name, files in partner_files.items():
            if len(files) == 1:
                # Hanya ada 1 file, cukup rename & pindahkan ke folder ID TKU Penjual
                source_path = files[0]
                new_filename = f"{partner_name}.pdf"
                destination_path = os.path.join(idtku_folder, new_filename)
                shutil.copy(source_path, destination_path)
                renamed_files += 1
                log_message(f"📂 {new_filename} dipindahkan ke {idtku_folder}", Fore.BLUE, log_callback)
            else:
                # Ada lebih dari 1 file, lakukan merge dan simpan di folder ID TKU Penjual
                try:
                    merger = PdfMerger()
                    for pdf_path in sorted(files):
                        merger.append(pdf_path)
                    
                    merged_filename = f"{partner_name}.pdf"
                    merged_path = os.path.join(idtku_folder, merged_filename)
                    
                    with open(merged_path, "wb") as fout:
                        merger.write(fout)
                    merger.close()
                    
                    merged_files += 1
                    log_message(f"✅ {len(files)} file berhasil digabung menjadi {merged_filename} di {idtku_folder}", Fore.GREEN, log_callback)
                except Exception as e:
                    log_message(f"❌ Gagal merge {partner_name}: {str(e)}", Fore.RED, log_callback)
            
            processed_groups += 1
            if progress_callback:
                progress_callback("processing", processed_groups, total_groups)

    # Tahap 4: Finalisasi (10%)
    if progress_callback:
        progress_callback("finalizing", 0, 1)

    log_message("\n📊 Hasil Akhir:", Fore.CYAN, log_callback)
    log_message(f"📝 Total file diproses   : {total_files}", Fore.CYAN, log_callback)
    log_message(f"📂 File hanya dipindahkan: {renamed_files}", Fore.BLUE, log_callback)
    log_message(f"✅ File yang digabung    : {merged_files}", Fore.GREEN, log_callback)
    log_message(f"❌ Total error           : {error_files}\n", Fore.RED, log_callback)
    log_message("✨ Selesai", Fore.GREEN, log_callback)

    if progress_callback:
        progress_callback("finalizing", 1, 1)

    return total_files, renamed_files, merged_files, error_files