import customtkinter as ctk
import tkinter.messagebox as mb
import GenelFonksiyonlar as gf

class Kitap(ctk.CTkToplevel):  # Toplevel'den türetildi
    def __init__(self, master=None):
        super().__init__(master)
        ctk.set_default_color_theme("green")
        gf.center_window(self, 400, 300)
        self.title("Ana Ekran")
        
        # Arayüz elemanları
        ctk.CTkButton(self, text="Çıkış", command=self.quit).pack()