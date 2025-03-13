#Soru2
def ikinci_en_buyuk(liste):
    benzersiz_sayilar = list(set(liste))
    if len(benzersiz_sayilar) < 2:
        return None
    benzersiz_sayilar.remove(max(benzersiz_sayilar))
    return max(benzersiz_sayilar)

liste = list(map(int, input("Sayıları boşluk ile ayırarak girin: ").split()))
ikinci_buyuk = ikinci_en_buyuk(liste)

if ikinci_buyuk is not None:
    print(f"Listenin en büyük ikinci sayısı: {ikinci_buyuk}")
else:
    print("Listede en büyük ikinci sayı bulunmuyor.")