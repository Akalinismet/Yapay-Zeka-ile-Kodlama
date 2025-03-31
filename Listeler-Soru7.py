#Sözlük Güncelleme ve Erişim
#Aşağıda verilen ogrenci sözlüğü üzerinde belirtilen işlemleri gerçekleştirin.
#ogrenci = {"isim": "Ahmet", "yas": 20, "bolum": "Bilgisayar Mühendisliği"}
#A) "yas" değerini 21 olarak güncelleyin.
#B) Sözlüğe "okul" anahtarını "İTÜ" değeri ile ekleyin.
#C) "isim" anahtarına karşılık gelen değeri ekrana yazdırın.

ogrenci = {"isim": "Ahmet", "yas": 20, "bolum": "Bilgisayar Mühendisliği"}
ogrenci["yas"] = 21
ogrenci["okul"] = "İTÜ"
print("Öğrencinin ismi:", ogrenci["isim"])
