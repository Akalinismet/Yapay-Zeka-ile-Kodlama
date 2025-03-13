def sirala(liste):
    kucukten_buyuge = sorted(liste)
    buyukten_kucuge = sorted(liste, reverse=True)
    return kucukten_buyuge, buyukten_kucuge


liste = list(map(int, input("Sayıları boşluk ile ayırarak girin: ").split()))
kucukten_buyuge, buyukten_kucuge = sirala(liste)


print(f"Küçükten büyüğe sıralama: {kucukten_buyuge}")
print(f"Büyükten küçüğe sıralama: {buyukten_kucuge}")
