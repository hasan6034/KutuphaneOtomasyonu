import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import Fonksiyonlar.GenelFonksiyonlar as gf
import Fonksiyonlar.Veritabani as vt

class KitapGeciktirenler(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.setup_ui()
        self.populate_treeview()

    def setup_ui(self):
        gf.CenterWindow(self, 1000, 700)
        self.title("Kitabını Geciktirenler")

        grid = ctk.CTkFrame(self)
        grid.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        columns = ("UyeAdi", "Telefon", "Adres", "KitapAdi", "OduncTarihi", "GecikmeSuresi")
        self.tw_Geciktirenler = ttk.Treeview(self, columns=columns, show="headings")

        headings = {
            "UyeAdi": "Üye Adı",
            "Telefon": "Telefon",
            "Adres": "Adres",
            "KitapAdi": "Kitap Adı",
            "OduncTarihi": "Ödünç Tarihi",
            "GecikmeSuresi": "Gecikme Süresi"
        }

        for col, heading in headings.items():
            self.tw_Geciktirenler.heading(col, text=heading)

        column_widths = {
            "UyeAdi": 150,
            "Telefon": 90,
            "Adres": 200,
            "KitapAdi": 150,
            "OduncTarihi": 90,
            "GecikmeSuresi": 80
        }

        for col, width in column_widths.items():
            self.tw_Geciktirenler.column(col, width=width)

        self.tw_Geciktirenler.grid(row=0, column=0, sticky="nsew")

    def populate_treeview(self):
        try:
            self.tw_Geciktirenler.delete(*self.tw_Geciktirenler.get_children())
            data = vt.KitapGeciktirenlerListesi()
            gf.PopulateTreeview(self.tw_Geciktirenler, data)
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Kitap geciktirenler listesi alınırken hata oluştu:\n{str(e)}")
