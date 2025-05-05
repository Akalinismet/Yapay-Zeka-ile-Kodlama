kitap_stok = {"1984": 4, "Sefiller": 2, "Martı": 5}

kitap_adi = input("Lütfen almak istediğiniz kitabın adını girin: ")
adet = int(input("Kaç adet almak istiyorsunuz? "))

if kitap_adi in kitap_stok:
    if kitap_stok[kitap_adi] >= adet:
        kitap_stok[kitap_adi] -= adet
        print("Sipariş tamamlandı.")
        print(f"Güncel stok: {kitap_stok[kitap_adi]} adet kaldı.")
    else:
        print("Yetersiz stok.")
else:
    print("Kitap bulunamadı.")
