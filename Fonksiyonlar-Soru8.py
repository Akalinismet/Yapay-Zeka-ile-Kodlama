#1’den verilen sayıya kadar olan sayıların toplamını hesaplayan recursive fonksiyon
#yazın.
#Kurallar:
#• toplam(n) fonksiyonu, 1’den n’e kadar olan sayıların toplamını
#döndürmelidir.
#• Durdurma koşulu → n == 1 olduğunda fonksiyon durmalıdır.


def toplam(n):
    if n == 1:
        return 1
    return n + toplam(n - 1)

n = int(input("Bir sayı girin: "))

print(f"1'den {n}'e kadar olan sayıların toplamı: {toplam(n)}")


