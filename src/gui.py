import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox, StringVar, DoubleVar
import os
import webbrowser
import threading
from src.pdf_processor import process_pdfs
from src.styles import Theme

class RenamergedGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RENAMERGED - Rename & Merge PDFs")
        self.root.geometry("700x800")
        self.root.resizable(True, True)
        self.root.minsize(700, 800)

        # Inisialisasi tema
        self.theme = Theme()
        self.current_theme = "dark"
        ctk.set_appearance_mode(self.current_theme)
        self.colors = self.theme.get_colors(self.current_theme)
        self.root.configure(bg=self.colors["bg"])

        # Frame utama
        self.main_frame = ctk.CTkFrame(self.root, fg_color=self.colors["bg"])
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Konfigurasi grid untuk layout
        self.main_frame.grid_rowconfigure(0, weight=0)  # Baris judul dan tombol donasi/tema
        self.main_frame.grid_rowconfigure(1, weight=0)  # Baris label input
        self.main_frame.grid_rowconfigure(2, weight=0)  # Baris entry input dan tombol browse
        self.main_frame.grid_rowconfigure(3, weight=0)  # Baris total PDF
        self.main_frame.grid_rowconfigure(4, weight=2)  # Baris listbox (pratinjau file, diperbesar)
        self.main_frame.grid_rowconfigure(5, weight=0)  # Baris label output
        self.main_frame.grid_rowconfigure(6, weight=0)  # Baris entry output
        self.main_frame.grid_rowconfigure(7, weight=0)  # Baris label progress
        self.main_frame.grid_rowconfigure(8, weight=0)  # Baris progress bar dan persentase
        self.main_frame.grid_rowconfigure(9, weight=0)  # Baris statistik
        self.main_frame.grid_rowconfigure(14, weight=0)  # Baris tombol proses
        self.main_frame.grid_columnconfigure(0, weight=1)  # Kolom utama
        self.main_frame.grid_columnconfigure(1, weight=0)  # Kolom untuk frame tombol donasi/tema

        # Judul
        self.title_label = ctk.CTkLabel(self.main_frame, text="RENAMERGED", font=self.theme.title_font,
                                        text_color=self.colors["fg"])
        self.title_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        # Frame untuk tombol Donasi dan Ganti Tema (di baris judul, sisi kanan)
        top_button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        top_button_frame.grid(row=0, column=1, sticky="e")
        top_button_frame.grid_columnconfigure(0, weight=0)
        top_button_frame.grid_columnconfigure(1, weight=0)

        # Tombol Donasi (di top_button_frame, kolom 0)
        self.donate_btn = ctk.CTkButton(top_button_frame, text="Donasi", command=self.open_donate_link,
                                        fg_color="#4A90E2", text_color="#FFFFFF",
                                        font=self.theme.button_font, hover_color="#357ABD",
                                        width=100, height=30, border_width=0, corner_radius=10)
        self.donate_btn.grid(row=0, column=0, padx=5, pady=10)

        # Tombol Ganti Tema (di top_button_frame, kolom 1)
        self.theme_btn = ctk.CTkButton(top_button_frame, text="Ganti Tema", command=self.toggle_theme,
                                       fg_color="#4A90E2", text_color="#FFFFFF",
                                       font=self.theme.button_font, hover_color="#357ABD",
                                       width=100, height=30, border_width=0, corner_radius=10)
        self.theme_btn.grid(row=0, column=1, padx=5, pady=10)

        # Input Folder
        ctk.CTkLabel(self.main_frame, text="Pilih Folder Input PDF:", font=self.theme.label_font,
                     text_color=self.colors["fg"]).grid(row=1, column=0, sticky="w", padx=10, pady=(10, 0))
        input_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        input_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        input_frame.grid_columnconfigure(0, weight=1)
        input_frame.grid_columnconfigure(1, weight=0)
        input_frame.grid_columnconfigure(2, weight=0)
        self.input_path_var = StringVar()
        self.input_entry = ctk.CTkEntry(input_frame, textvariable=self.input_path_var,
                                        height=30, fg_color=self.colors["entry_bg"],
                                        text_color=self.colors["entry_fg"], border_width=0,
                                        corner_radius=10)
        self.input_entry.grid(row=0, column=0, sticky="ew", padx=5)
        self.browse_input_btn = ctk.CTkButton(input_frame, text="Browse", command=self.browse_input,
                                              fg_color="#4A90E2", text_color="#FFFFFF",
                                              font=self.theme.button_font, hover_color="#357ABD",
                                              width=100, height=30, border_width=0, corner_radius=10)
        self.browse_input_btn.grid(row=0, column=1, padx=5)

        # Total PDF Terdeteksi
        self.total_pdf_var = StringVar(value="Total PDF Terdeteksi: 0")
        self.total_pdf_label = ctk.CTkLabel(self.main_frame, textvariable=self.total_pdf_var,
                                            font=self.theme.label_font, text_color=self.colors["fg"])
        self.total_pdf_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=(10, 0))

        # Daftar File PDF (Pratinjau)
        ctk.CTkLabel(self.main_frame, text="Daftar File PDF:", font=self.theme.label_font,
                     text_color=self.colors["fg"]).grid(row=4, column=0, sticky="nw", padx=10, pady=(10, 0))
        self.file_listbox = tk.Listbox(self.main_frame, height=12, bg=self.colors["listbox_bg"], fg=self.colors["listbox_fg"],
                                       font=self.theme.listbox_font, relief="flat", highlightthickness=0)
        self.file_listbox.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=10, pady=(5, 10))

        # Output Folder
        ctk.CTkLabel(self.main_frame, text="Pilih Folder Output PDF (Opsional):", font=self.theme.label_font,
                     text_color=self.colors["fg"]).grid(row=5, column=0, sticky="w", padx=10, pady=(10, 0))
        output_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        output_frame.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        output_frame.grid_columnconfigure(0, weight=1)
        self.output_path_var = StringVar()
        self.output_entry = ctk.CTkEntry(output_frame, textvariable=self.output_path_var,
                                         height=30, fg_color=self.colors["entry_bg"],
                                         text_color=self.colors["entry_fg"], border_width=0,
                                         corner_radius=10)
        self.output_entry.grid(row=0, column=0, sticky="ew", padx=5)
        self.browse_output_btn = ctk.CTkButton(output_frame, text="Browse", command=self.browse_output,
                                               fg_color="#4A90E2", text_color="#FFFFFF",
                                               font=self.theme.button_font, hover_color="#357ABD",
                                               width=100, height=30, border_width=0, corner_radius=10)
        self.browse_output_btn.grid(row=0, column=1, padx=5)

        # Progress Bar dan Persentase
        ctk.CTkLabel(self.main_frame, text="Progress:", font=self.theme.label_font,
                     text_color=self.colors["fg"]).grid(row=7, column=0, sticky="w", padx=10, pady=(10, 0))
        progress_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        progress_frame.grid(row=8, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.progress_var = DoubleVar(value=0.0)
        self.progress_bar = ctk.CTkProgressBar(progress_frame, variable=self.progress_var,
                                               progress_color="#00FF00", fg_color=self.colors["entry_bg"],
                                               height=20, width=500)
        self.progress_bar.grid(row=0, column=0, padx=(0, 10))
        self.progress_percentage_var = StringVar(value="0%")
        self.progress_percentage_label = ctk.CTkLabel(progress_frame, textvariable=self.progress_percentage_var,
                                                      font=self.theme.label_font, text_color=self.colors["fg"])
        self.progress_percentage_label.grid(row=0, column=1)

        # Statistik
        self.stats_vars = {
            "total": StringVar(value="Total diproses: 0"),
            "moved": StringVar(value="Total File yang hanya dipindahkan: 0"),
            "merged": StringVar(value="Total File yang digabung: 0"),
            "error": StringVar(value="Total File yang Error: 0")
        }
        for i, var in enumerate(self.stats_vars.values(), start=9):
            ctk.CTkLabel(self.main_frame, textvariable=var, font=self.theme.label_font,
                         text_color=self.colors["fg"]).grid(row=i, column=0, columnspan=2, sticky="w", padx=10, pady=2)

        # Lokasi Output
        self.output_location_var = StringVar(value="Hasil disimpan di: -")
        self.output_location_label = ctk.CTkLabel(self.main_frame, textvariable=self.output_location_var,
                                                  font=self.theme.label_font, text_color=self.colors["fg"],
                                                  wraplength=600)
        self.output_location_label.grid(row=13, column=0, sticky="w", padx=10, pady=(10, 0))

        # Tombol Buka Folder Hasil (dipindah ke kanan)
        self.open_output_btn = ctk.CTkButton(self.main_frame, text="Buka Folder Hasil", command=self.open_output_folder,
                                             fg_color="#4A90E2", text_color="#FFFFFF",
                                             font=self.theme.button_font, hover_color="#357ABD",
                                             width=150, height=30, border_width=0, corner_radius=10)
        self.open_output_btn.grid(row=13, column=1, sticky="e", padx=10, pady=(10, 0))

        # Tombol Proses
        self.process_btn = ctk.CTkButton(self.main_frame, text="Proses", command=self.process,
                                         fg_color="#4A90E2", text_color="#FFFFFF",
                                         font=self.theme.button_font, hover_color="#357ABD",
                                         width=150, height=40, border_width=0, corner_radius=10)
        self.process_btn.grid(row=14, column=0, columnspan=2, pady=20)

    def toggle_theme(self):
        """Mengganti tema antara dark dan light mode."""
        if self.current_theme == "dark":
            self.current_theme = "light"
        else:
            self.current_theme = "dark"
        ctk.set_appearance_mode(self.current_theme)
        self.colors = self.theme.get_colors(self.current_theme)
        self.root.configure(bg=self.colors["bg"])
        self.main_frame.configure(fg_color=self.colors["bg"])
        self.title_label.configure(text_color=self.colors["fg"])
        self.total_pdf_label.configure(text_color=self.colors["fg"])
        self.output_location_label.configure(text_color=self.colors["fg"])
        self.file_listbox.configure(bg=self.colors["listbox_bg"], fg=self.colors["listbox_fg"])
        self.input_entry.configure(fg_color=self.colors["entry_bg"], text_color=self.colors["entry_fg"])
        self.output_entry.configure(fg_color=self.colors["entry_bg"], text_color=self.colors["entry_fg"])
        self.browse_input_btn.configure(fg_color="#4A90E2", text_color=self.colors["button_fg"],
                                       hover_color="#357ABD")
        self.browse_output_btn.configure(fg_color="#4A90E2", text_color=self.colors["button_fg"],
                                        hover_color="#357ABD")
        self.donate_btn.configure(fg_color="#4A90E2", text_color=self.colors["button_fg"],
                                 hover_color="#357ABD")
        self.theme_btn.configure(fg_color="#4A90E2", text_color=self.colors["button_fg"],
                                hover_color="#357ABD")
        self.open_output_btn.configure(fg_color="#4A90E2", text_color=self.colors["button_fg"],
                                      hover_color="#357ABD")
        self.process_btn.configure(fg_color="#4A90E2", text_color=self.colors["button_fg"],
                                  hover_color="#357ABD")
        for child in self.main_frame.winfo_children():
            if isinstance(child, ctk.CTkLabel) and child != self.title_label and child != self.total_pdf_label and child != self.output_location_label:
                child.configure(text_color=self.colors["fg"])

    def open_donate_link(self):
        """Membuka link donasi di browser."""
        webbrowser.open("https://bit.ly/kiyuris")  # Ganti dengan link donasi Anda

    def open_output_folder(self):
        """Membuka folder hasil pemrosesan."""
        output_path = self.output_location_var.get().replace("Hasil disimpan di: ", "")
        if os.path.isdir(output_path):
            os.startfile(output_path)  # Untuk Windows
            # Untuk macOS/Linux, gunakan: subprocess.run(['open', output_path])
        else:
            messagebox.showerror("Error", "Folder tidak ditemukan!")

    def browse_input(self):
        """Memilih folder input dan menghitung jumlah PDF."""
        folder = filedialog.askdirectory(title="Pilih Folder PDF")
        if folder:
            self.input_path_var.set(folder)
            pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]
            count = len(pdf_files)
            self.total_pdf_var.set(f"Total PDF Terdeteksi: {count}")
            # Update pratinjau file PDF di listbox
            self.file_listbox.delete(0, tk.END)
            for pdf_file in pdf_files:
                self.file_listbox.insert(tk.END, pdf_file)

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
            total, renamed, merged, errors = process_pdfs(input_dir, output_dir, progress_callback, None)
            
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