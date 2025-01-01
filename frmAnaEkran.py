import customtkinter as ctk
import Fonksiyonlar.GenelFonksiyonlar as gf
import frmUye
import frmKullanicilar
import frmYazarlar
import frmKitaplar
import frmYayincilar
import frmKategoriler
import frmOdunc
import frmKitapGeciktirenler

class AnaEkran(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        gf.CenterWindow(self, 400, 400)
        self.title("Ana Ekran")
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        ctk.CTkLabel(
            self, text=f"Hoş Geldiniz Sayın {gf.kullaniciAdi}", font=("Arial", 16)
        ).grid(row=0, column=0, columnspan=2, pady=20, sticky="ew")

        buttons = [
            ("Kullanıcı İşlemleri", frmKullanicilar.Kullanicilar),
            ("Üye İşlemleri", frmUye.Uye),
            ("Yazar İşlemleri", frmYazarlar.Yazarlar),
            ("Kategori İşlemleri", frmKategoriler.Kategoriler),
            ("Yayıncı İşlemleri", frmYayincilar.Yayincilar),
            ("Kitap İşlemleri", frmKitaplar.Kitaplar),
            ("Ödünç İşlemleri", frmOdunc.Odunc),
            ("Kitap Geciktirenler", frmKitapGeciktirenler.KitapGeciktirenler),
        ]

        for i, (text, form) in enumerate(buttons):
            row, column = divmod(i, 2)
            ctk.CTkButton(self, text=text, command=lambda f=form: f(self).grab_set()).grid(row=row + 1, column=column, padx=5, pady=10, sticky="ew")

        ctk.CTkButton(self, text="Çıkış", command=self.quit).grid(row=(len(buttons) // 2) + 1, column=0, columnspan=2, pady=10, sticky="ew")

    def on_close(self):
        self.quit()
