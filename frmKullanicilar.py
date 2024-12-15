import customtkinter as ctk
from tkinter import ttk
import tkinter.messagebox as mb
import Fonksiyonlar.GenelFonksiyonlar as gf
import Fonksiyonlar.Veritabani as vt
import tkinter as tk


class Kullanicilar(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        ctk.set_default_color_theme("green")
        gf.CenterWindow(self, 650, 600)
        self.title("Kullanıcı İşlemleri")

        def Listele():
            try:
                tw_Kullanicilar.delete(*tw_Kullanicilar.get_children())
                data = vt.KullaniciListesi()
                gf.PopulateTreeview(tw_Kullanicilar, data)
            except Exception as e:
                mb.showerror("Hata", f"Üye listesi alınırken hata oluştu: {str(e)}")

        def YeniKayit():
            self.txtKullaniciID.set("-1")
            self.txtAdi.set("")
            self.txtSoyadi.set("")
            self.txtEmail.set("")
            self.txtSifre.set("")

        def Kaydet():
            try:
                vt.KullaniciEkleGuncelle(
                    self.txtKullaniciID.get(),
                    self.txtAdi.get(),
                    self.txtSoyadi.get(),
                    self.txtEmail.get(),
                    self.txtSifre.get(),
                )
                Listele()
                YeniKayit()
                mb.showinfo("Bilgi", "Kayıt başarıyla eklendi.")
            except Exception as e:
                mb.showerror("Hata", f"Kayıt eklenirken hata oluştu: {str(e)}")

        def Sil():
            try:
                if self.txtKullaniciID.get() == "-1":
                    mb.showwarning("Uyarı", "Lütfen bir kayıt seçiniz.")
                    return
                if not mb.askyesno("Onay", "Kaydı silmek istediğinize emin misiniz?"):
                    return
                vt.KullaniciSil(self.txtKullaniciID.get())
                Listele()
                YeniKayit()
                mb.showinfo("Bilgi", "Kayıt başarıyla silindi.")
            except Exception as e:
                mb.showerror("Hata", f"Kayıt silinirken hata oluştu: {str(e)}")

        tw_Kullanicilar = ttk.Treeview(
            self,
            columns=("KullaniciID", "Adi", "Soyadi", "Email", "Sifre"),
            show="headings",
        )
        tw_Kullanicilar.grid(
            row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew"
        )

        tw_Kullanicilar.heading("KullaniciID", text="Kullanıcı ID", anchor="center")
        tw_Kullanicilar.heading("Adi", text="Adı")
        tw_Kullanicilar.heading("Soyadi", text="Soyadı")
        tw_Kullanicilar.heading("Email", text="Email")
        tw_Kullanicilar.heading("Sifre", text="Sifre")

        tw_Kullanicilar.column("KullaniciID", width=80)
        tw_Kullanicilar.column("Adi", width=130)
        tw_Kullanicilar.column("Soyadi", width=130)
        tw_Kullanicilar.column("Email", width=180)
        tw_Kullanicilar.column("Sifre", width=120)

        ctk.CTkLabel(self, text="Kullanıcı ID:").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkLabel(self, text="Adı:").grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkLabel(self, text="Soyadı:").grid(
            row=3, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkLabel(self, text="Email:").grid(
            row=4, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkLabel(self, text="Şifre:").grid(
            row=5, column=0, padx=5, pady=5, sticky="w"
        )

        self.txtKullaniciID = tk.StringVar()
        self.txtAdi = tk.StringVar()
        self.txtSoyadi = tk.StringVar()
        self.txtEmail = tk.StringVar()
        self.txtSifre = tk.StringVar()

        ctk.CTkEntry(self, state="readonly", textvariable=self.txtKullaniciID).grid(
            row=1, column=1, padx=5, pady=5, sticky="w"
        )
        ctk.CTkEntry(self, textvariable=self.txtAdi).grid(
            row=2, column=1, padx=5, pady=5, sticky="w"
        )
        ctk.CTkEntry(self, textvariable=self.txtSoyadi).grid(
            row=3, column=1, padx=5, pady=5, sticky="w"
        )
        ctk.CTkEntry(self, textvariable=self.txtEmail).grid(
            row=4, column=1, padx=5, pady=5, sticky="w"
        )
        ctk.CTkEntry(self, textvariable=self.txtSifre).grid(
            row=5, column=1, padx=5, pady=5, sticky="w"
        )

        self.txtKullaniciID.set("-1")

        ctk.CTkButton(self, text="Yeni Kayıt", command=lambda: YeniKayit()).grid(
            row=6, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkButton(self, text="Kaydet", command=lambda: Kaydet()).grid(
            row=6, column=1, padx=5, pady=5, sticky="w"
        )
        ctk.CTkButton(self, text="Sil", command=lambda: Sil()).grid(
            row=6, column=2, padx=5, pady=5, sticky="w"
        )

        Listele()

        def TreeviewSelectedItem(event):
            selected_item = tw_Kullanicilar.selection()
            if selected_item:
                item = tw_Kullanicilar.item(selected_item)
                self.txtKullaniciID.set(item["values"][0])
                self.txtAdi.set(item["values"][1])
                self.txtSoyadi.set(item["values"][2])
                self.txtEmail.set(item["values"][3])
                self.txtSifre.set(item["values"][4])

        tw_Kullanicilar.bind("<ButtonRelease-1>", TreeviewSelectedItem)
