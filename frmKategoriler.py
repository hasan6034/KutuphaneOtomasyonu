import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import Fonksiyonlar.GenelFonksiyonlar as gf
import Fonksiyonlar.Veritabani as vt

class Kategoriler(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        ctk.set_default_color_theme("green")
        gf.CenterWindow(self, 700, 700)
        self.title("Kategori İşlemleri")

        def Listele():
            try:
                tw_Kategoriler.delete(*tw_Kategoriler.get_children())
                data = vt.KategoriListesi()
                gf.PopulateTreeview(tw_Kategoriler, data)
            except Exception as e:
                mb.showerror("Hata", f"Kategori listesi alınırken hata oluştu: {str(e)}")
        
        def YeniKayit():
            txtKategoriID.set("-1")
            txtKategoriAdi.set("")

        def Kaydet():
            try:
                if txtKategoriAdi.get() == "":
                    mb.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz!")
                    return
                vt.KategoriEkleGuncelle(
                    txtKategoriID.get(),
                    txtKategoriAdi.get()
                )
                Listele()
                YeniKayit()
            except Exception as e:
                mb.showerror("Hata", f"Kategori kaydedilirken hata oluştu: {str(e)}")

        def Sil():
            try:
                if txtKategoriID.get() == "-1":
                    mb.showwarning("Uyarı", "Lütfen bir kategori seçiniz!")
                    return
                if not mb.askyesno("Silme Onayı", "Seçili kategoriyi silmek istediğinizden emin misiniz?"):
                    return
                vt.KategoriSil(txtKategoriID.get())
                Listele()
                YeniKayit()
            except Exception as e:
                mb.showerror("Hata", f"Kategori silinirken hata oluştu: {str(e)}")

        tw_Kategoriler = ttk.Treeview(
            self,
            columns=("KategoriID", "KategoriAdi"),
            show="headings",
        )
        tw_Kategoriler.grid(
            row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew"
        )

        tw_Kategoriler.heading("KategoriID", text="Kategori ID", anchor="center")
        tw_Kategoriler.heading("KategoriAdi", text="Kategori Adı")

        tw_Kategoriler.column("KategoriID", width=80)
        tw_Kategoriler.column("KategoriAdi", width=150)

        txtKategoriID = tk.StringVar()
        txtKategoriAdi = tk.StringVar()

        alt = ctk.CTkFrame(self)
        alt.grid(row=1, column=0, columnspan=4, padx=2, pady=2, sticky="ew")

        ctk.CTkLabel(alt, text="Kategori ID:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=200, state="readonly", textvariable=txtKategoriID).grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(alt, text="Kategori Adı:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=200, textvariable=txtKategoriAdi).grid(row=1, column=3, padx=5, pady=5, sticky="w")

        butonlar = ctk.CTkFrame(self)
        butonlar.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        ctk.CTkButton(butonlar, text="Yeni Kayıt Ekle", command=lambda: YeniKayit()).grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkButton(butonlar, text="Ekle/Güncelle", command=lambda: Kaydet()).grid(row=0, column=1, padx=5, pady=5)
        ctk.CTkButton(butonlar, text="Sil", command=lambda: Sil()).grid(row=0, column=2, padx=5, pady=5)

        txtKategoriID.set("-1")
        Listele()

        def TreeviewSelectedItem(event):
            selected_item = tw_Kategoriler.selection()
            if selected_item:
                item = tw_Kategoriler.item(selected_item)
                txtKategoriID.set(item["values"][0])
                txtKategoriAdi.set(item["values"][1])

        tw_Kategoriler.bind("<ButtonRelease-1>", TreeviewSelectedItem)