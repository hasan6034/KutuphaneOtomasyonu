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
        ctk.set_default_color_theme("green")
        gf.CenterWindow(self, 1000, 700)
        self.title("Kitabını Geciktirenler")

        grid = ctk.CTkFrame(self)
        grid.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tw_Geciktirenler = ttk.Treeview(
            self,
            columns=("UyeAdi", "Telefon", "Adres", "KitapAdi", "OduncTarihi", "GecikmeSuresi"),
            show="headings",
        )

        self.tw_Geciktirenler.heading("UyeAdi", text="Üye Adı")
        self.tw_Geciktirenler.heading("Telefon", text="Telefon")
        self.tw_Geciktirenler.heading("Adres", text="Adres")
        self.tw_Geciktirenler.heading("KitapAdi", text="Kitap Adı")
        self.tw_Geciktirenler.heading("OduncTarihi", text="Ödünç Tarihi")
        self.tw_Geciktirenler.heading("GecikmeSuresi", text="Gecikme Süresi")

        self.tw_Geciktirenler.column("UyeAdi", width=150)
        self.tw_Geciktirenler.column("Telefon", width=90)
        self.tw_Geciktirenler.column("Adres", width=200)
        self.tw_Geciktirenler.column("KitapAdi", width=150)
        self.tw_Geciktirenler.column("OduncTarihi", width=90)
        self.tw_Geciktirenler.column("GecikmeSuresi", width=80)

        self.tw_Geciktirenler.grid(row=0, column=0, sticky="nsew")

    def populate_treeview(self):
        try:
            self.tw_Geciktirenler.delete(*self.tw_Geciktirenler.get_children())
            data = vt.KitapGeciktirenlerListesi()
            gf.PopulateTreeview(self.tw_Geciktirenler, data)
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Kitap geciktirenler listesi alınırken hata oluştu:\n{str(e)}")
