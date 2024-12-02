import customtkinter as ctk
import tkinter.messagebox as mb
import GenelFonksiyonlar as gf
import frmKitap as fk
import frmUye as uye


class AnaEkran(ctk.CTkToplevel):  # Toplevel'den türetildi
    def __init__(self, master=None):
        def KitapIslemleri():
            fk.Kitap(self).grab_set()

        def YazarIslemleri():
            pass

        def YetkiliIslemleri():
            pass

        def UyeIslemleri():
            uye.Uye(self).grab_set()

        super().__init__(master)
        ctk.set_default_color_theme("green")
        gf.center_window(self, 400, 300)
        self.title("Ana Ekran")

        # Kapatma olayını özelleştir
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Arayüz elemanları
        ctk.CTkLabel(
            self, text=f"Hoş Geldiniz Sayın {gf.kullaniciAdi}", font=("Arial", 16)
        ).pack(pady=20)
        ctk.CTkButton(
            self, text="Kitap İşlemleri", command=lambda: KitapIslemleri()
        ).pack()
        ctk.CTkButton(
            self, text="Yazar İşlemleri", command=lambda: YazarIslemleri()
        ).pack(pady=10)
        ctk.CTkButton(
            self, text="Yetkili Kullanıcı İşlemleri", command=lambda: YetkiliIslemleri()
        ).pack(pady=10)
        ctk.CTkButton(self, text="Üye İşlemleri", command=lambda: UyeIslemleri()).pack(
            pady=10
        )
        ctk.CTkButton(self, text="Çıkış", command=self.quit).pack()

    def on_close(self):
        self.quit()  # Pencereyi kapat
