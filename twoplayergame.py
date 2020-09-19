import random
import time
oyuncu1 = input("Oyuncu1 ismini gir: ")
oyuncu2 = input("Oyuncu2 ismini gir: ")


def oyun():
    ustsinir = int(input("Ust siniri belirle"))
    oyunturusinir = int(input("Oyun kaç tur olsun ?"))
    oyuncu1puan = 0
    oyuncu2puan = 0
    oyunturu = 0
    while True:
        randomsayi = random.randrange(0, ustsinir)
        while True:
            time.sleep(1)
            tahmin1 = int(input("Oyuncu 1'in Tahmini"))
            while (tahmin1 > ustsinir):
               print("Tahmin üst sınırdan büyük olamaz!")
               tahmin1 = int(input("Oyuncu 1'in Tahmini"))
            tahmin2 = int(input("Oyuncu 2'nin Tahmini"))
            while (tahmin2 > ustsinir):
                print("Tahmin üst sınırdan büyük olamaz!")
                tahmin2 = int(input("Oyuncu 2'nin Tahmini"))
            else:
                break


        fark1 = abs(randomsayi - tahmin1)
        fark2 = abs(randomsayi - tahmin2)
        if (fark1 < fark2):
            print("oyuncu 1 galip oldu!")
            if fark1 == 0:
                oyuncu1puan += 20
            else:
                oyuncu1puan += 10
        elif (fark2 < fark1):
            print("oyuncu 2 galip oldu!")
            if fark2 == 0:
                oyuncu2puan += 20
            else:
                oyuncu2puan += 10
        else:
            print("oyun berabere")
            oyuncu1puan += 5
            oyuncu2puan += 5
        time.sleep(1)
        print("Oyundaki sayı '{}' idi ".format(randomsayi))
        oyunturu += 1
        if oyunturu == oyunturusinir:
            print("{} kişisinin Toplam Puanı : {}".format(oyuncu1,oyuncu1puan))
            print("{} kişisinin Toplam Puanı : {}".format(oyuncu2,oyuncu2puan))
            if oyuncu1puan < oyuncu2puan:
                print("{} Bu maçı {} puan farkla Kazandı ".format(oyuncu2,oyuncu2puan - oyuncu1puan))
            elif oyuncu1puan > oyuncu2puan:
                print("{} Bu maçı {} puan farkla Kazandı ".format(oyuncu1,oyuncu1puan - oyuncu2puan))
            elif oyuncu1puan == oyuncu2puan:
                print("Oyun Berabere")
            print("Oyun Kapanıyor..")
            time.sleep(40)

            break



oyun()