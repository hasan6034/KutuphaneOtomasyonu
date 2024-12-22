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
        ctk.set_default_color_theme("green")
        gf.CenterWindow(self, 880, 700)
        self.title("Kitap İşlemleri")

        self.dataYazar = vt.YazarListesi()
        self.dataYazar.insert(0, (-1, "Seçiniz"))

        self.dataYayinci = vt.YayinciListesi()
        self.dataYayinci.insert(0, (-1, "Seçiniz"))

        self.dataKategori = vt.KategoriListesi()
        self.dataKategori.insert(0, (-1, "Seçiniz"))

        self.displayYazar = [row[1] for row in self.dataYazar]
        self.displayYayinci = [row[1] for row in self.dataYayinci]
        self.displayKategori = [row[1] for row in self.dataKategori]

        self.valueYazar = {row[1]: row[0] for row in self.dataYazar}
        self.valueYayinci = {row[1]: row[0] for row in self.dataYayinci}
        self.valueKategori = {row[1]: row[0] for row in self.dataKategori}

        self.create_widgets()
        self.Listele()
        self.YeniKayit()

    def create_widgets(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.tw_Kitaplar = ttk.Treeview(
            self,
            columns=("KitapID", "KitapAdi", "YazarAdi", "YayinciAdi", "KategoriAdi", "BasimTarihi", "SayfaSayisi"),
            show="headings",
        )
        self.tw_Kitaplar.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

        for col in self.tw_Kitaplar["columns"]:
            self.tw_Kitaplar.heading(col, text=col.replace("Adi", " Adı").replace("ID", " ID"), anchor="center")
            self.tw_Kitaplar.column(col, width=130 if col != "KitapID" else 80)

        self.tw_Kitaplar.bind("<ButtonRelease-1>", self.TreeviewSelectedItem)

        alt = ctk.CTkFrame(self)
        alt.grid(row=1, column=0, columnspan=4, padx=2, pady=2, sticky="ew")

        self.txtKitapID = tk.StringVar()
        self.txtKitapAdi = tk.StringVar()
        self.txtBasimTarihi = tk.StringVar()
        self.txtSayfaSayisi = tk.StringVar()
        self.txtKategoriAdi = tk.StringVar()
        self.txtYazarAdi = tk.StringVar()
        self.txtYayinciAdi = tk.StringVar()

        self.create_form(alt)
        self.create_buttons()

    def create_form(self, parent):
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)
        parent.grid_columnconfigure(3, weight=1)

        form_labels = ["Kitap ID:", "Kitap Adı:", "Yazar Adı:", "Yayıncı Adı:", "Kategori Adı:", "Basım Tarihi:", "Sayfa Sayısı:"]
        form_vars = [self.txtKitapID, self.txtKitapAdi, self.txtYazarAdi, self.txtYayinciAdi, self.txtKategoriAdi, self.txtBasimTarihi, self.txtSayfaSayisi]
        form_widgets = [
            ctk.CTkEntry(parent, width=150, state="readonly", textvariable=self.txtKitapID),
            ctk.CTkEntry(parent, width=150, textvariable=self.txtKitapAdi),
            ctk.CTkOptionMenu(parent, width=150, variable=self.txtYazarAdi, values=self.displayYazar),
            ctk.CTkOptionMenu(parent, width=150, variable=self.txtYayinciAdi, values=self.displayYayinci),
            ctk.CTkOptionMenu(parent, width=150, variable=self.txtKategoriAdi, values=self.displayKategori),
            tkcal.DateEntry(parent, width=20, textvariable=self.txtBasimTarihi, date_pattern='yyyy-mm-dd'),
            ctk.CTkEntry(parent, width=150, textvariable=self.txtSayfaSayisi)
        ]

        for i, (label, widget) in enumerate(zip(form_labels, form_widgets)):
            ctk.CTkLabel(parent, text=label).grid(row=i // 2 + 1, column=(i % 2) * 2, padx=5, pady=5, sticky="w")
            widget.grid(row=i // 2 + 1, column=(i % 2) * 2 + 1, padx=5, pady=5, sticky="w")

    def create_buttons(self):
        butonlar = ctk.CTkFrame(self)
        butonlar.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        btnYeniKayit = ctk.CTkButton(butonlar, text="Yeni Kayıt Ekle", command=self.YeniKayit)
        btnYeniKayit.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        btnEkle = ctk.CTkButton(butonlar, text="Ekle/Güncelle", command=self.Kaydet)
        btnEkle.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        btnSil = ctk.CTkButton(butonlar, text="Sil", command=self.Sil)
        btnSil.grid(row=0, column=2, padx=5, pady=5, sticky="w")

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
                self.valueYazar.get(self.txtYazarAdi.get()),
                self.valueYayinci.get(self.txtYayinciAdi.get()),
                self.valueKategori.get(self.txtKategoriAdi.get()),
                self.txtBasimTarihi.get(),
                self.txtSayfaSayisi.get()
            )
            self.Listele()
            self.YeniKayit()
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Kayıt sırasında hata oluştu:\n{str(e)}")

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
