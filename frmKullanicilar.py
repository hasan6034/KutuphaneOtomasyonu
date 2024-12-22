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

        self.tw_Kullanicilar = ttk.Treeview(
            self,
            columns=("KullaniciID", "Adi", "Soyadi", "Email", "Sifre"),
            show="headings",
        )
        self.tw_Kullanicilar.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

        self.tw_Kullanicilar.heading("KullaniciID", text="Kullanıcı ID", anchor="center")
        self.tw_Kullanicilar.heading("Adi", text="Adı")
        self.tw_Kullanicilar.heading("Soyadi", text="Soyadı")
        self.tw_Kullanicilar.heading("Email", text="Email")
        self.tw_Kullanicilar.heading("Sifre", text="Sifre")

        self.tw_Kullanicilar.column("KullaniciID", width=80)
        self.tw_Kullanicilar.column("Adi", width=130)
        self.tw_Kullanicilar.column("Soyadi", width=130)
        self.tw_Kullanicilar.column("Email", width=180)
        self.tw_Kullanicilar.column("Sifre", width=120)

        labels = ["Kullanıcı ID:", "Adı:", "Soyadı:", "Email:", "Şifre:"]
        for i, text in enumerate(labels):
            ctk.CTkLabel(self, text=text).grid(row=i+1, column=0, padx=5, pady=5, sticky="w")

        self.txtKullaniciID = tk.StringVar()
        self.txtAdi = tk.StringVar()
        self.txtSoyadi = tk.StringVar()
        self.txtEmail = tk.StringVar()
        self.txtSifre = tk.StringVar()

        ctk.CTkEntry(self, state="readonly", textvariable=self.txtKullaniciID).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkEntry(self, textvariable=self.txtAdi).grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkEntry(self, textvariable=self.txtSoyadi).grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkEntry(self, textvariable=self.txtEmail).grid(row=4, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkEntry(self, textvariable=self.txtSifre).grid(row=5, column=1, padx=5, pady=5, sticky="ew")

        self.txtKullaniciID.set("-1")

        ctk.CTkButton(self, text="Yeni Kayıt", command=self.YeniKayit).grid(row=6, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(self, text="Kaydet", command=self.Kaydet).grid(row=6, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(self, text="Sil", command=self.Sil).grid(row=6, column=2, padx=5, pady=5, sticky="ew")

    def bind_events(self):
        self.tw_Kullanicilar.bind("<ButtonRelease-1>", self.TreeviewSelectedItem)

    def Listele(self):
        try:
            self.tw_Kullanicilar.delete(*self.tw_Kullanicilar.get_children())
            data = vt.KullaniciListesi()
            gf.PopulateTreeview(self.tw_Kullanicilar, data)
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Üye listesi alınırken hata oluştu:\n{str(e)}")

    def YeniKayit(self):
        self.txtKullaniciID.set("-1")
        self.txtAdi.set("")
        self.txtSoyadi.set("")
        self.txtEmail.set("")
        self.txtSifre.set("")

    def Kaydet(self):
        try:
            vt.KullaniciEkleGuncelle(
                self.txtKullaniciID.get(),
                self.txtAdi.get(),
                self.txtSoyadi.get(),
                self.txtEmail.get(),
                self.txtSifre.get(),
            )
            self.Listele()
            self.YeniKayit()
            mb.showinfo("Bilgi", "Kayıt başarıyla eklendi.")
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Kayıt eklenirken hata oluştu:\n{str(e)}")

    def Sil(self):
        try:
            if self.txtKullaniciID.get() == "-1":
                mb.showwarning("Uyarı", "Lütfen bir kayıt seçiniz.")
                return
            if not mb.askyesno("Onay", "Kaydı silmek istediğinize emin misiniz?"):
                return
            vt.KullaniciSil(self.txtKullaniciID.get())
            self.Listele()
            self.YeniKayit()
            mb.showinfo("Bilgi", "Kayıt başarıyla silindi.")
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Kayıt silinirken hata oluştu:\n{str(e)}")

    def TreeviewSelectedItem(self, event):
        selected_item = self.tw_Kullanicilar.selection()
        if selected_item:
            item = self.tw_Kullanicilar.item(selected_item)
            self.txtKullaniciID.set(item["values"][0])
            self.txtAdi.set(item["values"][1])
            self.txtSoyadi.set(item["values"][2])
            self.txtEmail.set(item["values"][3])
            self.txtSifre.set(item["values"][4])
