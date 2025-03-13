liste = list(map(int, input("Lütfen sayıları boşlukla ayırarak girin: ").split()))

yeni_liste = [x * 2 for x in liste]

print("Yeni liste:", yeni_liste)