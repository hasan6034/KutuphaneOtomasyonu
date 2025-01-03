import customtkinter as ctk
import tkinter.messagebox as mb
import Fonksiyonlar.GenelFonksiyonlar as gf
import Fonksiyonlar.Veritabani as vt
import frmAnaEkran as ae

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Giriş Ekranı")
        self.iconbitmap("icon.ico")
        gf.CenterWindow(self, 600, 300)
        self.create_widgets()

    def create_widgets(self):
        frame = ctk.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew", pady=20, padx=40)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(
            frame,
            text="Merhaba KMU Kütüphane Sistemine Hoşgeldiniz\nLütfen Giriş Yapınız!!!",
            font=("Arial", 16, "bold")
        )
        label.grid(row=0, column=0, pady=20, padx=10)

        self.user_entry = ctk.CTkEntry(frame, placeholder_text="Kullanıcı Adı", width=200)
        self.user_entry.grid(row=1, column=0, pady=12, padx=10)

        self.user_pass = ctk.CTkEntry(frame, placeholder_text="Şifre", show="*", width=200)
        self.user_pass.grid(row=2, column=0, pady=12, padx=10)

        self.user_entry.insert(0, "hasan")
        self.user_pass.insert(0, "1234")

        button = ctk.CTkButton(
            frame,
            text="Giriş Yap",
            command=self.login,
            width=200,
            height=40,
            corner_radius=10
        )
        button.grid(row=3, column=0, pady=20, padx=10)

    def login(self):
        username = self.user_entry.get()
        password = self.user_pass.get()

        if not username or not password:
            mb.showwarning("Uyarı", "Kullanıcı adı ve şifre boş bırakılamaz!")
            return

        if vt.Login(username, password):
            self.withdraw()
            ae.AnaEkran(self)
        else:
            mb.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
