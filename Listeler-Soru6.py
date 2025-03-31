#Tuple İşlemleri
#Aşağıda verilen veriler isimli tuple üzerinde aşağıdaki işlemleri gerçekleştirin:
#veriler = (5, 10, 15, 20, 25, 30, 35)
#A) veriler tuple’ının ilk üç elemanını ekrana yazdırın.
#B) veriler tuple’ının son iki elemanını ekrana yazdırın.
#C) veriler tuple’ının uzunluğunu bulun.
#D) veriler içinde 20 sayısının olup olmadığını kontrol edin.


veriler = (5, 10, 15, 20, 25, 30, 35)
print("İlk üç eleman:", veriler[:3])
print("Son iki eleman:", veriler[-2:])
print("Tuple uzunluğu:", len(veriler))
print("20 var mı?", 20 in veriler)