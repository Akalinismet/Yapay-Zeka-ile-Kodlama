#List Comprehension Kullanımı
#Aşağıdaki işlemleri gerçekleştiren bir Python kodu yazın:
#1 ile 50 arasındaki sayıları içeren bir liste oluşturun.
#Bu listenin sadece 5’e bölünebilen elemanlarını içeren yeni bir liste oluşturun
#(List Comprehension kullanarak).

sayilar = list(range(1, 51))
besin_katlari = [sayi for sayi in sayilar if sayi % 5 == 0]
print("5'e bölünebilen sayılar:", besin_katlari)
