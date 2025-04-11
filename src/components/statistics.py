import customtkinter as ctk

class StatisticsComponent:
    def __init__(self, parent, colors):
        self.parent = parent
        self.colors = colors

        # Statistik
        self.stats_frame = ctk.CTkFrame(self.parent, fg_color=self.colors["entry_bg"], corner_radius=10)
        self.stats_frame.grid(row=12, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 0))
        self.stats_vars = {
            "total": ctk.StringVar(value="Total diproses: 0"),
            "moved": ctk.StringVar(value="Total File yang hanya dipindahkan: 0"),
            "merged": ctk.StringVar(value="Total File yang digabung: 0"),
            "error": ctk.StringVar(value="Total File yang Error: 0")
        }
        for i, var in enumerate(self.stats_vars.values(), start=0):
            ctk.CTkLabel(self.stats_frame, textvariable=var, font=("Roboto", 12),
                         text_color=self.colors["fg"]).grid(row=i, column=0, sticky="w", padx=10, pady=2)  # Kurangi pady dari 5 ke 2

    def update_stats(self, total, renamed, merged, errors):
        self.stats_vars["total"].set(f"Total diproses: {total}")
        self.stats_vars["moved"].set(f"Total File yang hanya dipindahkan: {renamed}")
        self.stats_vars["merged"].set(f"Total File yang digabung: {merged}")
        self.stats_vars["error"].set(f"Total File yang Error: {errors}")

    def reset_stats(self):
        for var in self.stats_vars.values():
            var.set(var.get().split(":")[0] + ": 0")

    def update_theme(self, colors):
        self.colors = colors
        self.stats_frame.configure(fg_color=self.colors["entry_bg"])
        for child in self.stats_frame.winfo_children():
            child.configure(text_color=self.colors["fg"])