import customtkinter as ctk
import tkinter as tk

class ModeSelectionComponent:
    def __init__(self, parent, colors, mode_var, settings):
        self.parent = parent
        self.colors = colors
        self.mode_var = mode_var
        self.settings = settings

        # Pemilihan Mode
        self.mode_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.mode_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))
        ctk.CTkLabel(self.mode_frame, text="Mode Pemrosesan:", font=("Roboto", 12),
                     text_color=self.colors["fg"]).pack(side="left", padx=(0, 10))
        self.mode_menu = ctk.CTkOptionMenu(self.mode_frame, values=["Rename Saja", "Rename dan Merge"],
                                           variable=self.mode_var, command=self.toggle_mode_options,
                                           fg_color="#1E3A8A", text_color="#FFFFFF",
                                           font=("Roboto", 12), width=150, height=35, corner_radius=15)
        self.mode_menu.pack(side="left")

        # Frame untuk opsi komponen nama file (hanya muncul pada mode Rename Saja)
        self.name_components_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.name_components_frame.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))
        ctk.CTkLabel(self.name_components_frame, text="Komponen Nama File (untuk Rename Saja):", font=("Roboto", 12),
                     text_color=self.colors["fg"]).grid(row=0, column=0, sticky="w", padx=(0, 10))
        self.name_check = ctk.CTkCheckBox(self.name_components_frame, text="Nama Lawan Transaksi",
                                          variable=self.settings["use_name"], font=("Roboto", 12),  # Font diperbesar
                                          checkbox_width=20, checkbox_height=20, width=90)  # Kurangi ukuran kotak
        self.name_check.grid(row=0, column=1, padx=2)
        self.date_check = ctk.CTkCheckBox(self.name_components_frame, text="Tanggal Faktur Pajak",
                                          variable=self.settings["use_date"], font=("Roboto", 12),  # Font diperbesar
                                          checkbox_width=20, checkbox_height=20, width=90)  # Kurangi ukuran kotak
        self.date_check.grid(row=0, column=2, padx=2)
        self.ref_check = ctk.CTkCheckBox(self.name_components_frame, text="Referensi",
                                         variable=self.settings["use_reference"], font=("Roboto", 12),  # Font diperbesar
                                         checkbox_width=20, checkbox_height=20, width=70)  # Kurangi ukuran kotak
        self.ref_check.grid(row=0, column=3, padx=2)
        self.faktur_check = ctk.CTkCheckBox(self.name_components_frame, text="Nomor Faktur Pajak",
                                            variable=self.settings["use_faktur"], font=("Roboto", 12),  # Font diperbesar
                                            checkbox_width=20, checkbox_height=20, width=90)  # Kurangi ukuran kotak
        self.faktur_check.grid(row=0, column=4, padx=2)
        self.toggle_mode_options(self.mode_var.get())  # Inisialisasi visibilitas

    def toggle_mode_options(self, mode):
        """Menampilkan atau menyembunyikan opsi komponen nama file berdasarkan mode."""
        if mode == "Rename Saja":
            self.name_components_frame.grid()
        else:
            self.name_components_frame.grid_remove()

    def update_theme(self, colors):
        self.colors = colors
        for child in self.mode_frame.winfo_children():
            if isinstance(child, ctk.CTkLabel):
                child.configure(text_color=self.colors["fg"])
        self.mode_menu.configure(fg_color="#1E3A8A", text_color="#FFFFFF")
        for child in self.name_components_frame.winfo_children():
            if isinstance(child, ctk.CTkLabel):
                child.configure(text_color=self.colors["fg"])