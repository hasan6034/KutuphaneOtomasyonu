import pyodbc
import Fonksiyonlar.GenelFonksiyonlar as gf

conn_str = (
    r"DRIVER={SQL Server};"
    r"SERVER=.;"
    r"DATABASE=KutuphaneDB;"
    r"Trusted_conneciton=yes;"
)

GIRIS_KONTROL = "Select * from GirisKontrol(?,?)"
UYE_LISTESI = "Select * from UyeListesi()"
KULLANICI_LISTESI = "Select * from KullaniciListesi()"

UYE_EKLE_GUNCELLE = "exec UyeEkleGuncelle @UyeID = ?, @Adi = ?, @Telefon = ?, @Adres = ?, @KayitTarihi = ?"
KULLANICI_EKLE_GUNCELLE = "exec KullaniciEkleGuncelle @KullaniciID = ?, @Adi = ?, @Soyadi = ?, @Email = ?, @Sifre = ?"
UYE_SIL = "exec UyeSil @UyeID = ?"
KULLANICI_SIL = "exec KullaniciSil @KullaniciID = ?"

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


def Login(email, sifre):
    cursor.execute(GIRIS_KONTROL, email, sifre)
    if cursor.rowcount == 0:
        return False
    else:
        gf.kullaniciAdi = cursor.fetchall()[0][0]
        return True

def UyeListesi():
    cursor.execute(UYE_LISTESI)
    return cursor.fetchall()

def UyeEkleGuncelle(uyeID, adi, telefon, adres, kayitTarihi):
    cursor.execute(UYE_EKLE_GUNCELLE, uyeID, adi, telefon, adres, kayitTarihi)
    conn.commit()
    
def UyeSil(uyeID):
    cursor.execute(UYE_SIL, uyeID)
    conn.commit()
    
def KullaniciListesi():
    cursor.execute(KULLANICI_LISTESI)
    return cursor.fetchall()

def KullaniciEkleGuncelle(kullaniciID, adi, soyadi, email, sifre):
    cursor.execute(KULLANICI_EKLE_GUNCELLE, kullaniciID, adi, soyadi, email, sifre)
    conn.commit()

def KullaniciSil(kullaniciID):
    cursor.execute(KULLANICI_SIL, kullaniciID)
    conn.commit()