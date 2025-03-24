#Aşağıdaki liste içindeki tek sayıları bulan bir fonksiyon yazın.
#sayilar = [10, 15, 20, 25, 30, 35]

def tek_sayilari_bul(liste):
    tek_sayilar = []
    for sayi in liste:
        if sayi % 2 != 0:
            tek_sayilar.append(sayi)
    return tek_sayilar

sayilar = [10, 15, 20, 25, 30, 35]
tekler = tek_sayilari_bul(sayilar)
print("Tek sayılar:", tekler)

