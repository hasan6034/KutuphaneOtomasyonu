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

        dataYazar = vt.YazarListesi()
        dataYazar.insert(0, (-1, "Seçiniz")) # İlk sıraya "Seçiniz" ekle

        dataYayinci = vt.YayinciListesi()
        dataYayinci.insert(0, (-1, "Seçiniz")) # İlk sıraya "Seçiniz" ekle

        dataKategori = vt.KategoriListesi()
        dataKategori.insert(0, (-1, "Seçiniz")) # İlk sıraya "Seçiniz" ekle

        displayYazar = [row[1] for row in dataYazar] # Yazar Adını al
        displayYayinci = [row[1] for row in dataYayinci] # Yayıncı Adını al
        displayKategori = [row[1] for row in dataKategori]  # Kategori Adını al

        valueYazar = {row[1]: row[0] for row in dataYazar} # Yazar ID al | Bunu kitabı kaydetmek için kullanacağız
        valueYayinci = {row[1]: row[0] for row in dataYayinci} # Yayıncı ID al | Bunu kitabı kaydetmek için kullanacağız
        valueKategori = {row[1]: row[0]  for row in dataKategori} # Kategori ID al | Bunu kitabı kaydetmek için kullanacağız

        def Listele():
            try:
                tw_Kitaplar.delete(*tw_Kitaplar.get_children())
                data = vt.KitapListesi()
                gf.PopulateTreeview(tw_Kitaplar, data)
            except Exception as e:
                mb.showerror("Hata", f"Kitap listesi alınırken hata oluştu: {str(e)}")

        def YeniKayit():
            txtKitapID.set("-1")
            txtKitapAdi.set("")
            txtBasimTarihi.set(datetime.now().strftime("%Y-%m-%d"))
            txtSayfaSayisi.set("")
            txtStokAdedi.set("")
            cmb1.set("Seçiniz")
            cmb2.set("Seçiniz")
            cmb3.set("Seçiniz")
            
        def Kaydet():
            try:
                if txtKitapAdi.get() == "" or txtYazarAdi.get() == "Seçiniz" or txtYayinciAdi.get() == "Seçiniz" or txtKategoriAdi.get() == "Seçiniz" or txtBasimTarihi.get() == "" or txtSayfaSayisi.get() == "" or txtStokAdedi.get() == "":
                    mb.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz!")
                    return
                vt.KitapEkleGuncelle(
                    txtKitapID.get(),
                    txtKitapAdi.get(),
                    valueYazar.get(txtYazarAdi.get()),
                    valueYayinci.get(txtYayinciAdi.get()),
                    valueKategori.get(txtKategoriAdi.get()),
                    txtBasimTarihi.get(),
                    txtSayfaSayisi.get(),
                    txtStokAdedi.get()
                )
                Listele()
                YeniKayit()
            except Exception as e:
                mb.showerror("Hata", f"Kayıt sırasında hata oluştu: {str(e)}")

        def Sil():
                try:
                    if txtKitapID.get() == "-1":
                        mb.showwarning("Uyarı", "Lütfen bir üye seçiniz.")
                        return
                    if not mb.askyesno("Onay", "Bu üyeyi silmek istediğinizden emin misiniz?"):
                        return
                    vt.KitapSil(txtKitapID.get())
                    Listele()
                    YeniKayit()
                    mb.showinfo("Bilgi","Üye başarıyla silindi")
                except Exception as e:
                    mb.showerror("Hata", f"Üye silinirken hata oluştu: {str(e)}")

        tw_Kitaplar = ttk.Treeview(
            self,
            columns=("KitapID", "KitapAdi", "YazarAdi","YayinciAdi","KategoriAdi","BasimTarihi","SayfaSayisi","StokAdedi"),
            show="headings",
        )
        tw_Kitaplar.grid(
            row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew"
        )

        tw_Kitaplar.heading("KitapID", text="Kitap ID", anchor="center")
        tw_Kitaplar.heading("KitapAdi", text="Kitap Adı")
        tw_Kitaplar.heading("YazarAdi", text="Yazar Adı")
        tw_Kitaplar.heading("YayinciAdi", text="Yayıncı Adı")
        tw_Kitaplar.heading("KategoriAdi", text="Kategori Adı")
        tw_Kitaplar.heading("BasimTarihi", text="Basım Tarihi")
        tw_Kitaplar.heading("SayfaSayisi", text="Sayfa Sayısı")
        tw_Kitaplar.heading("StokAdedi", text="Stok Adedi")

        tw_Kitaplar.column("KitapID", width=80)
        tw_Kitaplar.column("KitapAdi", width=130)
        tw_Kitaplar.column("YazarAdi", width=130)
        tw_Kitaplar.column("YayinciAdi", width=130)
        tw_Kitaplar.column("KategoriAdi", width=100)
        tw_Kitaplar.column("BasimTarihi", width=100)
        tw_Kitaplar.column("SayfaSayisi", width=80)
        tw_Kitaplar.column("StokAdedi", width=80)

        Listele()
        alt = ctk.CTkFrame(self)
        alt.grid(row=1, column=0, columnspan=4, padx=2, pady=2, sticky="ew")

        txtKitapID = tk.StringVar()
        txtKitapAdi = tk.StringVar()
        txtBasimTarihi = tk.StringVar()
        txtSayfaSayisi = tk.StringVar()
        txtStokAdedi = tk.StringVar()

        txtKategoriAdi = tk.StringVar()
        txtYazarAdi = tk.StringVar()
        txtYayinciAdi = tk.StringVar()

        ctk.CTkLabel(alt, text="Kitap ID:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=150, state="readonly", textvariable=txtKitapID).grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(alt, text="Kitap Adı:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=150, textvariable= txtKitapAdi).grid(row=1, column=3, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(alt, text="Yazar Adı:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        cmb1 = ctk.CTkOptionMenu(alt, width=150, variable=txtYazarAdi)
        cmb1.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(alt, text="Yayıncı Adı:").grid(row=2, column=2, padx=5, pady=5, sticky="w")
        cmb2 = ctk.CTkOptionMenu(alt, width=150, variable=txtYayinciAdi)
        cmb2.grid(row=2, column=3, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(alt, text="Kategori Adı:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        cmb3 = ctk.CTkOptionMenu(alt, width=150, variable=txtKategoriAdi)
        cmb3.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(alt, text="Basım Tarihi:").grid(row=3, column=2, padx=5, pady=5, sticky="w")
        tkcal.DateEntry(alt, width= 20, textvariable=txtBasimTarihi, date_pattern='yyyy-mm-dd').grid(row=3, column=3, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(alt, text="Sayfa Sayısı:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=150, textvariable= txtSayfaSayisi).grid(row=4, column=1, padx=2, pady=2, sticky="w")

        ctk.CTkLabel(alt, text="Stok Adedi:").grid(row=4, column=2, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(alt, width=150, textvariable= txtStokAdedi).grid(row=4, column=3, padx=2, pady=2, sticky="w")

        butonlar = ctk.CTkFrame(self)
        butonlar.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        btnYeniKayit = ctk.CTkButton(butonlar, text="Yeni Kayıt Ekle", command=lambda: YeniKayit())
        btnYeniKayit.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        btnEkle = ctk.CTkButton(butonlar, text="Ekle/Güncelle", command=lambda: Kaydet())
        btnEkle.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        btnSil = ctk.CTkButton(butonlar, text="Sil", command=lambda: Sil())
        btnSil.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        YeniKayit()

        cmb1.configure(values=displayYazar)
        cmb1.set("Seçiniz")

        cmb2.configure(values=displayYayinci)
        cmb2.set("Seçiniz")

        cmb3.configure(values=displayKategori)
        cmb3.set("Seçiniz")
        
        def TreeviewSelectedItem(event):
            selected_item = tw_Kitaplar.selection()
            if selected_item:
                item = tw_Kitaplar.item(selected_item)
                txtKitapID.set(item["values"][0])
                txtKitapAdi.set(item["values"][1])
                txtYazarAdi.set(item["values"][2])
                txtYayinciAdi.set(item["values"][3])
                txtKategoriAdi.set(item["values"][4])
                txtBasimTarihi.set(item["values"][5])
                txtSayfaSayisi.set(item["values"][6])
                txtStokAdedi.set(item["values"][7])

        tw_Kitaplar.bind("<ButtonRelease-1>", TreeviewSelectedItem)
