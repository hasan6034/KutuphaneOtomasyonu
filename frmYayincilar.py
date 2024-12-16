import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import Fonksiyonlar.GenelFonksiyonlar as gf
import Fonksiyonlar.Veritabani as vt

class Yayincilar(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        ctk.set_default_color_theme("green")
        gf.CenterWindow(self, 700, 700)
        self.title("Yayınevi İşlemleri")

        def Listele():
            try:
                tw_Yayincilar.delete(*tw_Yayincilar.get_children())
                data = vt.YayinciListesi()
                gf.PopulateTreeview(tw_Yayincilar, data)
            except Exception as e:
                mb.showerror("Hata", f"Yayıncı listesi alınırken hata oluştu: {str(e)}")
        
        def YeniKayit():
            txtYayinciID.set("-1")
            txtYayinciAdi.set("")
            txtAdres.set("")
        
        def Kaydet():
            try:
                if txtYayinciAdi.get() == "" or txtAdres.get() == "":
                    mb.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz!")
                    return
                vt.YayinciEkleGuncelle(
                    txtYayinciID.get(),
                    txtYayinciAdi.get(),
                    txtAdres.get()
                )
                Listele()
                YeniKayit()
            except Exception as e:
                mb.showerror("Hata", f"Yayıncı kaydedilirken hata oluştu: {str(e)}")

        def Sil():
            try:
                if txtYayinciID.get() == "-1":
                    mb.showwarning("Uyarı", "Lütfen bir yayıncı seçiniz!")
                    return
                if not mb.askyesno("Silme Onayı", "Seçili yayıncıyı silmek istediğinizden emin misiniz?"):
                    return
                vt.YayinciSil(txtYayinciID.get())
                Listele()
                YeniKayit()
            except Exception as e:
                mb.showerror("Hata", f"Yayıncı silinirken hata oluştu: {str(e)}")

        tw_Yayincilar = ttk.Treeview(
            self,
            columns=("YayinciID", "YayinciAdi", "Adres"),
            show="headings",
        )
        tw_Yayincilar.grid(
            row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew"
        )

        tw_Yayincilar.heading("YayinciID", text="Yayıncı ID", anchor="center")
        tw_Yayincilar.heading("YayinciAdi", text="Yayıncı Adı")
        tw_Yayincilar.heading("Adres", text="Adres")

        tw_Yayincilar.column("YayinciID", width=80)
        tw_Yayincilar.column("YayinciAdi", width=150)
        tw_Yayincilar.column("Adres", width=200)

        txtYayinciID = tk.StringVar()
        txtYayinciAdi = tk.StringVar()
        txtAdres = tk.StringVar()

        alt = ctk.CTkFrame(self)
        alt.grid(row=1, column=0, columnspan=4, padx=2, pady=2, sticky="ew")

        ctk.CTkLabel(alt, text="Yayıncı ID:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=200, state="readonly", textvariable=txtYayinciID).grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(alt, text="Yayıncı Adı:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=200, textvariable=txtYayinciAdi).grid(row=1, column=3, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(alt, text="Adres:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=200, textvariable=txtAdres).grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="w")

        butonlar = ctk.CTkFrame(self)
        butonlar.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        ctk.CTkButton(butonlar, text="Yeni Kayıt Ekle", command=lambda: YeniKayit()).grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkButton(butonlar, text="Ekle/Güncelle", command=lambda: Kaydet()).grid(row=0, column=1, padx=5, pady=5)
        ctk.CTkButton(butonlar, text="Sil", command=lambda: Sil()).grid(row=0, column=2, padx=5, pady=5)

        txtYayinciID.set("-1")
        Listele()

        def TreeviewSelectedItem(event):
            selected_item = tw_Yayincilar.selection()
            if selected_item:
                item = tw_Yayincilar.item(selected_item)
                txtYayinciID.set(item["values"][0])
                txtYayinciAdi.set(item["values"][1])
                txtAdres.set(item["values"][2])

        tw_Yayincilar.bind("<ButtonRelease-1>", TreeviewSelectedItem)
