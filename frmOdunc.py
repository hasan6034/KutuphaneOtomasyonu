import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import Fonksiyonlar.GenelFonksiyonlar as gf
import Fonksiyonlar.Veritabani as vt
from datetime import datetime, timedelta
import tkcalendar as tkcal

class Odunc(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        ctk.set_default_color_theme("blue")
        gf.CenterWindow(self, 700, 700)
        self.title("Ödünç İşlemleri")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.initialize_data()
        self.create_widgets()
        self.populate_comboboxes()
        self.new_record()
        self.list_records()

    def initialize_data(self):
        try:
            self.dataUyeler = vt.UyeListesi()
            self.dataUyeler.insert(0, (-1, "Seçiniz"))

            self.dataKitaplar = vt.KitapListesi()
            self.dataKitaplar.insert(0, (-1, "Seçiniz"))

            self.dataAlindiMi = [(1, "Alındı"), (0, "Alınmadı")]

            self.displayUyeler = [row[1] for row in self.dataUyeler]
            self.displayKitaplar = [row[1] for row in self.dataKitaplar]
            self.displayAlindiMi = [row[1] for row in self.dataAlindiMi]

            self.valueUyeler = {row[1]: row[0] for row in self.dataUyeler}
            self.valueKitaplar = {row[1]: row[0] for row in self.dataKitaplar}
            self.valueAlindiMi = {row[1]: row[0] for row in self.dataAlindiMi}
        except Exception as e:
            mb.showerror("Hata", f"Ödünç listesi alınırken hata oluştu: {str(e)}")

    def create_widgets(self):
        self.create_treeview()
        self.create_form()
        self.create_buttons()

    def create_treeview(self):
        self.tw_Kategoriler = ttk.Treeview(
            self,
            columns=("IslemID", "UyeAdi", "KitapAdi", "OduncTarihi", "IadeTarihi", "AlindiMi"),
            show="headings",
        )
        self.tw_Kategoriler.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

        for col in self.tw_Kategoriler["columns"]:
            self.tw_Kategoriler.heading(col, text=col, anchor="center")
            self.tw_Kategoriler.column(col, width=150)

        self.tw_Kategoriler.column("IslemID", width=80)
        self.tw_Kategoriler.column("AlindiMi", width=80)
        self.tw_Kategoriler.bind("<ButtonRelease-1>", self.treeview_selected_item)

    def create_form(self):
        self.txtIslemID = tk.StringVar()
        self.txtUyeAdi = tk.StringVar()
        self.txtKitapAdi = tk.StringVar()
        self.txtOduncTarihi = tk.StringVar()
        self.txtIadeTarihi = tk.StringVar()
        self.txtAlindiMi = tk.StringVar()

        form_frame = ctk.CTkFrame(self)
        form_frame.grid(row=1, column=0, columnspan=4, padx=2, pady=2, sticky="ew")
        form_frame.grid_columnconfigure(1, weight=1)
        form_frame.grid_columnconfigure(3, weight=1)

        self.create_label_entry(form_frame, "İşlem ID:", self.txtIslemID, 1, 0, readonly=True)
        self.create_label_combobox(form_frame, "Üye Adı:", self.txtUyeAdi, 1, 2)
        self.create_label_combobox(form_frame, "Kitap Adı:", self.txtKitapAdi, 2, 0)
        self.create_label_dateentry(form_frame, "Ödünç Tarihi:", self.txtOduncTarihi, 2, 2)
        self.create_label_dateentry(form_frame, "İade Tarihi:", self.txtIadeTarihi, 3, 0)
        self.create_label_combobox(form_frame, "Alındı mı:", self.txtAlindiMi, 3, 2)

    def create_buttons(self):
        button_frame = ctk.CTkFrame(self)
        button_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_columnconfigure(2, weight=1)

        self.create_button(button_frame, "Yeni Kayıt Ekle", self.new_record, 0, 0)
        self.create_button(button_frame, "Ekle/Güncelle", self.save_record, 0, 1)
        self.create_button(button_frame, "Sil", self.delete_record, 0, 2)

    def create_label_entry(self, parent, text, variable, row, column, readonly=False):
        ctk.CTkLabel(parent, text=text).grid(row=row, column=column, padx=5, pady=5, sticky="w")
        state = "readonly" if readonly else "normal"
        ctk.CTkEntry(parent, width=200, state=state, textvariable=variable).grid(row=row, column=column + 1, padx=5, pady=5, sticky="ew")

    def create_label_combobox(self, parent, text, variable, row, column):
        ctk.CTkLabel(parent, text=text).grid(row=row, column=column, padx=5, pady=5, sticky="w")
        cmb = ctk.CTkOptionMenu(parent, width=200, variable=variable)
        cmb.grid(row=row, column=column + 1, padx=5, pady=5, sticky="ew")
        setattr(self, f"cmb_{text.split()[0].lower()}", cmb)

    def create_label_dateentry(self, parent, text, variable, row, column):
        ctk.CTkLabel(parent, text=text).grid(row=row, column=column, padx=5, pady=5, sticky="w")
        tkcal.DateEntry(parent, width=30, textvariable=variable, date_pattern='yyyy-mm-dd').grid(row=row, column=column + 1, padx=5, pady=5, sticky="ew")

    def create_button(self, parent, text, command, row, column):
        ctk.CTkButton(parent, text=text, command=command).grid(row=row, column=column, padx=5, pady=5, sticky="ew")

    def populate_comboboxes(self):
        self.cmb_üye.configure(values=self.displayUyeler)
        self.cmb_üye.set("Seçiniz")

        self.cmb_kitap.configure(values=self.displayKitaplar)
        self.cmb_kitap.set("Seçiniz")

        self.cmb_alındı.configure(values=self.displayAlindiMi)
        self.cmb_alındı.set("Alınmadı")

    def list_records(self):
        try:
            self.tw_Kategoriler.delete(*self.tw_Kategoriler.get_children())
            data = vt.OduncListesi()
            gf.PopulateTreeview(self.tw_Kategoriler, data)
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Ödünç listesi alınırken hata oluştu:\n{str(e)}")

    def new_record(self):
        self.txtIslemID.set("-1")
        self.txtUyeAdi.set("Seçiniz")
        self.txtKitapAdi.set("Seçiniz")
        self.txtOduncTarihi.set(datetime.now().strftime("%Y-%m-%d"))
        self.txtIadeTarihi.set((datetime.now() + timedelta(weeks=1)).strftime("%Y-%m-%d"))

    def save_record(self):
        try:
            if self.txtUyeAdi.get() == "Seçiniz" or self.txtKitapAdi.get() == "Seçiniz" or not self.txtOduncTarihi.get() or not self.txtIadeTarihi.get():
                mb.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz!")
                return
            vt.OduncEkleGuncelle(
                self.txtIslemID.get(),
                self.valueUyeler[self.txtUyeAdi.get()],
                self.valueKitaplar[self.txtKitapAdi.get()],
                gf.kullaniciID,
                self.txtOduncTarihi.get(),
                self.txtIadeTarihi.get(),
                self.valueAlindiMi[self.txtAlindiMi.get()]
            )
            self.list_records()
            self.new_record()
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Ödünç kaydedilirken hata oluştu:\n{str(e)}")

    def delete_record(self):
        try:
            if self.txtIslemID.get() == "-1":
                mb.showwarning("Uyarı", "Silinecek kaydı seçiniz!")
                return
            if not mb.askyesno("Onay", "Seçili ödünç kaydı silinsin mi?"):
                return
            vt.OduncSil(self.txtIslemID.get())
            self.list_records()
            self.new_record()
        except Exception as e:
            mb.showerror("Hata", f"Sayın {gf.kullaniciAdi} Ödünç silinirken hata oluştu:\n{str(e)}")

    def treeview_selected_item(self, event):
        selected_item = self.tw_Kategoriler.selection()
        if selected_item:
            item = self.tw_Kategoriler.item(selected_item)
            self.txtIslemID.set(item["values"][0])
            self.txtUyeAdi.set(item["values"][1])
            self.txtKitapAdi.set(item["values"][2])
            self.txtOduncTarihi.set(item["values"][3])
            self.txtIadeTarihi.set(item["values"][4])
            self.txtAlindiMi.set(item["values"][5])
