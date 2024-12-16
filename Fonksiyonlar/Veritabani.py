import pyodbc
import Fonksiyonlar.GenelFonksiyonlar as gf

conn_str = (
    r"DRIVER={SQL Server};"
    r"SERVER=.;"
    r"DATABASE=KutuphaneDB;"
    r"Trusted_conneciton=yes;"
)

GIRIS_KONTROL = "Select * from GirisKontrol(?,?)"
KATEGORI_LISTESI = "Select * from KategoriListesi()"
KITAP_LISTESI = "Select * from KitapListesi()"
KULLANICI_LISTESI = "Select * from KullaniciListesi()"
ODUNC_LISTESI = "Select * from OduncListesi()"
UYE_LISTESI = "Select * from UyeListesi()"
YAYINCI_LISTESI = "Select * from YayinciListesi()"
YAZAR_LISTESI = "Select * from YazarListesi()"

KITAP_EKLE_GUNCELLE = "exec KitapEkleGuncelle @KitapID = ?, @KitapAdi = ?, @YazarID = ?, @YayinciID = ?, @KategoriID = ?, @BasimYili = ?, @SayfaSayisi = ?, @StokAdedi = ?"
KATEGORI_EKLE_GUNCELLE = "exec KategoriEkleGuncelle @KategoriID = ?, @KategoriAdi = ?"
KULLANICI_EKLE_GUNCELLE = "exec KullaniciEkleGuncelle @KullaniciID = ?, @Adi = ?, @Soyadi = ?, @Email = ?, @Sifre = ?"
ODUNC_EKLE_GUNCELLE = "exec OduncEkleGuncelle @OduncID = ?, @KitapID = ?, @UyeID = ?, @VerilisTarihi = ?, @TeslimTarihi = ?"
UYE_EKLE_GUNCELLE = "exec UyeEkleGuncelle @UyeID = ?, @Adi = ?, @Telefon = ?, @Adres = ?, @KayitTarihi = ?"
YAYINCI_EKLE_GUNCELLE = "exec YayinciEkleGuncelle @YayinciID = ?, @YayinciAdi = ?, @Adres = ?"
YAZAR_EKLE_GUNCELLE = "exec YazarEkleGuncelle @YazarID = ?, @YazarAdi = ?, @DogumTarihi = ?"

KATEGORI_SIL = "exec KategoriSil @KategoriID = ?"
KITAP_SIL = "exec KitapSil @KitapID = ?"
KULLANICI_SIL = "exec KullaniciSil @KullaniciID = ?"
ODUNC_SIL = "exec OduncSil @OduncID = ?"
UYE_SIL = "exec UyeSil @UyeID = ?"
YAYINCI_SIL = "exec YayinciSil @YayinciID = ?"
YAZAR_SIL = "exec YazarSil @YazarID = ?"

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# ..: Fonksiyonlar :..
def Login(email, sifre):
    cursor.execute(GIRIS_KONTROL, email, sifre)
    if cursor.rowcount == 0:
        return False
    else:
        gf.kullaniciAdi = cursor.fetchall()[0][0]
        return True

def KategoriListesi():
    cursor.execute(KATEGORI_LISTESI)
    return cursor.fetchall()

def KitapListesi():
    cursor.execute(KITAP_LISTESI)
    return cursor.fetchall()

def KullaniciListesi():
    cursor.execute(KULLANICI_LISTESI)
    return cursor.fetchall()

def OduncListesi():
    cursor.execute(ODUNC_LISTESI)
    return cursor.fetchall()

def UyeListesi():
    cursor.execute(UYE_LISTESI)
    return cursor.fetchall()

def YayinciListesi():
    cursor.execute(YAYINCI_LISTESI)
    return cursor.fetchall()

def YazarListesi():
    cursor.execute(YAZAR_LISTESI)
    return cursor.fetchall()
# ..: Fonksiyonlar :..


# ..: Ekleme ve Güncelleme :..
def KategoriEkleGuncelle(kategoriID, kategoriAdi):
    cursor.execute(KATEGORI_EKLE_GUNCELLE, kategoriID, kategoriAdi)
    conn.commit()

def KitapEkleGuncelle(kitapID, kitapAdi, yazarID, yayinciID, kategoriID, basimTarihi, sayfaSayisi, stokAdedi):
    cursor.execute(KITAP_EKLE_GUNCELLE, kitapID, kitapAdi, yazarID, yayinciID, kategoriID, basimTarihi, sayfaSayisi, stokAdedi)
    conn.commit()

def KullaniciEkleGuncelle(kullaniciID, adi, soyadi, email, sifre):
    cursor.execute(KULLANICI_EKLE_GUNCELLE, kullaniciID, adi, soyadi, email, sifre)
    conn.commit()

def OduncEkleGuncelle(oduncID, kitapID, uyeID, verilisTarihi, teslimTarihi):
    cursor.execute(ODUNC_EKLE_GUNCELLE, oduncID, kitapID, uyeID, verilisTarihi, teslimTarihi)
    conn.commit()

def UyeEkleGuncelle(uyeID, adi, telefon, adres, kayitTarihi):
    cursor.execute(UYE_EKLE_GUNCELLE, uyeID, adi, telefon, adres, kayitTarihi)
    conn.commit()
    
def YayinciEkleGuncelle(yayinciID, yayinciAdi, adres):
    cursor.execute(YAYINCI_EKLE_GUNCELLE, yayinciID, yayinciAdi, adres)
    conn.commit()

def YazarEkleGuncelle(yazarID, adi, soyadi):
    cursor.execute(YAZAR_EKLE_GUNCELLE, yazarID, adi, soyadi)
    conn.commit()
# ..: Ekleme ve Güncelleme :..


# ..: Silme :..
def KategoriSil(kategoriID):
    cursor.execute(KATEGORI_SIL, kategoriID)
    conn.commit()

def KitapSil(kitapID):
    cursor.execute(KITAP_SIL, kitapID)
    conn.commit()

def KullaniciSil(kullaniciID):
    cursor.execute(KULLANICI_SIL, kullaniciID)
    conn.commit()

def OduncSil(oduncID):
    cursor.execute(ODUNC_SIL, oduncID)
    conn.commit()

def UyeSil(uyeID):
    cursor.execute(UYE_SIL, uyeID)
    conn.commit()

def YayinciSil(yayinciID):
    cursor.execute(YAYINCI_SIL, yayinciID)
    conn.commit()

def YazarSil(yazarID):
    cursor.execute(YAZAR_SIL, yazarID)
    conn.commit()
# ..: Silme :..
