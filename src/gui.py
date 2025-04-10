import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox, StringVar, DoubleVar
import os
import webbrowser
import threading
from src.pdf_processor import process_pdfs

class RenamergedGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RENAMERGED - Rename & Merge PDFs")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.minsize(700, 600)

        # Pengaturan tema
        ctk.set_appearance_mode("dark")
        self.root.configure(bg="#333333")

        # Frame utama
        self.main_frame = ctk.CTkFrame(self.root, fg_color="#333333")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Konfigurasi grid untuk layout
        self.main_frame.grid_rowconfigure(0, weight=0)  # Baris judul dan tombol donasi
        self.main_frame.grid_rowconfigure(1, weight=0)  # Baris label input
        self.main_frame.grid_rowconfigure(2, weight=0)  # Baris entry input
        self.main_frame.grid_rowconfigure(3, weight=0)  # Baris total PDF
        self.main_frame.grid_rowconfigure(4, weight=0)  # Baris label output
        self.main_frame.grid_rowconfigure(5, weight=0)  # Baris entry output
        self.main_frame.grid_rowconfigure(6, weight=0)  # Baris label progress
        self.main_frame.grid_rowconfigure(7, weight=0)  # Baris progress bar
        self.main_frame.grid_rowconfigure(8, weight=0)  # Baris statistik
        self.main_frame.grid_rowconfigure(13, weight=1)  # Baris tombol proses
        self.main_frame.grid_columnconfigure(0, weight=1)  # Kolom utama
        self.main_frame.grid_columnconfigure(1, weight=0)  # Kolom tombol

        # Judul
        ctk.CTkLabel(self.main_frame, text="RENAMERGED", font=("Helvetica", 24, "bold"),
                     text_color="#FFFFFF").grid(row=0, column=0, sticky="w", padx=10, pady=10)

        # Tombol Donasi (pojok kanan atas)
        self.donate_btn = ctk.CTkButton(self.main_frame, text="Donasi", command=self.open_donate_link,
                                        fg_color="#0000FF", text_color="#FFFFFF",
                                        font=("Helvetica", 12, "bold"), hover_color="#00008B",
                                        width=100, height=30, border_width=0, corner_radius=10)
        self.donate_btn.grid(row=0, column=1, sticky="e", padx=10, pady=10)

        # Input Folder
        ctk.CTkLabel(self.main_frame, text="Pilih Folder Input PDF:", font=("Helvetica", 12),
                     text_color="#FFFFFF").grid(row=1, column=0, sticky="w", padx=10, pady=(10, 0))
        input_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        input_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        input_frame.grid_columnconfigure(0, weight=1)
        self.input_path_var = StringVar()
        self.input_entry = ctk.CTkEntry(input_frame, textvariable=self.input_path_var,
                                        height=30, fg_color="#555555",
                                        text_color="#FFFFFF", border_width=0,
                                        corner_radius=10)
        self.input_entry.grid(row=0, column=0, sticky="ew", padx=5)
        self.browse_input_btn = ctk.CTkButton(input_frame, text="Browse", command=self.browse_input,
                                              fg_color="#000000", text_color="#FFFFFF",
                                              font=("Helvetica", 12, "bold"), hover_color="#222222",
                                              width=100, height=30, border_width=0, corner_radius=10)
        self.browse_input_btn.grid(row=0, column=1, padx=5)

        # Total PDF Terdeteksi
        self.total_pdf_var = StringVar(value="Total PDF Terdeteksi: 0")
        self.total_pdf_label = ctk.CTkLabel(self.main_frame, textvariable=self.total_pdf_var,
                                            font=("Helvetica", 12, "bold"), text_color="#FFFFFF")
        self.total_pdf_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=(10, 0))

        # Output Folder
        ctk.CTkLabel(self.main_frame, text="Pilih Folder Output PDF (Opsional):", font=("Helvetica", 12),
                     text_color="#FFFFFF").grid(row=4, column=0, sticky="w", padx=10, pady=(10, 0))
        output_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        output_frame.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        output_frame.grid_columnconfigure(0, weight=1)
        self.output_path_var = StringVar()
        self.output_entry = ctk.CTkEntry(output_frame, textvariable=self.output_path_var,
                                         height=30, fg_color="#555555",
                                         text_color="#FFFFFF", border_width=0,
                                         corner_radius=10)
        self.output_entry.grid(row=0, column=0, sticky="ew", padx=5)
        self.browse_output_btn = ctk.CTkButton(output_frame, text="Browse", command=self.browse_output,
                                               fg_color="#000000", text_color="#FFFFFF",
                                               font=("Helvetica", 12, "bold"), hover_color="#222222",
                                               width=100, height=30, border_width=0, corner_radius=10)
        self.browse_output_btn.grid(row=0, column=1, padx=5)

        # Progress Bar
        ctk.CTkLabel(self.main_frame, text="Progress:", font=("Helvetica", 12),
                     text_color="#FFFFFF").grid(row=6, column=0, sticky="w", padx=10, pady=(10, 0))
        self.progress_var = DoubleVar(value=0.0)
        self.progress_bar = ctk.CTkProgressBar(self.main_frame, variable=self.progress_var,
                                               progress_color="#00FF00", fg_color="#555555",
                                               height=20, width=500)
        self.progress_bar.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
        self.progress_percentage_var = StringVar(value="0%")
        self.progress_percentage_label = ctk.CTkLabel(self.main_frame, textvariable=self.progress_percentage_var,
                                                      font=("Helvetica", 12), text_color="#FFFFFF")
        self.progress_percentage_label.grid(row=7, column=1, sticky="e", padx=10)

        # Statistik
        self.stats_vars = {
            "total": StringVar(value="Total diproses: 0"),
            "moved": StringVar(value="Total File yang hanya dipindahkan: 0"),
            "merged": StringVar(value="Total File yang digabung: 0"),
            "error": StringVar(value="Total File yang Error: 0")
        }
        for i, var in enumerate(self.stats_vars.values(), start=8):
            ctk.CTkLabel(self.main_frame, textvariable=var, font=("Helvetica", 12, "bold"),
                         text_color="#FFFFFF").grid(row=i, column=0, columnspan=2, sticky="w", padx=10, pady=2)

        # Lokasi Output
        self.output_location_var = StringVar(value="Hasil disimpan di: -")
        self.output_location_label = ctk.CTkLabel(self.main_frame, textvariable=self.output_location_var,
                                                  font=("Helvetica", 12), text_color="#FFFFFF")
        self.output_location_label.grid(row=12, column=0, columnspan=2, sticky="w", padx=10, pady=(10, 0))

        # Tombol Proses (warna biru)
        self.process_btn = ctk.CTkButton(self.main_frame, text="Proses", command=self.process,
                                         fg_color="#0000FF", text_color="#FFFFFF",
                                         font=("Helvetica", 12, "bold"), hover_color="#00008B",
                                         width=150, height=40, border_width=0, corner_radius=10)
        self.process_btn.grid(row=13, column=0, columnspan=2, pady=20)

    def open_donate_link(self):
        """Membuka link donasi di browser."""
        webbrowser.open("https://bit.ly/kiyuris")  # Ganti dengan link donasi Anda

    def browse_input(self):
        """Memilih folder input dan menghitung jumlah PDF."""
        folder = filedialog.askdirectory(title="Pilih Folder PDF")
        if folder:
            self.input_path_var.set(folder)
            pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]
            count = len(pdf_files)
            self.total_pdf_var.set(f"Total PDF Terdeteksi: {count}")

    def browse_output(self):
        """Memilih folder output."""
        folder = filedialog.askdirectory()
        if folder:
            self.output_path_var.set(folder)

    def process(self):
        """Memproses file PDF di thread terpisah dengan progress bar dinamis."""
        input_dir = self.input_path_var.get()
        output_dir = self.output_path_var.get()

        if not input_dir:
            messagebox.showerror("Error", "Silakan pilih folder input!")
            return

        if not os.path.isdir(input_dir):
            messagebox.showerror("Error", "Folder input tidak valid!")
            return

        pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
        if not pdf_files:
            messagebox.showerror("Error", "Folder yang dipilih tidak berisi file PDF!")
            return

        if output_dir and not os.path.isdir(output_dir):
            try:
                os.makedirs(output_dir, exist_ok=True)
            except Exception as e:
                messagebox.showerror("Error", f"Gagal membuat folder output: {str(e)}")
                return

        self.process_btn.configure(state="disabled")
        self.progress_var.set(0.0)
        self.progress_percentage_var.set("0%")
        for var in self.stats_vars.values():
            var.set(var.get().split(":")[0] + ": 0")

        def run_process():
            # Bobot untuk setiap tahap (tanpa counting)
            weight_reading = 0.40   # 40%
            weight_processing = 0.50  # 50%
            weight_finalizing = 0.10  # 10%

            # Variabel untuk melacak progress keseluruhan
            current_progress = 0.0

            def progress_callback(stage, processed, total):
                nonlocal current_progress
                if stage == "reading":
                    # Tahap 1: Pembacaan dan pengelompokan (40%)
                    current_progress = weight_reading * (processed / total)
                elif stage == "processing":
                    # Tahap 2: Pemrosesan (rename/merge) (50%)
                    current_progress = weight_reading + weight_processing * (processed / total)
                elif stage == "finalizing":
                    # Tahap 3: Finalisasi (10%)
                    current_progress = weight_reading + weight_processing + weight_finalizing * (processed / total if total > 0 else 1.0)

                # Update progress bar
                self.progress_var.set(current_progress)
                self.progress_percentage_var.set(f"{int(current_progress * 100)}%")
                self.root.update_idletasks()

            # Jalankan process_pdfs dengan callback
            total, renamed, merged, errors = process_pdfs(input_dir, output_dir, progress_callback)
            
            # Update statistik setelah selesai
            self.stats_vars["total"].set(f"Total diproses: {total}")
            self.stats_vars["moved"].set(f"Total File yang hanya dipindahkan: {renamed}")
            self.stats_vars["merged"].set(f"Total File yang digabung: {merged}")
            self.stats_vars["error"].set(f"Total File yang Error: {errors}")

            # Update lokasi output
            if output_dir and output_dir.strip() != "":
                final_output_path = output_dir
            else:
                final_output_path = os.path.join(input_dir, "ProcessedPDFs")
            self.output_location_var.set(f"Hasil disimpan di: {final_output_path}")

            self.process_btn.configure(state="normal")

        threading.Thread(target=run_process).start()

def run_gui():
    """Menjalankan aplikasi GUI."""
    root = ctk.CTk()
    app = RenamergedGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()