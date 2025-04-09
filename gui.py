# gui.py
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import webbrowser
from pdf_processor import process_pdfs
from styles import Theme

class RenamergedGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Renamerged - Rename & Merge PDFs")
        self.root.geometry("650x500")  # Tambah tinggi jendela dari 450 jadi 500
        self.root.resizable(False, False)

        # Inisialisasi tema
        self.theme = Theme()
        ctk.set_appearance_mode("dark")
        self.root.configure(bg=self.theme.bg)

        # Frame utama dengan scrollbar
        self.main_frame = ctk.CTkFrame(self.root, fg_color=self.theme.bg)
        self.main_frame.pack(fill="both", expand=True)

        # Label Judul
        ctk.CTkLabel(
            self.main_frame,
            text="Renamerged",
            font=self.theme.title_font,
            text_color=self.theme.fg
        ).pack(pady=10)

        # Frame untuk Input Path
        ctk.CTkLabel(
            self.main_frame,
            text="Pilih Folder PDF:",
            font=self.theme.label_font,
            text_color=self.theme.fg
        ).pack()
        self.input_path_var = tk.StringVar()
        input_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        input_frame.pack(fill="x", padx=10)
        self.input_entry = ctk.CTkEntry(
            input_frame,
            textvariable=self.input_path_var,
            width=500,
            height=30,
            fg_color=self.theme.entry_bg,
            text_color=self.theme.entry_fg,
            border_width=0,
            corner_radius=10
        )
        self.input_entry.pack(side="left", padx=5)
        self.browse_input_btn = ctk.CTkButton(
            input_frame,
            text="Browse",
            command=self.browse_input,
            fg_color=self.theme.button_bg,
            text_color=self.theme.button_fg,
            font=self.theme.button_font,
            hover_color=self.theme.button_hover_bg,
            width=100,
            height=30,
            border_width=0,
            corner_radius=10
        )
        self.browse_input_btn.pack(side="left")

        # Label Total PDF Terdeteksi
        self.total_pdf_var = tk.StringVar(value="Total PDF Terdeteksi: 0")
        ctk.CTkLabel(
            self.main_frame,
            textvariable=self.total_pdf_var,
            font=self.theme.label_font,
            text_color=self.theme.fg
        ).pack(pady=(5, 0))

        # Daftar File PDF (Listbox)
        ctk.CTkLabel(
            self.main_frame,
            text="File PDF di Folder:",
            font=self.theme.label_font,
            text_color=self.theme.fg
        ).pack(pady=(5, 0))
        self.pdf_listbox = tk.Listbox(
            self.main_frame,
            width=65,
            height=5,
            bg=self.theme.listbox_bg,
            fg=self.theme.listbox_fg,
            relief="flat",
            highlightthickness=0,
            borderwidth=2
        )
        self.pdf_listbox.pack(padx=10, pady=5)

        # Frame untuk Output Path
        ctk.CTkLabel(
            self.main_frame,
            text="Folder Output (opsional):",
            font=self.theme.label_font,
            text_color=self.theme.fg
        ).pack(pady=(5, 0))
        self.output_path_var = tk.StringVar()
        output_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        output_frame.pack(fill="x", padx=10)
        self.output_entry = ctk.CTkEntry(
            output_frame,
            textvariable=self.output_path_var,
            width=500,
            height=30,
            fg_color=self.theme.entry_bg,
            text_color=self.theme.entry_fg,
            border_width=0,
            corner_radius=10
        )
        self.output_entry.pack(side="left", padx=5)
        self.browse_output_btn = ctk.CTkButton(
            output_frame,
            text="Browse",
            command=self.browse_output,
            fg_color=self.theme.button_bg,
            text_color=self.theme.button_fg,
            font=self.theme.button_font,
            hover_color=self.theme.button_hover_bg,
            width=100,
            height=30,
            border_width=0,
            corner_radius=10
        )
        self.browse_output_btn.pack(side="left")

        # Label Loading
        ctk.CTkLabel(
            self.main_frame,
            text="Log Proses:",
            font=self.theme.label_font,
            text_color=self.theme.fg
        ).pack(pady=(5, 0))
        self.loading_var = tk.StringVar(value="")
        self.loading_label = ctk.CTkLabel(
            self.main_frame,
            textvariable=self.loading_var,
            font=self.theme.label_font,
            text_color="#00FF00"
        )
        self.loading_label.pack(pady=5)
        self.is_loading = False

        # Label Status
        self.status_var = tk.StringVar(value="Siap untuk memproses...")
        ctk.CTkLabel(
            self.main_frame,
            textvariable=self.status_var,
            font=self.theme.label_font,
            text_color=self.theme.status_fg,
            wraplength=600
        ).pack(pady=5)

        # Frame untuk Tombol
        button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        button_frame.pack(pady=20)  # Tambah padding supaya tombol terlihat

        # Tombol Process
        self.process_btn = ctk.CTkButton(
            button_frame,
            text="Process PDFs",
            command=self.process,
            fg_color=self.theme.button_bg,
            text_color=self.theme.button_fg,
            font=self.theme.button_font,
            hover_color=self.theme.button_hover_bg,
            width=150,
            height=40,
            border_width=0,
            corner_radius=10
        )
        self.process_btn.pack(side="left", padx=10)

        # Tombol Donasi
        self.donate_btn = ctk.CTkButton(
            button_frame,
            text="Donasi",
            command=self.open_donate_link,
            fg_color=self.theme.donate_bg,
            text_color=self.theme.button_fg,
            font=self.theme.button_font,
            hover_color=self.theme.donate_hover_bg,
            width=150,
            height=40,
            border_width=0,
            corner_radius=10
        )
        self.donate_btn.pack(side="left", padx=10)

    def open_donate_link(self):
        """Buka link donasi di browser."""
        webbrowser.open("https://bit.ly/kiyuris")

    def start_loading_animation(self):
        """Animasi loading dengan titik-titik bergerak."""
        if not self.is_loading:
            return
        dots = self.loading_var.get().count(".")
        if dots < 3:
            self.loading_var.set("Processing" + "." * (dots + 1))
        else:
            self.loading_var.set("Processing")
        self.root.after(500, self.start_loading_animation)

    def browse_input(self):
        folder = filedialog.askdirectory(title="Pilih Folder PDF")
        if folder:
            self.input_path_var.set(folder)
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, folder)
            # Tampilkan daftar file PDF di folder
            self.pdf_listbox.delete(0, tk.END)
            pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]
            if pdf_files:
                for pdf_file in pdf_files:
                    self.pdf_listbox.insert(tk.END, pdf_file)
                self.total_pdf_var.set(f"Total PDF Terdeteksi: {len(pdf_files)}")
            else:
                self.pdf_listbox.insert(tk.END, "Tidak ada file PDF di folder ini.")
                self.total_pdf_var.set("Total PDF Terdeteksi: 0")

    def browse_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_path_var.set(folder)
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, folder)

    def process(self):
        input_dir = self.input_path_var.get()
        output_dir = self.output_path_var.get()

        if not input_dir:
            messagebox.showerror("Error", "Silakan pilih folder input!")
            return

        if not os.path.isdir(input_dir):
            messagebox.showerror("Error", "Folder input tidak valid!")
            return

        # Validasi: pastikan ada file PDF di folder
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

        self.status_var.set("Processing...")
        self.is_loading = True
        self.start_loading_animation()
        self.root.update()

        try:
            total, renamed, merged, errors = process_pdfs(input_dir, output_dir)
            self.is_loading = False
            self.loading_var.set("")
            final_output_dir = output_dir if output_dir else os.path.join(input_dir, "ProcessedPDFs")
            self.status_var.set(f"Selesai! Total: {total}, Renamed: {renamed}, Merged: {merged}, Errors: {errors}\nDi ekstrak di: {final_output_dir}")
        except Exception as e:
            self.is_loading = False
            self.loading_var.set("")
            self.status_var.set("Error saat memproses!")
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

def run_gui():
    root = ctk.CTk()
    app = RenamergedGUI(root)
    root.mainloop()