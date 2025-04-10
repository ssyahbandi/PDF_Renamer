# styles.py
class Theme:
    def __init__(self):
        # Warna tema gelap modern dengan aksen neon
        self.bg = "#1E1E2F"  # Background utama (gelap)
        self.fg = "#E0E0E0"  # Warna teks (abu-abu terang)
        self.entry_bg = "#4A90E2"  # Background entry (biru muda)
        self.entry_fg = "#000000"  # Warna teks entry (hitam untuk kontras)
        self.button_bg = "#00C4B4"  # Warna tombol (hijau neon)
        self.button_fg = "#FFFFFF"  # Warna teks tombol (putih)
        self.button_hover_bg = "#00E5CC"  # Warna tombol saat hover (hijau neon lebih terang)
        self.listbox_bg = "#2D2D44"  # Background listbox
        self.listbox_fg = "#E0E0E0"  # Warna teks listbox
        self.status_fg = "#00C4B4"  # Warna teks status (hijau neon)
        self.donate_bg = "#FF6F61"  # Warna tombol donasi (oranye kemerahan)
        self.donate_hover_bg = "#FF8A80"  # Warna tombol donasi saat hover

        # Font modern dengan ukuran lebih besar
        self.title_font = ("Helvetica", 20, "bold")  # Ukuran lebih besar
        self.label_font = ("Helvetica", 12)  # Ukuran lebih besar
        self.button_font = ("Helvetica", 12, "bold")  # Ukuran lebih besar