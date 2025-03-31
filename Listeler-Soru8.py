#Sözlük (Dictionary) Üzerinde Döngü Kullanımı
#Aşağıda verilen ders_notlari sözlüğündeki öğrencilerin isimlerini ve notlarını ekrana
#yazdıran bir Python kodu yazın.
#ders_notlari = {
# "Ali": 85,
# "Zeynep": 90,
# "Mehmet": 78,
# "Elif": 95
#}

ders_notlari = {"Ali": 85, "Zeynep": 90, "Mehmet": 78, "Elif": 95}
for isim, notu in ders_notlari.items():
    print(isim, "notu:", notu)
