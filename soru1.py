#Soru1
def tekrar_bul(liste):
    tekrarlar = {}
    for eleman in liste:
        if liste.count(eleman) > 1:
            tekrarlar[eleman] = liste.count(eleman)

    return tekrarlar



liste = input("Liste elemanlarını boşluk ile ayırarak girin: ").split()
tekrar_edenler = tekrar_bul(liste)

if tekrar_edenler:
    for eleman, tekrar in tekrar_edenler.items():
        print(f"'{eleman}' elemanı {tekrar} kez tekrar ediyor.")
else:
    print("Listede tekrar eden eleman yok.")