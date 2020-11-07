# Ogrenci Puan Hesaplama


class Soru():

    def NetSayisi (self, dogruSayisi, yanlisSayisi):

        net_sayisi = int(dogruSayisi - yanlisSayisi / 4)

        return net_sayisi

    def Hesapla (self, netSayisi):

        return netSayisi * 10


class Ogrenci(Soru):

    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinifi):

        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinifi = ogrenciSinifi


Adi = input("Ogrencinin Adı : ")
Soyadi = input("Ogrenicinin Soyadı : ")
Sinifi = input("Ogrencinin Sınıfı : ")

while True:

    Dogru = int(input("Ogrencinin Dogru Sayısı : "))
    Yanlis = int(input("Ogrencinin Yanlış Sayısı : "))

    if Dogru + Yanlis <= 100 and Dogru >= 0 and Yanlis >= 0:
        break
    else:
        print("Yanlis Girdiniz. Tekrar giriniz !")


ogr1 = Ogrenci(Adi, Soyadi, Sinifi)
netSys = ogr1.NetSayisi(Dogru, Yanlis)
puan = ogr1.Hesapla(netSys)

print("Ad : {} , Soyad : {} , Sınıf : {} , Puan : {}".format(ogr1.ogrenciAdi, ogr1.ogrenciSoyadi, ogr1.ogrenciSinifi, puan))








