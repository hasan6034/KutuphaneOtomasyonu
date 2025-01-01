import customtkinter as ctk
from tkinter import ttk
import tkinter.messagebox as mb
import Fonksiyonlar.GenelFonksiyonlar as gf
import Fonksiyonlar.Veritabani as vt
import tkinter as tk


class Kullanicilar(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        gf.CenterWindow(self, 650, 600)
        self.title("Kullanıcı İşlemleri")

        self.create_widgets()
        self.bind_events()
        self.Listele()

    def create_widgets(self):
        self.configure_grid()
        self.create_treeview()
        self.create_labels_entries()
        self.create_buttons()

    def configure_grid(self):
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)

    def create_treeview(self):
        self.tw_Kullanicilar = ttk.Treeview(
            self,
            columns=("KullaniciID", "Adi", "Soyadi", "Email", "Sifre"),
            show="headings",
        )
        self.tw_Kullanicilar.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

        headings = ["Kullanıcı ID", "Adı", "Soyadı", "Email", "Sifre"]
        for col, text in zip(self.tw_Kullanicilar["columns"], headings):
            self.tw_Kullanicilar.heading(col, text=text, anchor="center")

        column_widths = [80, 130, 130, 180, 120]
        for col, width in zip(self.tw_Kullanicilar["columns"], column_widths):
            self.tw_Kullanicilar.column(col, width=width)

    def create_labels_entries(self):
        labels = ["Kullanıcı ID:", "Adı:", "Soyadı:", "Email:", "Şifre:"]
        self.entries = {}

        for i, text in enumerate(labels):
            ctk.CTkLabel(self, text=text).grid(row=i+1, column=0, padx=5, pady=5, sticky="w")
            var = tk.StringVar()
            self.entries[text[:-1]] = var
            state = "readonly" if text == "Kullanıcı ID:" else "normal"
            ctk.CTkEntry(self, textvariable=var, state=state).grid(row=i+1, column=1, padx=5, pady=5, sticky="ew")

        self.entries["Kullanıcı ID"].set("-1")

    def create_buttons(self):
        buttons = [("Yeni Kayıt", self.YeniKayit), ("Kaydet", self.Kaydet), ("Sil", self.Sil)]
        for i, (text, command) in enumerate(buttons):
            ctk.CTkButton(self, text=text, command=command).grid(row=6, column=i, padx=5, pady=5, sticky="ew")

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
        for var in self.entries.values():
            var.set("")

    def Kaydet(self):
        try:
            vt.KullaniciEkleGuncelle(
                self.entries["Kullanıcı ID"].get(),
                self.entries["Adı"].get(),
                self.entries["Soyadı"].get(),
                self.entries["Email"].get(),
                self.entries["Şifre"].get(),
            )
            self.Listele()
            self.YeniKayit()
            mb.showinfo("Bilgi", "Kayıt başarıyla eklendi.")
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Kayıt eklenirken hata oluştu:\n{str(e)}")

    def Sil(self):
        try:
            if self.entries["Kullanıcı ID"].get() == "-1":
                mb.showwarning("Uyarı", "Lütfen bir kayıt seçiniz.")
                return
            if not mb.askyesno("Onay", "Kaydı silmek istediğinize emin misiniz?"):
                return
            vt.KullaniciSil(self.entries["Kullanıcı ID"].get())
            self.Listele()
            self.YeniKayit()
            mb.showinfo("Bilgi", "Kayıt başarıyla silindi.")
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Kayıt silinirken hata oluştu:\n{str(e)}")

    def TreeviewSelectedItem(self, event):
        selected_item = self.tw_Kullanicilar.selection()
        if selected_item:
            item = self.tw_Kullanicilar.item(selected_item)
            for key, value in zip(self.entries.keys(), item["values"]):
                self.entries[key].set(value)
