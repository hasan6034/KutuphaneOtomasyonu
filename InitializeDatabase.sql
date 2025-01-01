USE [master]
GO
/****** Object:  Database [KutuphaneDB]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  Table [dbo].[Kitaplar]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  Table [dbo].[Uyeler]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  Table [dbo].[OduncIslemleri]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  UserDefinedFunction [dbo].[KitapGeciktirenler]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  Table [dbo].[Kullanicilar]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  UserDefinedFunction [dbo].[GirisKontrol]    Script Date: 1.01.2025 16:09:30 ******/
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
	select Adi + ' ' + Soyadi as "AdSoyad", KullaniciID from Kullanicilar where Email = @Email and Sifre = @Sifre
)
GO
/****** Object:  UserDefinedFunction [dbo].[UyeListesi]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  UserDefinedFunction [dbo].[KullaniciListesi]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  Table [dbo].[Yazarlar]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  Table [dbo].[Kategoriler]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  Table [dbo].[Yayincilar]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  UserDefinedFunction [dbo].[KitapListesi]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  UserDefinedFunction [dbo].[YayinciListesi]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  UserDefinedFunction [dbo].[YazarListesi]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  UserDefinedFunction [dbo].[OduncListesi]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  UserDefinedFunction [dbo].[KategoriListesi]    Script Date: 1.01.2025 16:09:30 ******/
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
SET IDENTITY_INSERT [dbo].[Kategoriler] ON 
GO
INSERT [dbo].[Kategoriler] ([KategoriID], [KategoriAdi]) VALUES (1, N'Gençlik')
GO
INSERT [dbo].[Kategoriler] ([KategoriID], [KategoriAdi]) VALUES (2, N'Anı')
GO
INSERT [dbo].[Kategoriler] ([KategoriID], [KategoriAdi]) VALUES (3, N'Anlatı')
GO
INSERT [dbo].[Kategoriler] ([KategoriID], [KategoriAdi]) VALUES (4, N'Çizgi Roman')
GO
INSERT [dbo].[Kategoriler] ([KategoriID], [KategoriAdi]) VALUES (5, N'Deneme')
GO
INSERT [dbo].[Kategoriler] ([KategoriID], [KategoriAdi]) VALUES (6, N'Edebiyat')
GO
INSERT [dbo].[Kategoriler] ([KategoriID], [KategoriAdi]) VALUES (7, N'Bilim')
GO
INSERT [dbo].[Kategoriler] ([KategoriID], [KategoriAdi]) VALUES (8, N'Araştırma')
GO
INSERT [dbo].[Kategoriler] ([KategoriID], [KategoriAdi]) VALUES (9, N'Biyogrofi')
GO
INSERT [dbo].[Kategoriler] ([KategoriID], [KategoriAdi]) VALUES (10, N'Oto Biyografi')
GO
SET IDENTITY_INSERT [dbo].[Kategoriler] OFF
GO
SET IDENTITY_INSERT [dbo].[Kitaplar] ON 
GO
INSERT [dbo].[Kitaplar] ([KitapID], [KitapAdi], [YazarID], [YayinciID], [KategoriID], [BasimYili], [SayfaSayisi]) VALUES (1, N'Sol Ayağım', 2, 1, 10, CAST(N'2025-01-01' AS Date), 250)
GO
INSERT [dbo].[Kitaplar] ([KitapID], [KitapAdi], [YazarID], [YayinciID], [KategoriID], [BasimYili], [SayfaSayisi]) VALUES (2, N'Tuş Beyinli', 1, 2, 1, CAST(N'2025-01-01' AS Date), 300)
GO
SET IDENTITY_INSERT [dbo].[Kitaplar] OFF
GO
SET IDENTITY_INSERT [dbo].[Kullanicilar] ON 
GO
INSERT [dbo].[Kullanicilar] ([KullaniciID], [Adi], [Soyadi], [Email], [Sifre]) VALUES (1, N'Yetkili', N'Kullanıcı', N'admin', N'1234')
GO
SET IDENTITY_INSERT [dbo].[Kullanicilar] OFF
GO
SET IDENTITY_INSERT [dbo].[OduncIslemleri] ON 
GO
INSERT [dbo].[OduncIslemleri] ([IslemID], [UyeID], [KitapID], [KullaniciID], [OduncTarihi], [IadeTarihi], [AlindiMi]) VALUES (1, 1, 1, 1, CAST(N'2025-01-01' AS Date), CAST(N'2025-01-08' AS Date), 0)
GO
INSERT [dbo].[OduncIslemleri] ([IslemID], [UyeID], [KitapID], [KullaniciID], [OduncTarihi], [IadeTarihi], [AlindiMi]) VALUES (2, 2, 2, 1, CAST(N'2025-01-01' AS Date), CAST(N'2025-01-08' AS Date), 1)
GO
INSERT [dbo].[OduncIslemleri] ([IslemID], [UyeID], [KitapID], [KullaniciID], [OduncTarihi], [IadeTarihi], [AlindiMi]) VALUES (3, 3, 2, 1, CAST(N'2025-01-01' AS Date), CAST(N'2025-01-08' AS Date), 0)
GO
SET IDENTITY_INSERT [dbo].[OduncIslemleri] OFF
GO
SET IDENTITY_INSERT [dbo].[Uyeler] ON 
GO
INSERT [dbo].[Uyeler] ([UyeID], [UyeAdi], [Telefon], [Adres], [KayitTarihi]) VALUES (1, N'Caner ORAK', N'531629356', N'Bitlis', CAST(N'2025-01-01' AS Date))
GO
INSERT [dbo].[Uyeler] ([UyeID], [UyeAdi], [Telefon], [Adres], [KayitTarihi]) VALUES (2, N'Kürşat KUTLUYER', N'555665455', N'Karaman', CAST(N'2025-01-01' AS Date))
GO
INSERT [dbo].[Uyeler] ([UyeID], [UyeAdi], [Telefon], [Adres], [KayitTarihi]) VALUES (3, N'Zafer ŞİMŞEK', N'5444444', N'Mersin', CAST(N'2024-12-31' AS Date))
GO
SET IDENTITY_INSERT [dbo].[Uyeler] OFF
GO
SET IDENTITY_INSERT [dbo].[Yayincilar] ON 
GO
INSERT [dbo].[Yayincilar] ([YayinciID], [YayinciAdi], [Adres]) VALUES (1, N'Nora Kitap', N'Gümüşsuyu Mah. Osmanlı Sokak Osmanlı İş Merkezi No:18 Kat:2/9 Beyoğlu - İSTANBUL')
GO
INSERT [dbo].[Yayincilar] ([YayinciID], [YayinciAdi], [Adres]) VALUES (2, N'Genç Nesil', N'Orhan Gazi Mahallesi 19.YOL Sokak No: 8, 34538 Esenyurt / İstanbul')
GO
SET IDENTITY_INSERT [dbo].[Yayincilar] OFF
GO
SET IDENTITY_INSERT [dbo].[Yazarlar] ON 
GO
INSERT [dbo].[Yazarlar] ([YazarID], [YazarAdi], [DogumTarihi]) VALUES (1, N'Yusuf ASAL', CAST(N'1973-07-01' AS Date))
GO
INSERT [dbo].[Yazarlar] ([YazarID], [YazarAdi], [DogumTarihi]) VALUES (2, N'Christy Brown', CAST(N'1980-05-12' AS Date))
GO
SET IDENTITY_INSERT [dbo].[Yazarlar] OFF
GO
ALTER TABLE [dbo].[Kullanicilar] ADD  CONSTRAINT [DF__Calisanla__IseGi__403A8C7D]  DEFAULT (getdate()) FOR [Sifre]
GO
ALTER TABLE [dbo].[OduncIslemleri] ADD  DEFAULT (getdate()) FOR [OduncTarihi]
GO
ALTER TABLE [dbo].[Uyeler] ADD  DEFAULT (getdate()) FOR [KayitTarihi]
GO
/****** Object:  StoredProcedure [dbo].[KategoriEkleGuncelle]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  StoredProcedure [dbo].[KategoriSil]    Script Date: 1.01.2025 16:09:30 ******/
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
	IF EXISTS (SELECT 1 FROM Kitaplar WHERE KategoriID = @KategoriID)
	BEGIN
		RAISERROR('Bu Kategori Silinemez. Bu Kategoriyi Silmek Veri Tutarsızlığına Neden Olabilir.', 16, 1);
		RETURN
	END
	IF EXISTS (SELECT 1 FROM Kategoriler WHERE KategoriID = @KategoriID)
	BEGIN
		DELETE FROM Kategoriler WHERE KategoriID = @KategoriID
	END

	ELSE
	BEGIN
		RAISERROR('Kategori Bulunamadı.', 16, 1);
		RETURN
	END
END
GO
/****** Object:  StoredProcedure [dbo].[KitapEkleGuncelle]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  StoredProcedure [dbo].[KitapSil]    Script Date: 1.01.2025 16:09:30 ******/
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
	IF EXISTS (SELECT 1 FROM OduncIslemleri WHERE KitapID = @KitapID)
	BEGIN
		RAISERROR('Bu Kitap Silinemez. Bu Kitabı Silmek Veri Tutarsızlığına Neden Olabilir.', 16, 1);
		RETURN
	END
	IF EXISTS (SELECT 1 FROM Kitaplar WHERE KitapID = @KitapID)
	BEGIN
		DELETE FROM Kitaplar WHERE KitapID = @KitapID
	END

	ELSE
	BEGIN
		RAISERROR('Kitap bulunamadı.', 16, 1);
		RETURN
	END
END
GO
/****** Object:  StoredProcedure [dbo].[KullaniciEkleGuncelle]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  StoredProcedure [dbo].[KullaniciSil]    Script Date: 1.01.2025 16:09:30 ******/
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
	IF @KullaniciID = 1
	BEGIN
		RAISERROR('İlk Kullanıcı Silinemez.', 16, 1);
		RETURN
	END
	IF EXISTS (SELECT 1 FROM OduncIslemleri WHERE KullaniciID = @KullaniciID)
	BEGIN
		RAISERROR('Bu Kullanıcı Silinemez. Bu Kullanıcıyı Silmek Veri Tutarsızlığına Neden Olabilir.', 16, 1);
		RETURN
	END

	IF EXISTS (SELECT 1 FROM Kullanicilar WHERE KullaniciID = @KullaniciID)
    BEGIN
        DELETE FROM Kullanicilar WHERE KullaniciID = @KullaniciID;
    END
    ELSE
    BEGIN
        RAISERROR('Kullanıcı bulunamadı, silme işlemi yapılmadı',16,1);
    END
END
GO
/****** Object:  StoredProcedure [dbo].[OduncEkleGuncelle]    Script Date: 1.01.2025 16:09:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
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
	IF @IslemID = -1
	BEGIN
		IF EXISTS (SELECT 1 FROM OduncIslemleri WHERE KitapID = @KitapID AND AlindiMi = 0)
		BEGIN
			RAISERROR('Bu kitap başka bir kullanıcıda ve henüz iade edilmedi.', 16, 1)
			RETURN
		END

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
		RETURN
	END

	ELSE
	BEGIN
		DECLARE @EskiKitapID INT
		SELECT @EskiKitapID = KitapID FROM OduncIslemleri WHERE IslemID = @IslemID

		IF @EskiKitapID <> @KitapID
		BEGIN
			IF EXISTS (SELECT 1 FROM OduncIslemleri WHERE KitapID = @KitapID AND AlindiMi = 0)
			BEGIN
				RAISERROR('Yeni kitap başka bir kullanıcıda ve henüz iade edilmedi.', 16, 1)
				RETURN
			END
		END

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
END
GO
/****** Object:  StoredProcedure [dbo].[OduncSil]    Script Date: 1.01.2025 16:09:30 ******/
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
	END

	ELSE
	BEGIN
		RAISERROR('İşlem bulunamadı.', 16, 1);
	END
END
GO
/****** Object:  StoredProcedure [dbo].[UyeEkleGuncelle]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  StoredProcedure [dbo].[UyeSil]    Script Date: 1.01.2025 16:09:30 ******/
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
	IF EXISTS(SELECT 1 FROM OduncIslemleri WHERE UyeID = @UyeID)
	BEGIN
		RAISERROR('Bu Üye Silinemez. Bu Üyeyi Silmek Veri Tutarsızlığına Neden Olabilir.', 16, 1);
		RETURN
	END
	IF EXISTS (SELECT 1 FROM Uyeler WHERE UyeID = @UyeID)
    BEGIN
        DELETE FROM Uyeler WHERE UyeID = @UyeID;
    END
    ELSE
    BEGIN
		RAISERROR('Üye bulunamadı, silme işlemi yapılmadı', 16, 1);
		RETURN
    END
END
GO
/****** Object:  StoredProcedure [dbo].[YayinciEkleGuncelle]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  StoredProcedure [dbo].[YayinciSil]    Script Date: 1.01.2025 16:09:30 ******/
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
	IF EXISTS(SELECT 1 FROM Kitaplar WHERE YayinciID = @YayinciID)
	BEGIN
		RAISERROR('Bu Yayıncı Silinemez. Bu Yayıncıyı Silmek Veri Tutarsızlığına Neden Olabilir.', 16, 1);
		RETURN
	END

	IF EXISTS (SELECT 1 FROM Yayincilar WHERE YayinciID = @YayinciID)
	BEGIN
		DELETE FROM Yayincilar WHERE YayinciID = @YayinciID
	END

	ELSE
	BEGIN
		RAISERROR('Yayıncı bulunamadı.', 16, 1);
		RETURN
	END
END
GO
/****** Object:  StoredProcedure [dbo].[YazarEkleGuncelle]    Script Date: 1.01.2025 16:09:30 ******/
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
/****** Object:  StoredProcedure [dbo].[YazarSil]    Script Date: 1.01.2025 16:09:30 ******/
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
	IF EXISTS(SELECT 1 FROM Kitaplar WHERE YazarID = @YazarID)
	BEGIN
		RAISERROR('Bu Yazar Silinemez. Bu Yazarı Silmek Veri Tutarsızlığına Neden Olabilir.', 16, 1);
		RETURN
	END
	IF EXISTS (SELECT 1 FROM Yazarlar WHERE YazarID = @YazarID)
	BEGIN
		DELETE FROM Yazarlar
		WHERE YazarID = @YazarID
	END

	ELSE
	BEGIN
		RAISERROR('Yazar bulunamadı.', 16, 1);
		RETURN
	END
END
GO
USE [master]
GO
ALTER DATABASE [KutuphaneDB] SET  READ_WRITE 
GO
