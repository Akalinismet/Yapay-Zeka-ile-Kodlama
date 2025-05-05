sehir_bilgi = {
    "Berlin": {"nüfus": 3_600_000},
    "Madrid": {"nüfus": 3_200_000}
}

sehir_adi = input("Lütfen şehir adını girin: ")

if sehir_adi in sehir_bilgi:
    print(sehir_bilgi[sehir_adi])
else:
    print("Veri yok")
