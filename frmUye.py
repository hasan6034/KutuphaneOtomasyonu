import customtkinter as ctk
from tkinter import ttk
import tkinter.messagebox as mb
import GenelFonksiyonlar as gf
import Veritabani as vt
import tkinter as tk  # StringVar için gerekli


class Uye(ctk.CTkToplevel):  # Toplevel'den türetildi
    def __init__(self, master=None):
        super().__init__(master)
        ctk.set_default_color_theme("green")
        gf.center_window(self, 700, 600)
        self.title("Üye İşlemleri")

        # Üye işlemleri için fonksiyonlar tanımlanıyor
        def listele():
            try:
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

        def yeni_kayit():
            self.txtUyeID.set("0")
            self.txtAdi.set("")
            self.txtSoyadi.set("")
            self.txtDogumTarihi.set("")
            self.txtAdres.set("")

        def kaydet():
            try:
                vt.UyeKaydet(
                    self.txtUyeID.get(),
                    self.txtAdi.get(),
                    self.txtSoyadi.get(),
                    self.txtDogumTarihi.get(),
                    self.txtAdres.get(),
                )
                listele()
                mb.showinfo("Bilgi", "Kayıt başarıyla eklendi.")
            except Exception as e:
                mb.showerror("Hata", f"Kayıt eklenirken hata oluştu: {str(e)}")

        def sil():
            try:
                vt.UyeSil(self.txtUyeID.get())
                listele()
                mb.showinfo("Bilgi", "Kayıt başarıyla silindi.")
            except Exception as e:
                mb.showerror("Hata", f"Kayıt silinirken hata oluştu: {str(e)}")

        # Arayüz elemanları
        tw_Uyeler = ttk.Treeview(
            self,
            columns=("UyeID", "Adi", "Soyadi", "DogumTarihi", "Adres"),
            show="headings",
        )
        tw_Uyeler.grid(row=0, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

        tw_Uyeler.heading("UyeID", text="Üye ID", anchor="center")
        tw_Uyeler.heading("Adi", text="Adı")
        tw_Uyeler.heading("Soyadi", text="Soyadı")
        tw_Uyeler.heading("DogumTarihi", text="Doğum Tarihi")
        tw_Uyeler.heading("Adres", text="Adres")

        tw_Uyeler.column("UyeID", width=50)
        tw_Uyeler.column("Adi", width=150)
        tw_Uyeler.column("Soyadi", width=150)
        tw_Uyeler.column("DogumTarihi", width=90)
        tw_Uyeler.column("Adres", width=250)

        ctk.CTkLabel(self, text="Üye ID:").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkLabel(self, text="Adı:").grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkLabel(self, text="Soyadı:").grid(
            row=3, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkLabel(self, text="Doğum Tarihi:").grid(
            row=4, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkLabel(self, text="Adres:").grid(
            row=5, column=0, padx=5, pady=5, sticky="w"
        )

        # StringVar ile metin değişkenleri oluşturuluyor
        self.txtUyeID = tk.StringVar()
        self.txtAdi = tk.StringVar()
        self.txtSoyadi = tk.StringVar()
        self.txtDogumTarihi = tk.StringVar()
        self.txtAdres = tk.StringVar()

        # Entry widget'larını oluştur ve textvariable ile bağla
        ctk.CTkEntry(self, state="readonly", textvariable=self.txtUyeID).grid(
            row=1, column=1, padx=5, pady=5, sticky="w"
        )
        ctk.CTkEntry(self, textvariable=self.txtAdi).grid(
            row=2, column=1, padx=5, pady=5, sticky="w"
        )
        ctk.CTkEntry(self, textvariable=self.txtSoyadi).grid(
            row=3, column=1, padx=5, pady=5, sticky="w"
        )
        ctk.CTkEntry(self, textvariable=self.txtDogumTarihi).grid(
            row=4, column=1, padx=5, pady=5, sticky="w"
        )
        ctk.CTkEntry(self, textvariable=self.txtAdres).grid(
            row=5, column=1, padx=5, pady=5, sticky="w"
        )

        self.txtUyeID.set("0")

        ctk.CTkButton(self, text="Yeni Kayıt", command=lambda: yeni_kayit()).grid(
            row=6, column=0, padx=5, pady=5, sticky="w"
        )
        ctk.CTkButton(self, text="Kaydet", command=lambda: kaydet()).grid(
            row=6, column=1, padx=5, pady=5, sticky="w"
        )
        ctk.CTkButton(self, text="Sil", command=lambda: sil()).grid(
            row=6, column=2, padx=5, pady=5, sticky="w"
        )

        listele()

        def on_item_select(event):
            # Tıklanan öğe (satır) hakkında bilgi al
            selected_item = tw_Uyeler.selection()  # Seçilen satırın ID'sini al
            if selected_item:
                item = tw_Uyeler.item(selected_item)
                # StringVar ile değerleri set et
                self.txtUyeID.set(item["values"][0])
                self.txtAdi.set(item["values"][1])
                self.txtSoyadi.set(item["values"][2])
                self.txtDogumTarihi.set(item["values"][3])
                self.txtAdres.set(item["values"][4])

        tw_Uyeler.bind("<ButtonRelease-1>", on_item_select)
