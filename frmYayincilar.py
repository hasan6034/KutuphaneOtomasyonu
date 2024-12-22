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

        self.create_widgets()
        self.bind_events()
        self.reset_fields()
        self.list_publishers()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def create_widgets(self):
        self.tw_Yayincilar = ttk.Treeview(
            self,
            columns=("YayinciID", "YayinciAdi", "Adres"),
            show="headings",
        )
        self.tw_Yayincilar.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

        self.tw_Yayincilar.heading("YayinciID", text="Yayıncı ID", anchor="center")
        self.tw_Yayincilar.heading("YayinciAdi", text="Yayıncı Adı")
        self.tw_Yayincilar.heading("Adres", text="Adres")

        self.tw_Yayincilar.column("YayinciID", width=80)
        self.tw_Yayincilar.column("YayinciAdi", width=150)
        self.tw_Yayincilar.column("Adres", width=200)

        self.txtYayinciID = tk.StringVar()
        self.txtYayinciAdi = tk.StringVar()
        self.txtAdres = tk.StringVar()

        alt = ctk.CTkFrame(self)
        alt.grid(row=1, column=0, columnspan=4, padx=2, pady=2, sticky="ew")
        alt.grid_columnconfigure(1, weight=1)
        alt.grid_columnconfigure(3, weight=1)

        ctk.CTkLabel(alt, text="Yayıncı ID:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=200, state="readonly", textvariable=self.txtYayinciID).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(alt, text="Yayıncı Adı:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=200, textvariable=self.txtYayinciAdi).grid(row=1, column=3, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(alt, text="Adres:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=200, textvariable=self.txtAdres).grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

        butonlar = ctk.CTkFrame(self)
        butonlar.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        butonlar.grid_columnconfigure(0, weight=1)
        butonlar.grid_columnconfigure(1, weight=1)
        butonlar.grid_columnconfigure(2, weight=1)

        ctk.CTkButton(butonlar, text="Yeni Kayıt Ekle", command=self.reset_fields).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(butonlar, text="Ekle/Güncelle", command=self.save_publisher).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(butonlar, text="Sil", command=self.delete_publisher).grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    def bind_events(self):
        self.tw_Yayincilar.bind("<ButtonRelease-1>", self.on_treeview_select)

    def list_publishers(self):
        try:
            self.tw_Yayincilar.delete(*self.tw_Yayincilar.get_children())
            data = vt.YayinciListesi()
            gf.PopulateTreeview(self.tw_Yayincilar, data)
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Yayıncı listesi alınırken hata oluştu:\n{str(e)}")

    def reset_fields(self):
        self.txtYayinciID.set("-1")
        self.txtYayinciAdi.set("")
        self.txtAdres.set("")

    def save_publisher(self):
        try:
            if self.txtYayinciAdi.get() == "" or self.txtAdres.get() == "":
                mb.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz!")
                return
            vt.YayinciEkleGuncelle(
                self.txtYayinciID.get(),
                self.txtYayinciAdi.get(),
                self.txtAdres.get()
            )
            self.list_publishers()
            self.reset_fields()
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Yayıncı kaydedilirken hata oluştu:\n{str(e)}")

    def delete_publisher(self):
        try:
            if self.txtYayinciID.get() == "-1":
                mb.showwarning("Uyarı", "Lütfen bir yayıncı seçiniz!")
                return
            if not mb.askyesno("Silme Onayı", "Seçili yayıncıyı silmek istediğinizden emin misiniz?"):
                return
            vt.YayinciSil(self.txtYayinciID.get())
            self.list_publishers()
            self.reset_fields()
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Yayıncı silinirken hata oluştu:\n{str(e)}")

    def on_treeview_select(self, event):
        selected_item = self.tw_Yayincilar.selection()
        if selected_item:
            item = self.tw_Yayincilar.item(selected_item)
            self.txtYayinciID.set(item["values"][0])
            self.txtYayinciAdi.set(item["values"][1])
            self.txtAdres.set(item["values"][2])
