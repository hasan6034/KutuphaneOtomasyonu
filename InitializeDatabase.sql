USE [master]
GO
/****** Object:  Database [KutuphaneDB]    Script Date: 22.12.2024 15:42:13 ******/
CREATE DATABASE [KutuphaneDB]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'KutuphaneDB', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\KutuphaneDB.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'KutuphaneDB_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\KutuphaneDB_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [KutuphaneDB] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [KutuphaneDB].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [KutuphaneDB] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [KutuphaneDB] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [KutuphaneDB] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [KutuphaneDB] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [KutuphaneDB] SET ARITHABORT OFF 
GO
ALTER DATABASE [KutuphaneDB] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [KutuphaneDB] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [KutuphaneDB] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [KutuphaneDB] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [KutuphaneDB] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [KutuphaneDB] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [KutuphaneDB] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [KutuphaneDB] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [KutuphaneDB] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [KutuphaneDB] SET  DISABLE_BROKER 
GO
ALTER DATABASE [KutuphaneDB] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [KutuphaneDB] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [KutuphaneDB] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [KutuphaneDB] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [KutuphaneDB] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [KutuphaneDB] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [KutuphaneDB] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [KutuphaneDB] SET RECOVERY FULL 
GO
ALTER DATABASE [KutuphaneDB] SET  MULTI_USER 
GO
ALTER DATABASE [KutuphaneDB] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [KutuphaneDB] SET DB_CHAINING OFF 
GO
ALTER DATABASE [KutuphaneDB] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [KutuphaneDB] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [KutuphaneDB] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [KutuphaneDB] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'KutuphaneDB', N'ON'
GO
ALTER DATABASE [KutuphaneDB] SET QUERY_STORE = ON
GO
ALTER DATABASE [KutuphaneDB] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [KutuphaneDB]
GO
/****** Object:  Table [dbo].[Kitaplar]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Kitaplar](
	[KitapID] [int] IDENTITY(1,1) NOT NULL,
	[KitapAdi] [varchar](255) NOT NULL,
	[YazarID] [int] NOT NULL,
	[YayinciID] [int] NOT NULL,
	[KategoriID] [int] NOT NULL,
	[BasimYili] [date] NULL,
	[SayfaSayisi] [int] NULL,
 CONSTRAINT [PK__Kitaplar__89491B2C35D163A0] PRIMARY KEY CLUSTERED 
(
	[KitapID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Uyeler]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Uyeler](
	[UyeID] [int] IDENTITY(1,1) NOT NULL,
	[UyeAdi] [nvarchar](255) NOT NULL,
	[Telefon] [nvarchar](15) NULL,
	[Adres] [nvarchar](255) NULL,
	[KayitTarihi] [date] NULL,
PRIMARY KEY CLUSTERED 
(
	[UyeID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[OduncIslemleri]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[OduncIslemleri](
	[IslemID] [int] IDENTITY(1,1) NOT NULL,
	[UyeID] [int] NOT NULL,
	[KitapID] [int] NOT NULL,
	[KullaniciID] [int] NOT NULL,
	[OduncTarihi] [date] NULL,
	[IadeTarihi] [date] NULL,
	[AlindiMi] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[IslemID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  UserDefinedFunction [dbo].[KitapGeciktirenler]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[KitapGeciktirenler]()
RETURNS TABLE 
AS
RETURN 
(
	SELECT
		u.UyeAdi,
		u.Telefon,
		u.Adres,
		k.KitapAdi,
		o.OduncTarihi,
		datediff(day,o.OduncTarihi,GETDATE()) as GecikmeSuresi
	FROM
		OduncIslemleri o
	INNER JOIN
		Uyeler u on  o.UyeID = u.UyeAdi
	INNER JOIN
		Kitaplar k on o.KitapID = k.KitapID
	WHERE
		datediff(day,o.OduncTarihi,GETDATE()) > 7
)
GO
/****** Object:  Table [dbo].[Kullanicilar]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Kullanicilar](
	[KullaniciID] [int] IDENTITY(1,1) NOT NULL,
	[Adi] [varchar](100) NOT NULL,
	[Soyadi] [varchar](100) NOT NULL,
	[Email] [varchar](100) NOT NULL,
	[Sifre] [varchar](50) NOT NULL,
 CONSTRAINT [PK__Calisanl__40749CB6848826CE] PRIMARY KEY CLUSTERED 
(
	[KullaniciID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  UserDefinedFunction [dbo].[GirisKontrol]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[GirisKontrol]
(	
	@Email varchar(100),
	@Sifre varchar(50)
)
RETURNS TABLE 
AS
RETURN 
(
	select Adi + ' ' + Soyadi as "AdSoyad" from Kullanicilar where Email = @Email and Sifre = @Sifre
)
GO
/****** Object:  UserDefinedFunction [dbo].[UyeListesi]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[UyeListesi]
(	
)
RETURNS TABLE 
AS
RETURN 
(
	select 
		UyeID,UyeAdi,Telefon,Adres,KayitTarihi 
	from 
		Uyeler
)
GO
/****** Object:  UserDefinedFunction [dbo].[KullaniciListesi]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[KullaniciListesi]
(	
)
RETURNS TABLE 
AS
RETURN 
(
	SELECT KullaniciID,Adi,Soyadi,Email,Sifre FROM Kullanicilar
)
GO
/****** Object:  Table [dbo].[Yazarlar]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Yazarlar](
	[YazarID] [int] IDENTITY(1,1) NOT NULL,
	[YazarAdi] [nvarchar](255) NOT NULL,
	[DogumTarihi] [date] NULL,
PRIMARY KEY CLUSTERED 
(
	[YazarID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Kategoriler]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Kategoriler](
	[KategoriID] [int] IDENTITY(1,1) NOT NULL,
	[KategoriAdi] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[KategoriID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Yayincilar]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Yayincilar](
	[YayinciID] [int] IDENTITY(1,1) NOT NULL,
	[YayinciAdi] [varchar](255) NOT NULL,
	[Adres] [varchar](255) NOT NULL,
 CONSTRAINT [PK__Yayincil__FA36F537B2BC42E4] PRIMARY KEY CLUSTERED 
(
	[YayinciID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  UserDefinedFunction [dbo].[KitapListesi]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[KitapListesi]()
RETURNS TABLE 
AS
RETURN 
(
	select 
		k.KitapID,
		k.KitapAdi,
		y.YazarAdi,
		yay.YayinciAdi,
		kat.KategoriAdi,
		k.BasimYili,
		k.SayfaSayisi
	from
		Kitaplar k
	INNER JOIN
		Yazarlar y on k.YazarID = y.YazarID
	INNER JOIN
		Yayincilar yay on k.YayinciID = yay.YayinciID
	INNER JOIN
		Kategoriler kat on k.KategoriID = kat.KategoriID
)
GO
/****** Object:  UserDefinedFunction [dbo].[YayinciListesi]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[YayinciListesi]()
RETURNS TABLE 
AS
RETURN 
(
	select 
		YayinciID,
		YayinciAdi,
		Adres
	from
		Yayincilar
)
GO
/****** Object:  UserDefinedFunction [dbo].[YazarListesi]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[YazarListesi]()
RETURNS TABLE 
AS
RETURN 
(
	select
		YazarID,
		YazarAdi,
		DogumTarihi
	from
		Yazarlar
)
GO
/****** Object:  UserDefinedFunction [dbo].[OduncListesi]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[OduncListesi]()
RETURNS TABLE 
AS
RETURN 
(
	select
		o.IslemID,
		u.UyeAdi,
		k.KitapAdi,
		o.OduncTarihi,
		o.IadeTarihi,
		CASE 
            WHEN o.AlindiMi = 1 THEN 'Alındı'
            ELSE 'Alınmadı'
        END AS AlindiMi
	from
		OduncIslemleri o
	INNER JOIN
		Uyeler u on o.UyeID = u.UyeID
	INNER JOIN
		Kitaplar k on o.KitapID = k.KitapID
	INNER JOIN
		Kullanicilar kul on o.KullaniciID = kul.KullaniciID
)
GO
/****** Object:  UserDefinedFunction [dbo].[KategoriListesi]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[KategoriListesi]()
RETURNS TABLE 
AS
RETURN 
(
	select 
		KategoriID,
		KategoriAdi
	from
		Kategoriler
)
GO
ALTER TABLE [dbo].[Kullanicilar] ADD  CONSTRAINT [DF__Calisanla__IseGi__403A8C7D]  DEFAULT (getdate()) FOR [Sifre]
GO
ALTER TABLE [dbo].[OduncIslemleri] ADD  DEFAULT (getdate()) FOR [OduncTarihi]
GO
ALTER TABLE [dbo].[Uyeler] ADD  DEFAULT (getdate()) FOR [KayitTarihi]
GO
/****** Object:  StoredProcedure [dbo].[KategoriEkleGuncelle]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[KategoriEkleGuncelle]
	@KategoriID int,
	@KategoriAdi varchar(100)
AS
BEGIN
	IF EXISTS (SELECT 1 FROM Kategoriler WHERE KategoriID = @KategoriID)
	BEGIN
		UPDATE Kategoriler
		SET KategoriAdi = @KategoriAdi
		WHERE KategoriID = @KategoriID
	END

	ELSE
	BEGIN
		INSERT INTO Kategoriler(KategoriAdi)
		VALUES(@KategoriAdi)
	END
END
GO
/****** Object:  StoredProcedure [dbo].[KategoriSil]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[KategoriSil]
	@KategoriID int
AS
BEGIN
	IF EXISTS (SELECT 1 FROM Kategoriler WHERE KategoriID = @KategoriID)
	BEGIN
		DELETE FROM Kategoriler WHERE KategoriID = @KategoriID
		SELECT 'Kategori başarıyla silindi.' as Sonuc
	END

	ELSE
	BEGIN
		SELECT 'Kategori bulunamadı.' as Sonuc
	END
END
GO
/****** Object:  StoredProcedure [dbo].[KitapEkleGuncelle]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[KitapEkleGuncelle]
	@KitapID int,
	@KitapAdi varchar(255),
	@YazarID int,
	@YayinciID int,
	@KategoriID int,
	@BasimYili date,
	@SayfaSayisi int
AS
BEGIN
	IF EXISTS (SELECT 1 FROM Kitaplar WHERE KitapID = @KitapID)
	BEGIN
		UPDATE Kitaplar
		SET 
			KitapAdi = @KitapAdi,
			YazarID = @YazarID,
			YayinciID = @YayinciID,
			KategoriID = @KategoriID,
			BasimYili = @BasimYili,
			SayfaSayisi = @SayfaSayisi
		WHERE
			KitapID = @KitapID
	END

	ELSE
	BEGIN
		INSERT INTO Kitaplar
			(
				KitapAdi,
				YazarID,
				YayinciID,
				KategoriID,
				BasimYili,
				SayfaSayisi
			)
		VALUES
			(
				@KitapAdi,
				@YazarID,
				@YayinciID,
				@KategoriID,
				@BasimYili,
				@SayfaSayisi
			)
	END
END
GO
/****** Object:  StoredProcedure [dbo].[KitapSil]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[KitapSil]
	@KitapID int
AS
BEGIN
	IF EXISTS (SELECT 1 FROM Kitaplar WHERE KitapID = @KitapID)
	BEGIN
		DELETE FROM Kitaplar WHERE KitapID = @KitapID
		SELECT 'Kitap başarıyla silindi.' as Sonuc
	END

	ELSE
	BEGIN
		SELECT 'Kitap bulunamadı.' as Sonuc
	END
END
GO
/****** Object:  StoredProcedure [dbo].[KullaniciEkleGuncelle]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[KullaniciEkleGuncelle]
	@KullaniciID int,
	@Adi varchar(100),
	@Soyadi varchar(100),
	@Email varchar(100),
	@Sifre varchar(50)
AS
BEGIN
	IF EXISTS (SELECT 1 FROM Kullanicilar WHERE KullaniciID = @KullaniciID)
	BEGIN
		UPDATE Kullanicilar
		SET Adi = @Adi,Soyadi = @Soyadi,Email = @Email,Sifre = @Sifre
		where KullaniciID = @KullaniciID
	END
	ELSE
	BEGIN
		INSERT INTO Kullanicilar(Adi,Soyadi,Email,Sifre)
		Values(@Adi,@Soyadi,@Email,@Sifre)
	END
END
GO
/****** Object:  StoredProcedure [dbo].[KullaniciSil]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[KullaniciSil]
	@KullaniciID int
AS
BEGIN
	IF EXISTS (SELECT 1 FROM Kullanicilar WHERE KullaniciID = @KullaniciID)
    BEGIN
        DELETE FROM Kullanicilar WHERE KullaniciID = @KullaniciID;
        SELECT 'Kullanıcı silindi' AS Sonuc;
    END
    ELSE
    BEGIN
        SELECT 'Kullanıcı bulunamadı, silme işlemi yapılmadı' AS Sonuc;
    END
END
GO
/****** Object:  StoredProcedure [dbo].[OduncEkleGuncelle]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[OduncEkleGuncelle]
	@IslemID int,
	@UyeID int,
	@KitapID int,
	@KullaniciID int,
	@OduncTarihi date,
	@IadeTarihi date,
	@AlindiMi bit
AS
BEGIN
	IF EXISTS (SELECT 1 FROM OduncIslemleri WHERE IslemID= @IslemID)
	BEGIN
		UPDATE OduncIslemleri
		SET 
			UyeID = @UyeID,
			KitapID = @KitapID,
			KullaniciID = @KullaniciID,
			OduncTarihi = @OduncTarihi,
			IadeTarihi = @IadeTarihi,
			AlindiMi = @AlindiMi
		WHERE
			IslemID = @IslemID
	END

	ELSE
	BEGIN
		INSERT INTO OduncIslemleri
			(
				UyeID,
				KitapID,
				KullaniciID,
				OduncTarihi,
				IadeTarihi,
				AlindiMi
			)
		VALUES
			(
				@UyeID,
				@KitapID,
				@KullaniciID,
				@OduncTarihi,
				@IadeTarihi,
				@AlindiMi
			)
	END
END
GO
/****** Object:  StoredProcedure [dbo].[OduncSil]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[OduncSil]
	@IslemID int
AS
BEGIN
	IF EXISTS (SELECT 1 FROM OduncIslemleri WHERE IslemID = @IslemID)
	BEGIN
		DELETE FROM OduncIslemleri
		WHERE IslemID = @IslemID
		SELECT 'İşlem başarıyla tamamlandı.' as Sonuc
	END

	ELSE
	BEGIN
		SELECT 'İşlem bulunamadı.' as Sonuc
	END
END
GO
/****** Object:  StoredProcedure [dbo].[UyeEkleGuncelle]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[UyeEkleGuncelle]
	@UyeID int,
	@UyeAdi varchar(255),
	@Telefon varchar(15),
	@Adres varchar(255),
	@KayitTarihi date
AS
BEGIN
	IF EXISTS (SELECT 1 FROM Uyeler WHERE UyeID = @UyeID)
	BEGIN
		UPDATE Uyeler
		SET UyeAdi = @UyeAdi,Telefon = @Telefon,Adres = @Adres,KayitTarihi = @KayitTarihi
		where UyeID = @UyeID
	END
	ELSE
	BEGIN
		INSERT INTO Uyeler(UyeAdi,Telefon,Adres,KayitTarihi)
		Values(@UyeAdi,@Telefon,@Adres,@KayitTarihi)
	END
END
GO
/****** Object:  StoredProcedure [dbo].[UyeSil]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[UyeSil]
	@UyeID int
AS
BEGIN
	IF EXISTS (SELECT 1 FROM Uyeler WHERE UyeID = @UyeID)
    BEGIN
        DELETE FROM Uyeler WHERE UyeID = @UyeID;
        SELECT 'Üye silindi' AS Sonuc;
    END
    ELSE
    BEGIN
        SELECT 'Üye bulunamadı, silme işlemi yapılmadı' AS Sonuc;
    END
END
GO
/****** Object:  StoredProcedure [dbo].[YayinciEkleGuncelle]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[YayinciEkleGuncelle]
	@YayinciID int,
	@YayinciAdi varchar(255),
	@Adres varchar(255)
AS
BEGIN
	IF EXISTS (SELECT 1 FROM Yayincilar WHERE YayinciID = @YayinciID)
	BEGIN
		UPDATE Yayincilar
		SET
			YayinciAdi = @YayinciAdi,
			Adres = @Adres
		WHERE
			YayinciID = @YayinciID
	END

	ELSE
	BEGIN
		INSERT INTO Yayincilar
			(
				YayinciAdi,
				Adres
			)
		VALUES
			(
				@YayinciAdi,
				@Adres
			)
	END
END
GO
/****** Object:  StoredProcedure [dbo].[YayinciSil]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[YayinciSil]
	@YayinciID int
AS
BEGIN
	IF EXISTS (SELECT 1 FROM Yayincilar WHERE YayinciID = @YayinciID)
	BEGIN
		DELETE FROM Yayincilar WHERE YayinciID = @YayinciID
		SELECT 'Yayıncı başarıyla silindi.' as Sonuc
	END

	ELSE
	BEGIN
		SELECT 'Yayıncı bulunamadı.' as Sonuc
	END
END
GO
/****** Object:  StoredProcedure [dbo].[YazarEkleGuncelle]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[YazarEkleGuncelle]
	@YazarID int,
	@YazarAdi varchar(100),
	@DogumTarihi date
AS
BEGIN
	IF EXISTS (SELECT 1 FROM Yazarlar WHERE YazarID = @YazarID)
	BEGIN
		UPDATE Yazarlar
		SET YazarAdi = @YazarAdi, DogumTarihi = @DogumTarihi
		WHERE YazarID = @YazarID
	END

	ELSE
	BEGIN
		INSERT INTO Yazarlar(YazarAdi,DogumTarihi)
		VALUES(@YazarAdi,@DogumTarihi)
	END
END
GO
/****** Object:  StoredProcedure [dbo].[YazarSil]    Script Date: 22.12.2024 15:42:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[YazarSil]
	@YazarID int
AS
BEGIN
	IF EXISTS (SELECT 1 FROM Yazarlar WHERE YazarID = @YazarID)
	BEGIN
		DELETE FROM Yazarlar
		WHERE YazarID = @YazarID
		SELECT 'Yazar başarıyla silindi.' as Sonuc
	END

	ELSE
	BEGIN
		SELECT 'Yazar bulunamadı.' as Sonuc
	END
END
GO
USE [master]
GO
ALTER DATABASE [KutuphaneDB] SET  READ_WRITE 
GO

INSERT INTO Kullanicilar(Adi,Soyadi,Email,Sifre) values ('Yetkili','Kullanıcı','admin','1234')
