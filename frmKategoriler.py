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

        self.create_widgets()
        self.bind_events()
        self.reset_fields()
        self.list_categories()

    def create_widgets(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tw_Kategoriler = ttk.Treeview(
            self,
            columns=("KategoriID", "KategoriAdi"),
            show="headings",
        )
        self.tw_Kategoriler.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")
        self.tw_Kategoriler.heading("KategoriID", text="Kategori ID", anchor="center")
        self.tw_Kategoriler.heading("KategoriAdi", text="Kategori Adı")
        self.tw_Kategoriler.column("KategoriID", width=80)
        self.tw_Kategoriler.column("KategoriAdi", width=150)

        self.txtKategoriID = tk.StringVar()
        self.txtKategoriAdi = tk.StringVar()

        alt = ctk.CTkFrame(self)
        alt.grid(row=1, column=0, columnspan=4, padx=2, pady=2, sticky="ew")
        alt.grid_columnconfigure(1, weight=1)
        alt.grid_columnconfigure(3, weight=1)
        ctk.CTkLabel(alt, text="Kategori ID:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=200, state="readonly", textvariable=self.txtKategoriID).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkLabel(alt, text="Kategori Adı:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=200, textvariable=self.txtKategoriAdi).grid(row=1, column=3, padx=5, pady=5, sticky="ew")

        butonlar = ctk.CTkFrame(self)
        butonlar.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        butonlar.grid_columnconfigure((0, 1, 2), weight=1)
        ctk.CTkButton(butonlar, text="Yeni Kayıt Ekle", command=self.reset_fields, hover_color="lightgreen").grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(butonlar, text="Ekle/Güncelle", command=self.save_category, hover_color="lightgreen").grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(butonlar, text="Sil", command=self.delete_category, hover_color="lightgreen").grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    def bind_events(self):
        self.tw_Kategoriler.bind("<ButtonRelease-1>", self.on_treeview_select)

    def list_categories(self):
        try:
            self.tw_Kategoriler.delete(*self.tw_Kategoriler.get_children())
            data = vt.KategoriListesi()
            gf.PopulateTreeview(self.tw_Kategoriler, data)
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Kategori listesi alınırken hata oluştu:\n{str(e)}")

    def reset_fields(self):
        self.txtKategoriID.set("-1")
        self.txtKategoriAdi.set("")

    def save_category(self):
        try:
            if self.txtKategoriAdi.get() == "":
                mb.showwarning("Uyarı", f"Sayın {gf.kullaniciAdi} Lütfen tüm alanları doldurunuz!")
                return
            vt.KategoriEkleGuncelle(
                self.txtKategoriID.get(),
                self.txtKategoriAdi.get()
            )
            self.list_categories()
            self.reset_fields()
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Kategori kaydedilirken hata oluştu:\n{str(e)}")

    def delete_category(self):
        try:
            if self.txtKategoriID.get() == "-1":
                mb.showwarning("Uyarı", f"Sayın {gf.kullaniciAdi} Lütfen bir kategori seçiniz!")
                return
            if not mb.askyesno("Silme Onayı", f"Sayın {gf.kullaniciAdi} Seçili kategoriyi silmek istediğinizden emin misiniz?"):
                return
            vt.KategoriSil(self.txtKategoriID.get())
            self.list_categories()
            self.reset_fields()
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Kategori silinirken hata oluştu:\n{str(e)}")

    def on_treeview_select(self, event):
        selected_item = self.tw_Kategoriler.selection()
        if selected_item:
            item = self.tw_Kategoriler.item(selected_item)
            self.txtKategoriID.set(item["values"][0])
            self.txtKategoriAdi.set(item["values"][1])
