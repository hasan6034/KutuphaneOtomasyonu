import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import Fonksiyonlar.GenelFonksiyonlar as gf
import Fonksiyonlar.Veritabani as vt
from datetime import datetime
import tkcalendar as tkcal

class Odunc(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        ctk.set_default_color_theme("blue")
        gf.CenterWindow(self, 700, 700)
        self.title("Ödünç İşlemleri")

        try:
            dataUyeler = vt.UyeListesi()
            dataUyeler.insert(0, (-1, "Seçiniz")) # İlk sıraya "Seçiniz" ekle

            dataKitaplar = vt.KitapListesi()
            dataKitaplar.insert(0, (-1, "Seçiniz")) # İlk sıraya "Seçiniz" ekle

            displayUyeler = [row[1] for row in dataUyeler] # Üye Adını al
            displayKitaplar = [row[1] for row in dataKitaplar] # Kitap Adını al

            valueUyeler = {row[1]: row[0] for row in dataUyeler} # Üye ID al | Bunu ödünç kaydetmek için kullanacağız
            valueKitaplar = {row[1]: row[0] for row in dataKitaplar} # Kitap ID al | Bunu ödünç kaydetmek için kullanacağız
        except Exception as e:
            mb.showerror("Hata", f"Ödünç listesi alınırken hata oluştu: {str(e)}")

        def Listele():
            try:
                tw_Kategoriler.delete(*tw_Kategoriler.get_children())
                data = vt.OduncListesi()
                gf.PopulateTreeview(tw_Kategoriler, data)
            except Exception as e:
                mb.showerror("Hata", f"Ödünç listesi alınırken hata oluştu: {str(e)}")

        def YeniKayit():
            txtIslemID.set("-1")
            txtUyeAdi.set("Seçiniz")
            txtKitapAdi.set("Seçiniz")
            txtOduncTarihi.set(datetime.now().strftime("%Y-%m-%d"))
            txtIadeTarihi.set(datetime.now().strftime("%Y-%m-%d"))
        
        def Kaydet():
            try:
                if txtUyeAdi.get() == "Seçiniz" or txtKitapAdi.get() == "Seçiniz" or txtOduncTarihi.get() == "" or txtIadeTarihi.get() == "":
                    mb.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz!")
                    return
                vt.OduncEkleGuncelle(
                    txtIslemID.get(),
                    valueUyeler.get(txtUyeAdi.get()),
                    valueKitaplar.get(txtKitapAdi.get()),
                    txtOduncTarihi.get(),
                    txtIadeTarihi.get()
                )
                Listele()
                YeniKayit()
            except Exception as e:
                mb.showerror("Hata", f"Ödünç kaydedilirken hata oluştu: {str(e)}")
        
        def Sil():
            try:
                if txtIslemID.get() == "-1":
                    mb.showwarning("Uyarı", "Silinecek kaydı seçiniz!")
                    return
                vt.OduncSil(txtIslemID.get())
                Listele()
                YeniKayit()
            except Exception as e:
                mb.showerror("Hata", f"Ödünç silinirken hata oluştu: {str(e)}")

        tw_Kategoriler = ttk.Treeview(
            self,
            columns=("IslemID", "UyeAdi", "KitapAdi", "OduncTarihi", "IadeTarihi"),
            show="headings",
        )
        tw_Kategoriler.grid(
            row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew"
        )

        tw_Kategoriler.heading("IslemID", text="İşlem ID", anchor="center")
        tw_Kategoriler.heading("UyeAdi", text="Üye Adı")
        tw_Kategoriler.heading("KitapAdi", text="Kitap Adı")
        tw_Kategoriler.heading("OduncTarihi", text="OduncTarihi")
        tw_Kategoriler.heading("IadeTarihi", text="IadeTarihi")

        tw_Kategoriler.column("IslemID", width=80)
        tw_Kategoriler.column("UyeAdi", width=150)
        tw_Kategoriler.column("KitapAdi", width=150)
        tw_Kategoriler.column("OduncTarihi", width=150)
        tw_Kategoriler.column("IadeTarihi", width=150)

        txtIslemID = tk.StringVar()
        txtUyeAdi = tk.StringVar()
        txtKitapAdi = tk.StringVar()
        txtOduncTarihi = tk.StringVar()
        txtIadeTarihi = tk.StringVar()

        alt = ctk.CTkFrame(self)
        alt.grid(row=1, column=0, columnspan=4, padx=2, pady=2, sticky="ew")

        ctk.CTkLabel(alt, text="İşlem ID:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=200, state="readonly", textvariable=txtIslemID).grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(alt, text="Üye Adı:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        cmb1 = ctk.CTkOptionMenu(alt, width=200, variable=txtUyeAdi)
        cmb1.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(alt, text="Kitap Adı:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        cmb2 = ctk.CTkOptionMenu(alt, width=200, variable=txtKitapAdi)
        cmb2.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(alt, text="Ödünç Tarihi:").grid(row=2, column=2, padx=5, pady=5, sticky="w")
        tkcal.DateEntry(alt, width= 30, textvariable=txtOduncTarihi, date_pattern='yyyy-mm-dd').grid(row=2, column=3, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(alt, text="İade Tarihi:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        tkcal.DateEntry(alt, width= 30, textvariable=txtIadeTarihi, date_pattern='yyyy-mm-dd').grid(row=3, column=1, padx=5, pady=5, sticky="w")

        butonlar = ctk.CTkFrame(self)
        butonlar.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        btnYeniKayit = ctk.CTkButton(butonlar, text="Yeni Kayıt Ekle", command=lambda: YeniKayit())
        btnYeniKayit.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        btnEkle = ctk.CTkButton(butonlar, text="Ekle/Güncelle", command=lambda: Kaydet())
        btnEkle.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        btnSil = ctk.CTkButton(butonlar, text="Sil", command=lambda: Sil())
        btnSil.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        cmb1.configure(values=displayUyeler)
        cmb1.set("Seçiniz")

        cmb2.configure(values=displayKitaplar)
        cmb2.set("Seçiniz")

        def TreeviewSelectedItem(event):
            selected_item = tw_Kategoriler.selection()
            if selected_item:
                item = tw_Kategoriler.item(selected_item)
                txtIslemID.set(item["values"][0])
                txtUyeAdi.set(item["values"][1])
                txtKitapAdi.set(item["values"][2])
                txtOduncTarihi.set(item["values"][3])
                txtIadeTarihi.set(item["values"][4])

        tw_Kategoriler.bind("<ButtonRelease-1>", TreeviewSelectedItem)
