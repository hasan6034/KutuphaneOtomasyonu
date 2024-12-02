import pyodbc
import tkinter as tk

conn_str = (
    r"DRIVER={SQL Server};"
    r"SERVER=.;"
    r"DATABASE=Kutuphane;"
    r"Trusted_conneciton=yes;"
)

KULLANICI_GIRIS = "Select * from KullaniciGiris(?,?)"

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


def login(email, sifre):
    cursor.execute(KULLANICI_GIRIS, email, sifre)
    if cursor.rowcount == 0:
        return False
    else:
        return True


def populate_treeview(tree, data):
    for row in data:
        tree.insert("", "end", values=row)


def UyeListesi():
    cursor.execute("Select * from Uyeler")
    return cursor.fetchall()
