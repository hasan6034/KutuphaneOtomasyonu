import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import tkcalendar as tkcal
import Fonksiyonlar.GenelFonksiyonlar as gf
import Fonksiyonlar.Veritabani as vt
import tkinter.messagebox as mb
from datetime import datetime

class Kitaplar(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        gf.CenterWindow(self, 880, 700)
        self.title("Kitap İşlemleri")

        self.dataYazar = self.prepare_data(vt.YazarListesi())
        self.dataYayinci = self.prepare_data(vt.YayinciListesi())
        self.dataKategori = self.prepare_data(vt.KategoriListesi())

        self.create_widgets()
        self.Listele()
        self.YeniKayit()

    def prepare_data(self, data):
        data.insert(0, (-1, "Seçiniz"))
        return data

    def create_widgets(self):
        self.configure_grid()
        self.create_treeview()
        self.create_form_frame()
        self.create_buttons_frame()

    def configure_grid(self):
        for i in range(3):
            self.grid_rowconfigure(i, weight=1 if i == 0 else 0)
        self.grid_columnconfigure(0, weight=1)

    def create_treeview(self):
        columns = ("KitapID", "KitapAdi", "YazarAdi", "YayinciAdi", "KategoriAdi", "BasimTarihi", "SayfaSayisi")
        self.tw_Kitaplar = ttk.Treeview(self, columns=columns, show="headings")
        self.tw_Kitaplar.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

        for col in columns:
            self.tw_Kitaplar.heading(col, text=col.replace("Adi", " Adı").replace("ID", " ID"), anchor="center")
            self.tw_Kitaplar.column(col, width=130 if col != "KitapID" else 80)

        self.tw_Kitaplar.bind("<ButtonRelease-1>", self.TreeviewSelectedItem)

    def create_form_frame(self):
        form_frame = ctk.CTkFrame(self)
        form_frame.grid(row=1, column=0, columnspan=4, padx=2, pady=2, sticky="ew")

        self.txtKitapID = tk.StringVar()
        self.txtKitapAdi = tk.StringVar()
        self.txtBasimTarihi = tk.StringVar()
        self.txtSayfaSayisi = tk.StringVar()
        self.txtKategoriAdi = tk.StringVar()
        self.txtYazarAdi = tk.StringVar()
        self.txtYayinciAdi = tk.StringVar()

        form_labels = ["Kitap ID:", "Kitap Adı:", "Yazar Adı:", "Yayıncı Adı:", "Kategori Adı:", "Basım Tarihi:", "Sayfa Sayısı:"]
        form_vars = [self.txtKitapID, self.txtKitapAdi, self.txtYazarAdi, self.txtYayinciAdi, self.txtKategoriAdi, self.txtBasimTarihi, self.txtSayfaSayisi]
        form_widgets = [
            ctk.CTkEntry(form_frame, width=150, state="readonly", textvariable=self.txtKitapID),
            ctk.CTkEntry(form_frame, width=150, textvariable=self.txtKitapAdi),
            ctk.CTkOptionMenu(form_frame, width=150, variable=self.txtYazarAdi, values=[row[1] for row in self.dataYazar]),
            ctk.CTkOptionMenu(form_frame, width=150, variable=self.txtYayinciAdi, values=[row[1] for row in self.dataYayinci]),
            ctk.CTkOptionMenu(form_frame, width=150, variable=self.txtKategoriAdi, values=[row[1] for row in self.dataKategori]),
            tkcal.DateEntry(form_frame, width=20, textvariable=self.txtBasimTarihi, date_pattern='yyyy-mm-dd'),
            ctk.CTkEntry(form_frame, width=150, textvariable=self.txtSayfaSayisi)
        ]

        for i, (label, widget) in enumerate(zip(form_labels, form_widgets)):
            ctk.CTkLabel(form_frame, text=label).grid(row=i // 2 + 1, column=(i % 2) * 2, padx=5, pady=5, sticky="w")
            widget.grid(row=i // 2 + 1, column=(i % 2) * 2 + 1, padx=5, pady=5, sticky="w")

    def create_buttons_frame(self):
        buttons_frame = ctk.CTkFrame(self)
        buttons_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        buttons = [
            ("Yeni Kayıt Ekle", self.YeniKayit),
            ("Ekle/Güncelle", self.Kaydet),
            ("Sil", self.Sil)
        ]

        for i, (text, command) in enumerate(buttons):
            ctk.CTkButton(buttons_frame, text=text, command=command).grid(row=0, column=i, padx=5, pady=5, sticky="w")

    def Listele(self):
        try:
            self.tw_Kitaplar.delete(*self.tw_Kitaplar.get_children())
            data = vt.KitapListesi()
            gf.PopulateTreeview(self.tw_Kitaplar, data)
        except Exception as e:
            mb.showerror("Hata", f"Kitap listesi alınırken hata oluştu: {str(e)}")

    def YeniKayit(self):
        self.txtKitapID.set("-1")
        self.txtKitapAdi.set("")
        self.txtBasimTarihi.set(datetime.now().strftime("%Y-%m-%d"))
        self.txtSayfaSayisi.set("")
        self.txtYazarAdi.set("Seçiniz")
        self.txtYayinciAdi.set("Seçiniz")
        self.txtKategoriAdi.set("Seçiniz")

    def Kaydet(self):
        try:
            if any(var.get() in ["", "Seçiniz"] for var in [self.txtKitapAdi, self.txtYazarAdi, self.txtYayinciAdi, self.txtKategoriAdi, self.txtBasimTarihi, self.txtSayfaSayisi]):
                mb.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz!")
                return
            vt.KitapEkleGuncelle(
                self.txtKitapID.get(),
                self.txtKitapAdi.get(),
                self.get_value(self.txtYazarAdi.get(), self.dataYazar),
                self.get_value(self.txtYayinciAdi.get(), self.dataYayinci),
                self.get_value(self.txtKategoriAdi.get(), self.dataKategori),
                self.txtBasimTarihi.get(),
                self.txtSayfaSayisi.get()
            )
            self.Listele()
            self.YeniKayit()
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Kayıt sırasında hata oluştu:\n{str(e)}")

    def get_value(self, key, data):
        return next((row[0] for row in data if row[1] == key), -1)

    def Sil(self):
        try:
            if self.txtKitapID.get() == "-1":
                mb.showwarning("Uyarı", "Lütfen bir üye seçiniz.")
                return
            if not mb.askyesno("Onay", "Bu üyeyi silmek istediğinizden emin misiniz?"):
                return
            vt.KitapSil(self.txtKitapID.get())
            self.Listele()
            self.YeniKayit()
            mb.showinfo("Bilgi", "Üye başarıyla silindi")
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Üye silinirken hata oluştu:\n{str(e)}")

    def TreeviewSelectedItem(self, event):
        selected_item = self.tw_Kitaplar.selection()
        if selected_item:
            item = self.tw_Kitaplar.item(selected_item)
            self.txtKitapID.set(item["values"][0])
            self.txtKitapAdi.set(item["values"][1])
            self.txtYazarAdi.set(item["values"][2])
            self.txtYayinciAdi.set(item["values"][3])
            self.txtKategoriAdi.set(item["values"][4])
            self.txtBasimTarihi.set(item["values"][5])
            self.txtSayfaSayisi.set(item["values"][6])
