#Liste ve List Comprehension Kullanımı
#Aşağıdaki işlemleri gerçekleştiren bir Python kodu yazın:
#"Ankara", "İstanbul", "İzmir", "Bursa", "Antalya", "Adana", "Trabzon"
#şehir isimlerini içeren bir liste oluşturun.
#İ harfi içeren şehirleri yeni bir listeye ekleyin.
#Aynı işlemi list comprehension kullanarak gerçekleştirin.


sehirler = ["Ankara", "İstanbul", "İzmir", "Bursa", "Antalya", "Adana", "Trabzon"]
i_harfli_sehirler = [sehir for sehir in sehirler if "İ" in sehir or "i" in sehir]
print("İ harfi içeren şehirler:", i_harfli_sehirler)
