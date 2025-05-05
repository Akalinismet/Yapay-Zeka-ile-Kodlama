fiyatlar = {
    "masa": 1200,
    "sandalye": 450,
    "lamba": 300
}

# Her ürünün fiyatına %15 zam yapıyoruz
for urun, fiyat in fiyatlar.items():
    fiyatlar[urun] = fiyat * 1.15

print(fiyatlar)
