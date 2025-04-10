class Theme:
    def __init__(self):
        # Definisi warna untuk tema dark
        self.dark = {
            "bg": "#333333",  # Background utama
            "fg": "#FFFFFF",  # Warna teks utama
            "entry_bg": "#555555",  # Background entry
            "entry_fg": "#FFFFFF",  # Warna teks entry
            "button_bg": "#0000FF",  # Warna tombol
            "button_fg": "#FFFFFF",  # Warna teks tombol
            "button_hover_bg": "#00008B",  # Warna tombol saat hover
            "listbox_bg": "#555555",  # Background listbox
            "listbox_fg": "#FFFFFF",  # Warna teks listbox
            "log_bg": "#555555",  # Background log text
            "log_fg": "#FFFFFF",  # Warna teks log
            "status_fg": "#FFFFFF",  # Warna teks status
        }

        # Definisi warna untuk tema light
        self.light = {
            "bg": "#F0F0F0",  # Background utama
            "fg": "#000000",  # Warna teks utama
            "entry_bg": "#E0E0E0",  # Background entry
            "entry_fg": "#000000",  # Warna teks entry
            "button_bg": "#0000FF",  # Warna tombol
            "button_fg": "#FFFFFF",  # Warna teks tombol
            "button_hover_bg": "#00008B",  # Warna tombol saat hover
            "listbox_bg": "#E0E0E0",  # Background listbox
            "listbox_fg": "#000000",  # Warna teks listbox
            "log_bg": "#E0E0E0",  # Background log text
            "log_fg": "#000000",  # Warna teks log
            "status_fg": "#000000",  # Warna teks status
        }

        # Font
        self.title_font = ("Helvetica", 24, "bold")
        self.label_font = ("Helvetica", 12)
        self.button_font = ("Helvetica", 12, "bold")
        self.listbox_font = ("Helvetica", 10)

    def get_colors(self, theme):
        """Mengembalikan warna berdasarkan tema yang dipilih."""
        if theme == "dark":
            return self.dark
        else:
            return self.light