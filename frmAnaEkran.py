import customtkinter as ctk
import Fonksiyonlar.GenelFonksiyonlar as gf
import frmUye
import frmKullanicilar
import frmYazarlar
import frmKitaplar
import frmYayincilar
import frmKategoriler
import frmOdunc

class AnaEkran(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        ctk.set_default_color_theme("green")
        gf.CenterWindow(self, 500, 600)
        self.title("Ana Ekran")

        # Pencere kapatıldığında Programı kapat
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        def FormUyeAc():
            frmUye.Uye(self).grab_set()
        
        def FormKullanicilarAc():
            frmKullanicilar.Kullanicilar(self).grab_set()

        def FormYazarlarAc():
            frmYazarlar.Yazarlar(self).grab_set()

        def FormKitaplarAc():
            frmKitaplar.Kitaplar(self).grab_set()

        def FormYayincilarAc():
            frmYayincilar.Yayincilar(self).grab_set()

        def FormKategorilerAc():
            frmKategoriler.Kategoriler(self).grab_set()

        def FormOduncAc():
            frmOdunc.Odunc(self).grab_set()

        # Arayüz elemanları
        ctk.CTkLabel(
            self, text=f"Hoş Geldiniz Sayın {gf.kullaniciAdi}", font=("Arial", 16)
        ).pack(pady=20)
        ctk.CTkButton(self, text="Kullanıcı İşlemleri", command=lambda: FormKullanicilarAc()).pack(pady=10)
        ctk.CTkButton(self, text="Üye İşlemleri", command=lambda: FormUyeAc()).pack(pady=10)
        ctk.CTkButton(self, text="Yazar İşlemleri", command= lambda: FormYazarlarAc()).pack(pady=10)
        ctk.CTkButton(self, text="Kitap İşlemleri", command=lambda: FormKitaplarAc()).pack(pady=10)
        ctk.CTkButton(self, text="Yayıncı İşlemleri", command=lambda: FormYayincilarAc()).pack(pady=10)
        ctk.CTkButton(self, text="Kategori İşlemleri", command=lambda: FormKategorilerAc()).pack(pady=10)
        ctk.CTkButton(self, text="Ödünç İşlemleri", command=lambda: FormOduncAc()).pack(pady=10)
        ctk.CTkButton(self, text="Çıkış", command=self.quit).pack(pady=10)

    def on_close(self):
        self.quit()
