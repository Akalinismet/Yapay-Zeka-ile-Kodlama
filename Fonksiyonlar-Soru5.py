#Bir fonksiyon yazın. Bu fonksiyon iki parametre almalıdır:
#• metin → İşlem yapılacak string
#• islem_tipi → Yapılacak işlem türü ("ters", "buyuk", "kucuk", "uzunluk")
#Fonksiyon, islem_tipi parametresine göre şu işlemleri yapmalıdır:
#• "ters" → Metni ters çevirir.
#• "buyuk" → Tüm harfleri büyük yapar.
#• "kucuk" → Tüm harfleri küçük yapar.
#• "uzunluk" → Metnin karakter uzunluğunu döndürür.
#• Geçersiz bir işlem girilirse "Geçersiz işlem" mesajı döndürmelidir.

def metin_isle(metin, islem_tipi):
    if islem_tipi == "ters":
        return metin[::-1]
    elif islem_tipi == "buyuk":
        return metin.upper()
    elif islem_tipi == "kucuk":
        return metin.lower()
    elif islem_tipi == "uzunluk":
        return len(metin)
    else:
        return "Geçersiz işlem"

metin = input("Lütfen bir metin girin: ")
islem = input("İşlem türünü girin (ters, buyuk, kucuk, uzunluk): ")

sonuc = metin_isle(metin, islem)
print("Sonuç:", sonuc)
