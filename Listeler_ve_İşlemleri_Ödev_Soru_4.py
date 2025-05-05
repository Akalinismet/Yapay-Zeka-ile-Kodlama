urunler = {
    "Telefon": {"yil": 2019},
    "Televizyon": {"yil": 2014},
    "Laptop": {"yil": 2021}
}

yeni_urunler = []

for urun, bilgi in urunler.items():
    if bilgi["yil"] > 2015:
        yeni_urunler.append(urun)

print("2015 yılından sonra çıkan ürünler:", yeni_urunler)
