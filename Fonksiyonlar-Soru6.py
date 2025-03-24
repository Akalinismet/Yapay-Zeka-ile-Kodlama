#Aşağıdaki özelliklere sahip bir fonksiyon yazın:
#• isim_ekle adlı fonksiyon, birden fazla isim alabilmelidir.
#• Fonksiyon, isimlerin saklandığı boş bir liste olan isimler adlı bir liste
#kullanmalıdır.
#• args kullanarak, parametre olarak verilen tüm isimleri büyük harf formatında
#isimler listesine eklemelidir.
#• Fonksiyon en son olarak isimler listesini döndürmelidir.

def isim_ekle(*args):
    isimler = []
    for isim in args:
        isimler.append(isim.upper())
    return isimler

girdi = input("Lütfen isimleri virgül ile ayırarak girin: ")

isim_listesi = girdi.split(',')

isim_listesi = [isim.strip() for isim in isim_listesi]

sonuc = isim_ekle(*isim_listesi)
print("Büyük harfli isim listesi:", sonuc)

