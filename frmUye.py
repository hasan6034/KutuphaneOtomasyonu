import customtkinter as ctk
from tkinter import ttk
import tkinter.messagebox as mb
import Fonksiyonlar.GenelFonksiyonlar as gf
import Fonksiyonlar.Veritabani as vt
import tkinter as tk
import tkcalendar as tkcal
from datetime import datetime


class Uye(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        ctk.set_default_color_theme("green")
        gf.CenterWindow(self, 750, 600)
        self.title("Üye İşlemleri")

        def Listele():
            try:
                tw_Uyeler.delete(*tw_Uyeler.get_children())
                data = vt.UyeListesi()
                for uye in data:
                    tw_Uyeler.insert(
                        "",
                        "end",
                        values=(
                            uye[0],
                            uye[1],
                            uye[2],
                            uye[3],
                            uye[4],
                        ),
                    )
            except Exception as e:
                mb.showerror("Hata", f"Üye listesi alınırken hata oluştu: {str(e)}")

        def YeniKayit():
            self.txtUyeID.set("-1")
            self.txtAdi.set("")
            self.txtTelefon.set("")
            self.txtAdres.set("")
            self.txtKayitTarihi.set(datetime.now().strftime("%Y-%m-%d"))

        def Kaydet():
            try:
                vt.UyeEkleGuncelle(
                    self.txtUyeID.get(),
                    self.txtAdi.get(),
                    self.txtTelefon.get(),
                    self.txtAdres.get(),
                    self.txtKayitTarihi.get(),
                )
                Listele()
                YeniKayit()
                mb.showinfo("Bilgi", "Kayıt başarıyla eklendi.")
            except Exception as e:
                mb.showerror("Hata", f"Kayıt eklenirken hata oluştu: {str(e)}")

        def Sil():
            try:
                if self.txtUyeID.get() == "-1":
                    mb.showwarning("Uyarı", "Lütfen bir üye seçiniz.")
                    return
                if not mb.askyesno("Onay", "Bu üyeyi silmek istediğinizden emin misiniz?"):
                    return
                vt.UyeSil(self.txtUyeID.get())
                Listele()
                YeniKayit()
                mb.showinfo("Bilgi","Üye başarıyla silindi.")
            except Exception as e:
                mb.showerror("Hata", f"Kayıt silinirken hata oluştu: {str(e)}")

        tw_Uyeler = ttk.Treeview(
            self,
            columns=("UyeID", "Adi", "Telefon", "Adres", "KayitTarihi"),
            show="headings",
        )
        tw_Uyeler.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

        tw_Uyeler.heading("UyeID", text="Üye ID", anchor="center")
        tw_Uyeler.heading("Adi", text="Adı")
        tw_Uyeler.heading("Telefon", text="Telefon")
        tw_Uyeler.heading("Adres", text="Adres")
        tw_Uyeler.heading("KayitTarihi", text="Kayıt Tarihi")

        tw_Uyeler.column("UyeID", width=50)
        tw_Uyeler.column("Adi", width=200)
        tw_Uyeler.column("Telefon", width=100)
        tw_Uyeler.column("Adres", width=250)
        tw_Uyeler.column("KayitTarihi", width=100)

        ctk.CTkLabel(self, text="Üye ID:").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkLabel(self, text="Adı:").grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkLabel(self, text="Telefon:").grid(
            row=3, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkLabel(self, text="Adres:").grid(
            row=4, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkLabel(self, text="Kayıt Tarihi:").grid(
            row=5, column=0, padx=5, pady=5, sticky="w"
        )

        self.txtUyeID = tk.StringVar()
        self.txtAdi = tk.StringVar()
        self.txtTelefon = tk.StringVar()
        self.txtAdres = tk.StringVar()
        self.txtKayitTarihi = tk.StringVar()

        ctk.CTkEntry(self, state="readonly", textvariable=self.txtUyeID).grid(
            row=1, column=1, padx=5, pady=5, sticky="w"
        )
        ctk.CTkEntry(self, textvariable=self.txtAdi).grid(
            row=2, column=1, padx=5, pady=5, sticky="w"
        )
        ctk.CTkEntry(self, textvariable=self.txtTelefon).grid(
            row=3, column=1, padx=5, pady=5, sticky="w"
        )
        ctk.CTkEntry(self, textvariable=self.txtAdres).grid(
            row=4, column=1, padx=5, pady=5, sticky="w"
        )
        self.date_entry = tkcal.DateEntry(self, textvariable=self.txtKayitTarihi, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        self.txtUyeID.set("-1")

        ctk.CTkButton(self, text="Yeni Kayıt", command=lambda: YeniKayit()).grid(
            row=6, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkButton(self, text="Kaydet", command=lambda: Kaydet()).grid(
            row=6, column=1, padx=5, pady=5, sticky="w"
        )
        ctk.CTkButton(self, text="Sil", command=lambda: Sil()).grid(
            row=6, column=2, padx=5, pady=5, sticky="w"
        )

        Listele()

        def TreeviewSelectedItem(event):
            selected_item = tw_Uyeler.selection()
            if selected_item:
                item = tw_Uyeler.item(selected_item)
                self.txtUyeID.set(item["values"][0])
                self.txtAdi.set(item["values"][1])
                self.txtTelefon.set(item["values"][2])
                self.txtAdres.set(item["values"][3])
                self.txtKayitTarihi.set(item["values"][4])

        tw_Uyeler.bind("<ButtonRelease-1>", TreeviewSelectedItem)
