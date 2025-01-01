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
        gf.CenterWindow(self, 750, 600)
        self.title("Üye İşlemleri")

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
        self.tw_Uyeler = ttk.Treeview(
            self,
            columns=("UyeID", "Adi", "Telefon", "Adres", "KayitTarihi"),
            show="headings",
        )
        self.tw_Uyeler.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")
        headings = ["Üye ID", "Adı", "Telefon", "Adres", "Kayıt Tarihi"]
        for col, text in zip(self.tw_Uyeler["columns"], headings):
            self.tw_Uyeler.heading(col, text=text, anchor="center")
            self.tw_Uyeler.column(col, width=100 if col != "UyeID" else 50)

    def create_labels_entries(self):
        labels = ["Üye ID:", "Adı:", "Telefon:", "Adres:", "Kayıt Tarihi:"]
        self.entries = {}
        for i, text in enumerate(labels):
            ctk.CTkLabel(self, text=text).grid(row=i + 1, column=0, padx=5, pady=5, sticky="w")
            var = tk.StringVar()
            entry = ctk.CTkEntry(self, textvariable=var)
            if text == "Üye ID:":
                entry.configure(state="readonly")
                var.set("-1")
            elif text == "Kayıt Tarihi:":
                entry = tkcal.DateEntry(self, textvariable=var, date_pattern='yyyy-mm-dd')
            entry.grid(row=i + 1, column=1, padx=5, pady=5, sticky="ew")
            self.entries[text] = var

    def create_buttons(self):
        buttons = [("Yeni Kayıt", self.YeniKayit), ("Kaydet", self.Kaydet), ("Sil", self.Sil)]
        for i, (text, command) in enumerate(buttons):
            ctk.CTkButton(self, text=text, command=command).grid(row=6, column=i, padx=5, pady=5, sticky="ew")

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
        for key in self.entries:
            self.entries[key].set("" if key != "Kayıt Tarihi:" else datetime.now().strftime("%Y-%m-%d"))
        self.entries["Üye ID:"].set("-1")

    def Kaydet(self):
        try:
            vt.UyeEkleGuncelle(
                self.entries["Üye ID:"].get(),
                self.entries["Adı:"].get(),
                self.entries["Telefon:"].get(),
                self.entries["Adres:"].get(),
                self.entries["Kayıt Tarihi:"].get(),
            )
            self.Listele()
            self.YeniKayit()
            mb.showinfo("Bilgi", "Kayıt başarıyla eklendi.")
        except Exception as e:
            mb.showerror("Hata", f"Kayıt eklenirken hata oluştu: {str(e)}")

    def Sil(self):
        try:
            if self.entries["Üye ID:"].get() == "-1":
                mb.showwarning("Uyarı", "Lütfen bir üye seçiniz.")
                return
            if not mb.askyesno("Onay", "Bu üyeyi silmek istediğinizden emin misiniz?"):
                return
            vt.UyeSil(self.entries["Üye ID:"].get())
            self.Listele()
            self.YeniKayit()
            mb.showinfo("Bilgi", "Üye başarıyla silindi.")
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Kayıt silinirken hata oluştu:\n{str(e)}")

    def TreeviewSelectedItem(self, event):
        selected_item = self.tw_Uyeler.selection()
        if selected_item:
            item = self.tw_Uyeler.item(selected_item)
            for key, value in zip(self.entries, item["values"]):
                self.entries[key].set(value)
