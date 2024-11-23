import customtkinter as ctk
import Fonksiyonlar.GenelFonksiyonlar as gf
import frmUye
import frmKullanicilar


class AnaEkran(ctk.CTkToplevel):
    def __init__(self, master=None):

        def FormUyeAc():
            frmUye.Uye(self).grab_set()
        
        def FormKullanicilarAc():
            frmKullanicilar.Kullanicilar(self).grab_set()

        super().__init__(master)
        ctk.set_default_color_theme("green")
        gf.CenterWindow(self, 400, 300)
        self.title("Ana Ekran")

        # Pencere kapatıldığında Programı kapat
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Arayüz elemanları
        ctk.CTkLabel(
            self, text=f"Hoş Geldiniz Sayın {gf.kullaniciAdi}", font=("Arial", 16)
        ).pack(pady=20)
        ctk.CTkButton(self, text="Kullanıcı İşlemleri", command=lambda: FormKullanicilarAc()).pack(pady=10)
        ctk.CTkButton(self, text="Üye İşlemleri", command=lambda: FormUyeAc()).pack(pady=10)
        ctk.CTkButton(self, text="Kitap İşlemleri").pack(pady=10)
        ctk.CTkButton(self, text="Çıkış", command=self.quit).pack(pady=10)

    def on_close(self):
        self.quit()
