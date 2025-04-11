import customtkinter as ctk
import threading
import os  # Tambahkan impor os
from tkinter import messagebox
from src.pdf_processor import process_pdfs as process_pdfs_merge
from src.pdf_processor_rename import process_pdfs as process_pdfs_rename

class ProcessButtonComponent:
    def __init__(self, parent, colors, input_path_var, output_path_var, mode_var, settings, progress_var, progress_percentage_var, stats_component, output_location_component):
        self.parent = parent
        self.colors = colors
        self.input_path_var = input_path_var
        self.output_path_var = output_path_var
        self.mode_var = mode_var
        self.settings = settings
        self.progress_var = progress_var
        self.progress_percentage_var = progress_percentage_var
        self.stats_component = stats_component
        self.output_location_component = output_location_component

        # Tombol Proses
        self.process_btn = ctk.CTkButton(self.parent, text="Proses", command=self.process,
                                         fg_color="#1E3A8A", text_color="#FFFFFF",
                                         font=("Roboto", 12, "bold"), hover_color="#3B82F6",
                                         width=120, height=40, border_width=0, corner_radius=15)
        self.process_btn.grid(row=14, column=0, columnspan=2, pady=20)

    def process(self):
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
        self.stats_component.reset_stats()

        def run_process():
            weight_reading = 0.40
            weight_processing = 0.50
            weight_finalizing = 0.10

            current_progress = 0.0

            def progress_callback(stage, processed, total):
                nonlocal current_progress
                if stage == "reading":
                    current_progress = weight_reading * (processed / total)
                elif stage == "processing":
                    current_progress = weight_reading + weight_processing * (processed / total)
                elif stage == "finalizing":
                    current_progress = weight_reading + weight_processing + weight_finalizing * (processed / total if total > 0 else 1.0)

                self.progress_var.set(current_progress)
                self.progress_percentage_var.set(f"{int(current_progress * 100)}%")
                self.parent.update_idletasks()

            # Siapkan pengaturan dengan nilai boolean biasa
            processed_settings = {
                "mode": self.mode_var.get(),
                "use_name": self.settings["use_name"].get(),
                "use_date": self.settings["use_date"].get(),
                "use_reference": self.settings["use_reference"].get(),
                "use_faktur": self.settings["use_faktur"].get()
            }

            # Pilih fungsi pemrosesan berdasarkan mode
            if self.mode_var.get() == "Rename Saja":
                process_func = process_pdfs_rename
            else:
                process_func = process_pdfs_merge

            total, renamed, merged, errors = process_func(input_dir, output_dir, progress_callback, None, processed_settings)

            self.stats_component.update_stats(total, renamed, merged, errors)

            if output_dir and output_dir.strip() != "":
                final_output_path = output_dir
            else:
                final_output_path = os.path.join(input_dir, "ProcessedPDFs")
            self.output_location_component.set_output_path(final_output_path)

            self.process_btn.configure(state="normal")

        threading.Thread(target=run_process).start()

    def update_theme(self, colors):
        self.colors = colors
        self.process_btn.configure(fg_color="#1E3A8A", text_color=self.colors["button_fg"], hover_color="#3B82F6")