# src/styles.py
class Theme:
    def __init__(self):
        # Warna sesuai deskripsi
        self.bg = "#333333"  # Latar belakang abu-abu gelap
        self.fg = "#FFFFFF"  # Teks putih
        self.entry_bg = "#555555"  # Latar kolom teks abu-abu terang
        self.entry_fg = "#FFFFFF"  # Teks kolom teks putih
        self.button_bg = "#000000"  # Tombol Browse hitam
        self.button_fg = "#FFFFFF"  # Teks tombol Browse putih
        self.button_hover_bg = "#222222"  # Hover tombol Browse
        self.action_button_bg = "#FF69B4"  # Tombol aksi pink
        self.action_button_fg = "#FFFFFF"  # Teks tombol aksi putih
        self.action_button_hover_bg = "#FF85C2"  # Hover tombol aksi
        self.progress_fg = "#00FF00"  # Progress bar hijau
        self.progress_bg = "#555555"  # Latar progress bar
        self.stats_fg = "#FF0000"  # Teks statistik merah

        # Font
        self.title_font = ("Helvetica", 24, "bold")  # Judul besar dan tebal
        self.label_font = ("Helvetica", 12)  # Label biasa
        self.button_font = ("Helvetica", 12, "bold")  # Tombol tebal