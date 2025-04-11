import customtkinter as ctk

class ProgressBarComponent:
    def __init__(self, parent, colors):
        self.parent = parent
        self.colors = colors

        # Progress Bar dan Persentase
        ctk.CTkLabel(self.parent, text="Progress:", font=("Roboto", 12),
                     text_color=self.colors["fg"]).grid(row=10, column=0, sticky="w", padx=10, pady=(10, 0))
        self.progress_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.progress_frame.grid(row=11, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.progress_frame.grid_columnconfigure(0, weight=1)
        self.progress_var = ctk.DoubleVar(value=0.0)
        self.progress_bar = ctk.CTkProgressBar(self.progress_frame, variable=self.progress_var,
                                               progress_color="#22C55E", fg_color=self.colors["entry_bg"],
                                               height=20, width=600, corner_radius=10)  # Perpanjang progress bar
        self.progress_bar.grid(row=0, column=0, sticky="ew", padx=(0, 10))  # Memanjang dari kiri ke kanan
        self.progress_percentage_var = ctk.StringVar(value="0%")
        self.progress_percentage_label = ctk.CTkLabel(self.progress_frame, textvariable=self.progress_percentage_var,
                                                      font=("Roboto", 12, "bold"), text_color=self.colors["fg"])
        self.progress_percentage_label.grid(row=0, column=1)

    def update_theme(self, colors):
        self.colors = colors
        for child in self.parent.winfo_children():
            if isinstance(child, ctk.CTkLabel):
                child.configure(text_color=self.colors["fg"])
        self.progress_frame.configure(fg_color="transparent")
        self.progress_bar.configure(fg_color=self.colors["entry_bg"])
        # Atur warna teks persentase berdasarkan mode
        if self.colors["fg"] == "#000000":  # Mode light
            self.progress_percentage_label.configure(text_color="#333333")  # Abu-abu gelap untuk kontras
        else:  # Mode dark
            self.progress_percentage_label.configure(text_color=self.colors["fg"])