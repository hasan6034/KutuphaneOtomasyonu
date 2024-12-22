import customtkinter as ctk
from tkinter import ttk
import tkinter.messagebox as mb
import Fonksiyonlar.GenelFonksiyonlar as gf
import Fonksiyonlar.Veritabani as vt
import tkinter as tk
import tkcalendar as tkcal
from datetime import datetime


class Uye(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        ctk.set_default_color_theme("green")
        gf.CenterWindow(self, 750, 600)
        self.title("Üye İşlemleri")

        self.create_widgets()
        self.bind_events()
        self.Listele()

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
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)

        self.tw_Uyeler = ttk.Treeview(
            self,
            columns=("UyeID", "Adi", "Telefon", "Adres", "KayitTarihi"),
            show="headings",
        )
        self.tw_Uyeler.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

        self.tw_Uyeler.heading("UyeID", text="Üye ID", anchor="center")
        self.tw_Uyeler.heading("Adi", text="Adı")
        self.tw_Uyeler.heading("Telefon", text="Telefon")
        self.tw_Uyeler.heading("Adres", text="Adres")
        self.tw_Uyeler.heading("KayitTarihi", text="Kayıt Tarihi")

        self.tw_Uyeler.column("UyeID", width=50)
        self.tw_Uyeler.column("Adi", width=200)
        self.tw_Uyeler.column("Telefon", width=100)
        self.tw_Uyeler.column("Adres", width=250)
        self.tw_Uyeler.column("KayitTarihi", width=100)

        labels = ["Üye ID:", "Adı:", "Telefon:", "Adres:", "Kayıt Tarihi:"]
        for i, text in enumerate(labels):
            ctk.CTkLabel(self, text=text).grid(row=i + 1, column=0, padx=5, pady=5, sticky="w")

        self.txtUyeID = tk.StringVar()
        self.txtAdi = tk.StringVar()
        self.txtTelefon = tk.StringVar()
        self.txtAdres = tk.StringVar()
        self.txtKayitTarihi = tk.StringVar()

        ctk.CTkEntry(self, state="readonly", textvariable=self.txtUyeID).grid(
            row=1, column=1, padx=5, pady=5, sticky="ew"
        )
        ctk.CTkEntry(self, textvariable=self.txtAdi).grid(
            row=2, column=1, padx=5, pady=5, sticky="ew"
        )
        ctk.CTkEntry(self, textvariable=self.txtTelefon).grid(
            row=3, column=1, padx=5, pady=5, sticky="ew"
        )
        ctk.CTkEntry(self, textvariable=self.txtAdres).grid(
            row=4, column=1, padx=5, pady=5, sticky="ew"
        )
        self.date_entry = tkcal.DateEntry(self, textvariable=self.txtKayitTarihi, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

        self.txtUyeID.set("-1")

        ctk.CTkButton(self, text="Yeni Kayıt", command=self.YeniKayit).grid(
            row=6, column=0, padx=5, pady=5, sticky="ew"
        )
        ctk.CTkButton(self, text="Kaydet", command=self.Kaydet).grid(
            row=6, column=1, padx=5, pady=5, sticky="ew"
        )
        ctk.CTkButton(self, text="Sil", command=self.Sil).grid(
            row=6, column=2, padx=5, pady=5, sticky="ew"
        )

    def bind_events(self):
        self.tw_Uyeler.bind("<ButtonRelease-1>", self.TreeviewSelectedItem)

    def Listele(self):
        try:
            self.tw_Uyeler.delete(*self.tw_Uyeler.get_children())
            data = vt.UyeListesi()
            gf.PopulateTreeview(self.tw_Uyeler, data)
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Üye listesi alınırken hata oluştu:\n{str(e)}")

    def YeniKayit(self):
        self.txtUyeID.set("-1")
        self.txtAdi.set("")
        self.txtTelefon.set("")
        self.txtAdres.set("")
        self.txtKayitTarihi.set(datetime.now().strftime("%Y-%m-%d"))

    def Kaydet(self):
        try:
            vt.UyeEkleGuncelle(
                self.txtUyeID.get(),
                self.txtAdi.get(),
                self.txtTelefon.get(),
                self.txtAdres.get(),
                self.txtKayitTarihi.get(),
            )
            self.Listele()
            self.YeniKayit()
            mb.showinfo("Bilgi", "Kayıt başarıyla eklendi.")
        except Exception as e:
            mb.showerror("Hata", f"Kayıt eklenirken hata oluştu: {str(e)}")

    def Sil(self):
        try:
            if self.txtUyeID.get() == "-1":
                mb.showwarning("Uyarı", "Lütfen bir üye seçiniz.")
                return
            if not mb.askyesno("Onay", "Bu üyeyi silmek istediğinizden emin misiniz?"):
                return
            vt.UyeSil(self.txtUyeID.get())
            self.Listele()
            self.YeniKayit()
            mb.showinfo("Bilgi", "Üye başarıyla silindi.")
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Kayıt silinirken hata oluştu:\n{str(e)}")

    def TreeviewSelectedItem(self, event):
        selected_item = self.tw_Uyeler.selection()
        if selected_item:
            item = self.tw_Uyeler.item(selected_item)
            self.txtUyeID.set(item["values"][0])
            self.txtAdi.set(item["values"][1])
            self.txtTelefon.set(item["values"][2])
            self.txtAdres.set(item["values"][3])
            self.txtKayitTarihi.set(item["values"][4])
