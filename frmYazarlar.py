import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import Fonksiyonlar.GenelFonksiyonlar as gf
import Fonksiyonlar.Veritabani as vt
import tkinter.messagebox as mb
from datetime import datetime
import tkcalendar as tkcal

class Yazarlar(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        ctk.set_default_color_theme("green")
        gf.CenterWindow(self, 600, 600)
        self.title("Yazar İşlemleri")

        self.create_widgets()
        self.bind_events()
        self.YazarlariGetir()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.tw_Yazarlar = ttk.Treeview(
            self,
            columns=("YazarID", "YazarAdi", "DogumTarihi"),
            show="headings",
        )
        self.tw_Yazarlar.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

        self.tw_Yazarlar.heading("YazarID", text="Yazar ID", anchor="center")
        self.tw_Yazarlar.heading("YazarAdi", text="Yazar Adı")
        self.tw_Yazarlar.heading("DogumTarihi", text="Doğum Tarihi")

        self.tw_Yazarlar.column("YazarID", width=80)
        self.tw_Yazarlar.column("YazarAdi", width=130)
        self.tw_Yazarlar.column("DogumTarihi", width=130)

        ctk.CTkLabel(self, text="Yazar ID:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkLabel(self, text="Yazar Adı:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkLabel(self, text="Doğum Tarihi:").grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.txtYazarID = tk.StringVar()
        self.txtYazarAdi = tk.StringVar()
        self.dateDogumTarihi = tk.StringVar()

        ctk.CTkEntry(self, state="readonly", textvariable=self.txtYazarID).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkEntry(self, textvariable=self.txtYazarAdi).grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        tkcal.DateEntry(self, textvariable=self.dateDogumTarihi, date_pattern='yyyy-mm-dd').grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        self.txtYazarID.set("-1")

        ctk.CTkButton(self, text="Yeni Kayıt Ekle", command=self.YeniKayit).grid(row=4, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(self, text="Ekle/Güncelle", command=self.Kaydet).grid(row=4, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(self, text="Sil", command=self.Sil).grid(row=4, column=2, padx=5, pady=5, sticky="ew")

    def bind_events(self):
        self.tw_Yazarlar.bind("<ButtonRelease-1>", self.TreeviewSelectedItem)

    def YazarlariGetir(self):
        try:
            self.tw_Yazarlar.delete(*self.tw_Yazarlar.get_children())
            data = vt.YazarListesi()
            gf.PopulateTreeview(self.tw_Yazarlar, data)
            self.YeniKayit()
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Yazar listesi alınırken hata oluştu:\n{str(e)}")

    def YeniKayit(self):
        self.txtYazarID.set("-1")
        self.txtYazarAdi.set("")
        self.dateDogumTarihi.set(datetime.now().strftime("%Y-%m-%d"))

    def Kaydet(self):
        try:
            vt.YazarEkleGuncelle(
                self.txtYazarID.get(),
                self.txtYazarAdi.get(),
                self.dateDogumTarihi.get()
            )
            self.YazarlariGetir()
            mb.showinfo("Bilgi", "Yazar başarıyla eklendi.")
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Yazar eklenirken hata oluştu:\n{str(e)}")

    def Sil(self):
        try:
            if self.txtYazarID.get() == "-1":
                mb.showwarning("Uyarı", "Lütfen bir yazar seçiniz.")
                return
            if not mb.askyesno("Onay", "Bu yazarı silmek istediğinizden emin misiniz?"):
                return
            vt.YazarSil(self.txtYazarID.get())
            self.YazarlariGetir()
            mb.showinfo("Bilgi", "Yazar başarıyla silindi.")
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Yazar silinirken hata oluştu:\n{str(e)}")

    def TreeviewSelectedItem(self, event):
        if len(self.tw_Yazarlar.get_children()) == 0:
            return
        secilen = self.tw_Yazarlar.selection()
        if secilen:
            item = self.tw_Yazarlar.item(secilen)
            self.txtYazarID.set(item["values"][0])
            self.txtYazarAdi.set(item["values"][1])
            self.dateDogumTarihi.set(item["values"][2])
