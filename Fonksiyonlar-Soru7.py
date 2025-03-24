#Aşağıdaki iki fonksiyonu oluşturun:
#1. kelime_sayisi(metin)
#a. Verilen metindeki kelime sayısını döndürmelidir.
#2. cumle_analiz(metin)
#a. kelime_sayisi fonksiyonunu kullanarak metindeki kelime sayısını
#hesaplamalıdır.
#b. Cümlede 5 veya daha fazla kelime varsa "Cümle uzun",
#aksi takdirde "Cümle kısa" çıktısını döndürmelidir.
# İpucu: Kelime sayısını bulmak için .split() metodunu kullanabilirsiniz.


def kelime_sayisi(metin):
    kelimeler = metin.split()
    return len(kelimeler)

def cumle_analiz(metin):
    sayi = kelime_sayisi(metin)
    if sayi >= 5:
        return "Cümle uzun"
    else:
        return "Cümle kısa"

metin = input("Bir cümle girin: ")

print("Kelime sayısı:", kelime_sayisi(metin))
print("Analiz:", cumle_analiz(metin))

