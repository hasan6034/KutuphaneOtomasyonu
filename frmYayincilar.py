import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import Fonksiyonlar.GenelFonksiyonlar as gf
import Fonksiyonlar.Veritabani as vt

class Yayincilar(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        gf.CenterWindow(self, 700, 700)
        self.title("Yayınevi İşlemleri")

        self.create_widgets()
        self.bind_events()
        self.reset_fields()
        self.list_publishers()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def create_widgets(self):
        self.create_treeview()
        self.create_form()
        self.create_buttons()

    def create_treeview(self):
        self.tw_Yayincilar = ttk.Treeview(
            self,
            columns=("YayinciID", "YayinciAdi", "Adres"),
            show="headings",
        )
        self.tw_Yayincilar.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

        for col, text, width in [("YayinciID", "Yayıncı ID", 80), ("YayinciAdi", "Yayıncı Adı", 150), ("Adres", "Adres", 200)]:
            self.tw_Yayincilar.heading(col, text=text, anchor="center")
            self.tw_Yayincilar.column(col, width=width)

    def create_form(self):
        self.txtYayinciID = tk.StringVar()
        self.txtYayinciAdi = tk.StringVar()
        self.txtAdres = tk.StringVar()

        form_frame = ctk.CTkFrame(self)
        form_frame.grid(row=1, column=0, columnspan=4, padx=2, pady=2, sticky="ew")
        form_frame.grid_columnconfigure(1, weight=1)
        form_frame.grid_columnconfigure(3, weight=1)

        for row, (label_text, var, col, colspan) in enumerate([
            ("Yayıncı ID:", self.txtYayinciID, 1, 1),
            ("Yayıncı Adı:", self.txtYayinciAdi, 1, 1),
            ("Adres:", self.txtAdres, 1, 3)
        ]):
            ctk.CTkLabel(form_frame, text=label_text).grid(row=row, column=0, padx=5, pady=5, sticky="w")
            ctk.CTkEntry(form_frame, width=200, textvariable=var, state="readonly" if label_text == "Yayıncı ID:" else "normal").grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="ew")

    def create_buttons(self):
        button_frame = ctk.CTkFrame(self)
        button_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        button_frame.grid_columnconfigure((0, 1, 2), weight=1)

        for col, (text, command) in enumerate([
            ("Yeni Kayıt Ekle", self.reset_fields),
            ("Ekle/Güncelle", self.save_publisher),
            ("Sil", self.delete_publisher)
        ]):
            ctk.CTkButton(button_frame, text=text, command=command).grid(row=0, column=col, padx=5, pady=5, sticky="ew")

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
        if not self.txtYayinciAdi.get() or not self.txtAdres.get():
            mb.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz!")
            return
        try:
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
        if self.txtYayinciID.get() == "-1":
            mb.showwarning("Uyarı", "Lütfen bir yayıncı seçiniz!")
            return
        if not mb.askyesno("Silme Onayı", "Seçili yayıncıyı silmek istediğinizden emin misiniz?"):
            return
        try:
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
