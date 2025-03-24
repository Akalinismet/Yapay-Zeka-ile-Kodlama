#Aşağıdaki matematiksel işlemleri gerçekleştiren fonksiyonları eksiksiz bir şekilde yazın.
#Fonksiyon Açıklamaları:
#• topla(sayi1, sayi2) → İki sayının toplamını döndürür.
#• bolme(sayi1, sayi2) → İlk sayıyı ikinci sayıya böler. Eğer bölen 0 ise "Bölen
#kısım 0 olamaz" mesajını döndürür.
#• carpma(sayi1, sayi2) → İki sayının çarpımını döndürür.
#• cikarma(sayi1, sayi2) → İlk sayıdan ikinciyi çıkarıp sonucu döndürür.
#• mod(sayi1, sayi2) → İlk sayının ikinci sayıya göre modunu döndürür.

def calculator():
    islem = input("Yapmak istediğiniz işlemi giriniz:(topla,cikarma,bolme,carpma,mod):")
    sayi1 = int(input("sayi1'i giriniz:"))
    sayi2 = int(input("sayi2'yi giriniz:"))
    match islem:
        case "topla":
            print(f"Sonuç: {sayi1 + sayi2}")
        case "cikarma":
            print(f"Sonuç: {sayi1 - sayi2}")
        case "bolme":
            if sayi2 > 0:
                print(f"Sonuç: {sayi1 / sayi2}")
            else:
                print("Bölen Kısım 0 Olamaz")
        case "carpma":
            print(f"Sonuç: {sayi1 * sayi2}")
        case "mod":
            print(f"Sonuç: {sayi1 % sayi2}")
        case _:
            print("Geçersiz işlem veya Yanlış Format Kullandınız")

calculator()