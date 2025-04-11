import customtkinter as ctk
import os

class FileListComponent:
    def __init__(self, parent, colors, input_path_var):
        self.parent = parent
        self.colors = colors
        self.input_path_var = input_path_var
        self.file_labels = []

        # Total PDF Terdeteksi
        self.total_pdf_var = ctk.StringVar(value="Total PDF Terdeteksi: 0")
        self.total_pdf_label = ctk.CTkLabel(self.parent, textvariable=self.total_pdf_var,
                                            font=("Roboto", 12), text_color=self.colors["fg"])
        self.total_pdf_label.grid(row=6, column=0, columnspan=2, sticky="w", padx=10, pady=(10, 0))

        # Daftar File PDF (Pratinjau)
        ctk.CTkLabel(self.parent, text="Daftar File PDF:", font=("Roboto", 12),
                     text_color=self.colors["fg"]).grid(row=7, column=0, sticky="nw", padx=10, pady=(10, 0))
        self.file_frame = ctk.CTkScrollableFrame(self.parent, fg_color=self.colors["listbox_bg"],
                                                 height=200, corner_radius=10)
        self.file_frame.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=10, pady=(5, 10))

        # Bind input_path_var untuk update daftar file
        self.input_path_var.trace("w", self.update_file_list)

    def update_file_list(self, *args):
        folder = self.input_path_var.get()
        if folder and os.path.isdir(folder):
            pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]
            count = len(pdf_files)
            self.total_pdf_var.set(f"Total PDF Terdeteksi: {count}")
            for label in self.file_labels:
                label.destroy()
            self.file_labels.clear()
            for pdf_file in pdf_files:
                label = ctk.CTkLabel(self.file_frame, text=pdf_file, font=("Roboto", 10),
                                     text_color=self.colors["listbox_fg"])
                label.pack(anchor="w", padx=5, pady=2)
                self.file_labels.append(label)

    def update_theme(self, colors):
        self.colors = colors
        self.total_pdf_label.configure(text_color=self.colors["fg"])
        self.file_frame.configure(fg_color=self.colors["listbox_bg"])
        for child in self.parent.winfo_children():
            if isinstance(child, ctk.CTkLabel) and child != self.total_pdf_label:
                child.configure(text_color=self.colors["fg"])
        for label in self.file_labels:
            label.configure(text_color=self.colors["listbox_fg"])