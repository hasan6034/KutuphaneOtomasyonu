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

        def YazarlariGetir():
            try:
                tw_Yazarlar.delete(*tw_Yazarlar.get_children())
                data = vt.YazarListesi()
                gf.PopulateTreeview(tw_Yazarlar, data)
                YeniKayit()
            except Exception as e:
                mb.showerror("Hata", f"Yazar listesi alınırken hata oluştu: {str(e)}")

        def YeniKayit():
            self.txtYazarID.set("-1")
            self.txtYazarAdi.set("")
            self.dateDogumTarihi.set(datetime.now().strftime("%Y-%m-%d"))

        def Kaydet():
            try:
                vt.YazarEkleGuncelle(
                    self.txtYazarID.get(),
                    self.txtYazarAdi.get(),
                    self.dateDogumTarihi.get()
                )
                YazarlariGetir()
                mb.showinfo("Bilgi", "Yazar başarıyla eklendi.")
            except Exception as e:
                mb.showerror("Hata", f"Yazar eklenirken hata oluştu: {str(e)}")
        
        def Sil():
            try:
                if self.txtYazarID.get() == "-1":
                    mb.showwarning("Uyarı", "Lütfen bir yazar seçiniz.")
                    return
                if not mb.askyesno("Onay", "Bu yazarı silmek istediğinizden emin misiniz?"):
                    return
                vt.YazarSil(self.txtYazarID.get())
                YazarlariGetir()
                mb.showinfo("Bilgi","Yazar başarıyla silindi.")
            except Exception as e:
                mb.showerror("Hata", f"Yazar silinirken hata oluştu: {str(e)}")

        tw_Yazarlar = ttk.Treeview(
            self,
            columns=("YazarID", "YazarAdi", "DogumTarihi"),
            show="headings",
        )
        tw_Yazarlar.grid(
            row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew"
        )

        tw_Yazarlar.heading("YazarID", text="Yazar ID", anchor="center")
        tw_Yazarlar.heading("YazarAdi", text="Yazar Adı")
        tw_Yazarlar.heading("DogumTarihi", text="Doğum Tarihi")

        tw_Yazarlar.column("YazarID", width=80)
        tw_Yazarlar.column("YazarAdi", width=130)
        tw_Yazarlar.column("DogumTarihi", width=130)

        ctk.CTkLabel(self, text="Yazar ID:").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        
        ctk.CTkLabel(self, text="Yazar Adı:").grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )

        ctk.CTkLabel(self, text="Doğum Tarihi:").grid(
            row=3, column=0, padx=5, pady=5, sticky="w"
        )

        self.txtYazarID = tk.StringVar()
        self.txtYazarAdi = tk.StringVar()
        self.dateDogumTarihi = tk.StringVar()

        ctk.CTkEntry(self, state="readonly", textvariable=self.txtYazarID).grid(
            row=1, column=1, padx=5, pady=5, sticky="w"
        )

        ctk.CTkEntry(self, textvariable=self.txtYazarAdi).grid(
            row=2, column=1, padx=5, pady=5, sticky="w"
        )

        date_entry = tkcal.DateEntry(self, textvariable=self.dateDogumTarihi, date_pattern='yyyy-mm-dd')
        date_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.txtYazarID.set("-1")

        btnYeniKayit = ctk.CTkButton(self, text="Yeni Kayıt Ekle", command=lambda: YeniKayit())
        btnYeniKayit.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        btnEkle = ctk.CTkButton(self, text="Ekle/Güncelle", command=lambda: Kaydet())
        btnEkle.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        btnSil = ctk.CTkButton(self, text="Sil", command=lambda: Sil())
        btnSil.grid(row=4, column=2, padx=5, pady=5, sticky="w")

        YazarlariGetir()

        def TreeviewSelectedItem(event):
            if len(tw_Yazarlar.get_children()) == 0:
                return
            secilen = tw_Yazarlar.selection()[0]
            self.txtYazarID.set(tw_Yazarlar.item(secilen)["values"][0])
            self.txtYazarAdi.set(tw_Yazarlar.item(secilen)["values"][1])
            self.dateDogumTarihi.set(tw_Yazarlar.item(secilen)["values"][2])
        
        tw_Yazarlar.bind("<ButtonRelease-1>", TreeviewSelectedItem)