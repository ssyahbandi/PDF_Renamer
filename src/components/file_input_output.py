import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog

class FileInputOutputComponent:
    def __init__(self, parent, colors, input_path_var, output_path_var):
        self.parent = parent
        self.colors = colors
        self.input_path_var = input_path_var
        self.output_path_var = output_path_var

        # Input Folder
        ctk.CTkLabel(self.parent, text="Pilih Folder Input PDF:", font=("Roboto", 12),
                     text_color=self.colors["fg"]).grid(row=4, column=0, sticky="w", padx=10, pady=(10, 0))
        self.input_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.input_frame.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.input_frame.grid_columnconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(1, weight=0)
        self.input_entry = ctk.CTkEntry(self.input_frame, textvariable=self.input_path_var,
                                        height=35, fg_color=self.colors["entry_bg"],
                                        text_color=self.colors["entry_fg"], border_width=0,
                                        corner_radius=10, font=("Roboto", 12))
        self.input_entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        self.browse_input_btn = ctk.CTkButton(self.input_frame, text="Browse", command=self.browse_input,
                                              fg_color="#1E3A8A", text_color="#FFFFFF",
                                              font=("Roboto", 12, "bold"), hover_color="#3B82F6",
                                              width=120, height=35, border_width=0, corner_radius=15)
        self.browse_input_btn.grid(row=0, column=1)

        # Output Folder
        ctk.CTkLabel(self.parent, text="Pilih Folder Output PDF (Opsional):", font=("Roboto", 12),
                     text_color=self.colors["fg"]).grid(row=8, column=0, sticky="w", padx=10, pady=(10, 0))
        self.output_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.output_frame.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.output_frame.grid_columnconfigure(0, weight=1)
        self.output_entry = ctk.CTkEntry(self.output_frame, textvariable=self.output_path_var,
                                         height=35, fg_color=self.colors["entry_bg"],
                                         text_color=self.colors["entry_fg"], border_width=0,
                                         corner_radius=10, font=("Roboto", 12))
        self.output_entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        self.browse_output_btn = ctk.CTkButton(self.output_frame, text="Browse", command=self.browse_output,
                                               fg_color="#1E3A8A", text_color="#FFFFFF",
                                               font=("Roboto", 12, "bold"), hover_color="#3B82F6",
                                               width=120, height=35, border_width=0, corner_radius=15)
        self.browse_output_btn.grid(row=0, column=1)

    def browse_input(self):
        folder = filedialog.askdirectory(title="Pilih Folder PDF")
        if folder:
            self.input_path_var.set(folder)

    def browse_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_path_var.set(folder)

    def update_theme(self, colors):
        self.colors = colors
        for child in self.parent.winfo_children():
            if isinstance(child, ctk.CTkLabel) and child != self.parent.winfo_children()[0]:  # Skip title label
                child.configure(text_color=self.colors["fg"])
        self.input_frame.configure(fg_color="transparent")
        self.input_entry.configure(fg_color=self.colors["entry_bg"], text_color=self.colors["entry_fg"])
        self.browse_input_btn.configure(fg_color="#1E3A8A", text_color=self.colors["button_fg"], hover_color="#3B82F6")
        self.output_frame.configure(fg_color="transparent")
        self.output_entry.configure(fg_color=self.colors["entry_bg"], text_color=self.colors["entry_fg"])
        self.browse_output_btn.configure(fg_color="#1E3A8A", text_color=self.colors["button_fg"], hover_color="#3B82F6")