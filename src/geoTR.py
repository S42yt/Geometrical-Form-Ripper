import math

def kare():
    kenar = float(input("Karenin bir kenar uzunluğunu girin: "))
    cevre = 4 * kenar
    alan = kenar ** 2
    print(f"Karenin Çevresi: {cevre}, Alanı: {alan}")

def dikdortgen():
    uzun_kenar = float(input("Dikdörtgenin uzun kenarını girin: "))
    kisa_kenar = float(input("Dikdörtgenin kısa kenarını girin: "))
    cevre = 2 * (uzun_kenar + kisa_kenar)
    alan = uzun_kenar * kisa_kenar
    print(f"Dikdörtgenin Çevresi: {cevre}, Alanı: {alan}")

def daire():
    yaricap = float(input("Dairenin yarıçapını girin: "))
    cevre = 2 * math.pi * yaricap
    alan = math.pi * (yaricap ** 2)
    print(f"Dairenin Çevresi: {cevre:.2f}, Alanı: {alan:.2f}")

def ucgen():
    print("Üçgen için üç kenar uzunluğu veya taban ve yükseklik girebilirsiniz.")
    secim = input("1: Üç kenar uzunluğu, 2: Taban ve yükseklik: ")
    if secim == "1":
        kenar1 = float(input("Birinci kenarı girin: "))
        kenar2 = float(input("İkinci kenarı girin: "))
        kenar3 = float(input("Üçüncü kenarı girin: "))
        cevre = kenar1 + kenar2 + kenar3
        s = cevre / 2
        alan = math.sqrt(s * (s - kenar1) * (s - kenar2) * (s - kenar3))
        print(f"Üçgenin Çevresi: {cevre}, Alanı: {alan:.2f}")
    elif secim == "2":
        taban = float(input("Tabanı girin: "))
        yukseklik = float(input("Yüksekliği girin: "))
        alan = (taban * yukseklik) / 2
        print(f"Üçgenin Alanı: {alan}")
    else:
        print("Geçersiz seçim yaptınız.")

def main():
    while True:
        print("\nHangi şeklin çevresini ve alanını hesaplamak istiyorsunuz?")
        print("1: Kare\n2: Dikdörtgen\n3: Daire\n4: Üçgen\n5: Çıkış")
        secim = input("Seçiminizi yapın (1-5): ")

        if secim == "1":
            kare()
        elif secim == "2":
            dikdortgen()
        elif secim == "3":
            daire()
        elif secim == "4":
            ucgen()
        elif secim == "5":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz bir seçim yaptınız, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
