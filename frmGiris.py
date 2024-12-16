import customtkinter as ctk
import tkinter.messagebox as mb
import Fonksiyonlar.GenelFonksiyonlar as gf
import Fonksiyonlar.Veritabani as vt
import frmAnaEkran as ae


# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Giriş Ekranı")
app.iconbitmap("icon.ico")
gf.CenterWindow(app, 400, 300)


# Methods
def login(username, password):
    if username == "" or password == "":
        mb.showwarning("Uyarı", "Kullanıcı adı ve şifre boş bırakılamaz!")
        return

    elif vt.Login(username, password):
        app.withdraw()
        ae.AnaEkran(app)

    else:
        mb.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")


frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill="both", expand=True)

label = ctk.CTkLabel(
    master=frame,
    text="Merhaba KMU Kütüphane Sistemine Hoşgeldiniz\nLütfen Giriş Yapınız!!!",
)
label.pack(pady=12, padx=10)


user_entry = ctk.CTkEntry(master=frame, placeholder_text="Kullanıcı Adı")
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Şifre", show="*")
user_pass.pack(pady=12, padx=10)

user_entry.insert(0, "hasan")
user_pass.insert(0, "1234")

button = ctk.CTkButton(
    master=frame,
    text="Giriş Yap",
    command=lambda: login(user_entry.get(), user_pass.get()),
)
button.pack(pady=12, padx=10)


app.mainloop()
