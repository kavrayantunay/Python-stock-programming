# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:15:33 2020

@author: Tunay
"""
"""
programın işleyişi:
    !1-Program başlayınca bize bir menü gelecek, bu menüde aşağıdaki şekilde bir liste olacak
    *Ürünleri Listele
    *Ürün Ekle
    *Ürün Sil
    !2- Ürünleri listeleyi seçersem, o ana kadarki kullanılan ürünleri listeler
    !3- ürün ekleyi seçersem, program benden, ürün adı, fiyatı ve kaç tane stokta bulunduğunu bana sormalı, ve bu bilgileri kaydetmeli
    4- Ürün sil seçersem program yine ürünleri listeleyecek ve yanında hangi sayı bulunan ürünü silmek istiyorsak, o numarayı yazmamızı isteyecek
    
"""
urunAdiListesi = []
urunFiyatiListesi = []
urunStoguListesi = []
uygulamaCalisiyor = True

print("***************\nPython ile yazılmış basit stok programına hoşgeldiniz...\n***************")

while(uygulamaCalisiyor):
    print("**************************")
    print("İşlem listesi:\n1-Ürünleri Listele:\n2-Ürün Ekle:\n3-Ürün Sil:")
    islemNo = input("İşlem numarasını giriniz: ")
    
    
    #not: sayıları "" içinde yazmamızın nedeni input içinden gelenlerin str olması
    
    if islemNo == "1":
        for urun in urunAdiListesi:
            print("-", urun)
        print("Ürünleri Listele Seçildi..")
    elif islemNo == "2":
        
        urunAdi = input ("Ürünün Adı : ")
        urunFiyati = input ("Ürünün Fiyatı : ")
        urunStogu = input ("Ürün Stok Sayısı : ")
        
        urunAdiListesi.append(urunAdi)
        urunFiyatiListesi.append(urunFiyati)
        urunStoguListesi.append(urunStogu)
        
        print(urunStogu, urunAdi, "sisteme başarıyla eklendi")
        
    elif islemNo == "3":
        if len(urunAdiListesi) == 0:
            print("Herhangi bir ürün bulunmadığı için silme işlemi gerçekleşmedi..")
        else:    
        
            siraDegiskeni = 0
            for urun in urunAdiListesi:
                print("-", siraDegiskeni, urun)
                siraDegiskeni += 1
                
            urunKodu = input("silmek istediğiniz ürünün kodu : ")
            urunKodu = int(urunKodu)
            urunAdiListesi.pop(urunKodu)
            urunFiyatiListesi.pop(urunKodu)
            urunStoguListesi.pop(urunKodu)
            
            print("Ürün silme işlemi başarıyla gerçekleşti...")
    elif islemNo == "q":
        print("Programdan Çıkış Yapılıyor")
        uygulamaCalisiyor = False   
        
            

    else:
        print("Hatalı İşlem Numarası Girdiniz..!!")