#soru1
#sayi1 = int(input("birinci sayıyı giriniz:"))
#sayi2 = int(input("ikinci sayıyı giriniz:"))
#toplam = sayi1 + sayi2
#print(toplam)

#soru2
#sayi3 = int(input("bir sayı giriniz:"))

#if sayi3 > 0 :
#    print("pozitif sayı girdiniz")
#elif sayi3 < 0 :
#    print("negatif sayı girdiniz")
#else:
#    print("0 girdiniz")

#soru3
#a= int(input("ilk sayıyı gırınız"))
#b = int(input("ikinci sayıyı giriniz:"))
#c = int(input("üçüncü sayıyı giriniz:"))

#en_buyuk = a

#if b > en_buyuk:
#    en_buyuk = b

#if c > en_buyuk:
#    en_buyuk = c

#print("En büyük sayı:", en_buyuk)


#soru4
#sayi4 = int(input("sayıyı giriniz:"))

#if sayi4 %2 == 0 :
#    print("girdiğiniz sayı çift")
#else:
#    print("girdiğiniz sayı tek")


#soru5
#sayi5 = int(input("gün numarısını giriniz:"))
#match sayi5:
#    case 1:
#        print("gününüz pazartesi")
#    case 2:
#        print("gününüz salı")
#    case 3:
#        print("gününüz çarşamba")
#    case 4:
#        print("gününüz perşembe")
#    case 5:
#        print("gününüz cuma")
#    case 6:
#        print("gününüz cumartesi")
#    case 7:
#        print("gününüz pazar")
#    case _:
#        print("geçersiz giriş")

#soru6
#sayi6 = int(input("birinci sayıyı giriniz"))
#sayi7 = int(input("ikinci sayıyı giriniz"))
#islem = input("yapılmasını istediğiniz işlemi giriniz")
#toplam = sayi6 + sayi7
#fark = sayi6 - sayi7
#carpim = sayi6 * sayi7
#bolum = sayi6 / sayi7

#match islem:
#    case "+":
#        print(toplam)
#    case "-":
#        print(fark)
#    case "/":
#        print(bolum)
#    case "*":
#        print(carpim)
#    case _:
#        print("geçersiz işlem girdiniz")


#soru7
#N = int(input("Bir sayı giriniz: "))
#toplam = 0

#for i in range(1, N + 1):
#    toplam += i

#print(f"1'den {N}'e kadar olan sayıların toplamı:",toplam)



#soru8
#sayi = int(input("tablosunu istediğiniz sayıyı giriniz:"))

#for j in range(1,11):
#    print(f"{sayi} * {j}=",sayi*j)



#soru9
#toplam = 0
#for i in range(5):
#    sayi = int(input(f"{i+1}.sayı giriniz:"))
#    toplam += sayi

#print("sayılarınızın ortalaması:",toplam/5)



#soru10
#asal = int(input("Bir sayı giriniz: "))

#if asal > 1:
#    for i in range(2, asal):
#        if asal % i == 0:
#            print("sayınız asal değil.")
#            break
#    else:
#        print("sayınız asal bir sayıdır.")
#else:
#    print("sayınız asal değil.")


#soru11
#sayim = int(input("Bir sayı giriniz: "))
#faktoriyel = 1
#i = 1

#while i <= sayim:
#    faktoriyel *= i
#    i += 1

#print(f"{sayim}! = {faktoriyel}")


#soru12
#print("Sayı Tahmin Oyununa Hoş Geldiniz")
#print("5 Tahmin hakkınız var")

#dogru_sayi = 78
#i = 5
#while i != 0:
#    tahmin = int(input("tahmininizi giriniz"))
#    if tahmin == dogru_sayi:
#        print("doğru tahmin tebrikler")
#        break
#    else:
#        print(f"tekrar dene {i-1} hakkınız kaldı ")
#    i -= 1

#if i == 0:
#    print("hakkınızı doldurdunuz")



#soru13
#n = int(input("Bir sayı giriniz: "))

#a, b = 0, 1
#print("Fibonacci Serisi:")
#for i in range(n):
#    print(a, end=" ")
#    a, b = b, a + b

#soru14
#num = int(input("Bir sayı giriniz: "))
#ters_sayi = 0

#while num > 0:
#    digit = num % 10
#    ters_sayi = ters_sayi * 10 + digit
#    num //= 10

#print("Tersine çevrilmiş sayı:", ters_sayi)


#soru15
#num = int(input("Bir sayı giriniz: "))
#original_num = num
#basamak_sayisi = len(str(num))
#toplam = 0

#while num > 0:
#    digit = num % 10
#    toplam += digit ** basamak_sayisi
#    num //= 10

#if toplam == original_num:
#    print(f"{original_num} bir Armstrong sayısıdır.")
#else:
#    print(f"{original_num} bir Armstrong sayısı değildir.")


#soru16
#toplam = 0
#for i in range(1,101):
#    if i %2 ==0:
#        toplam += i
#print("1 ile 100 arasındaki çift sayıların toplamı:",toplam)



#soru17
#sonuc = 1
#for i in range(1,11):
#    if i % 2 == 1:
#        sonuc *= i
#print("1 ile 10 arasındaki tek sayıların çarpımı:",sonuc)



#soru18
#for j in range(1,11):
#    print(f"{j}'nin karesi:",j**2)



#soru19
#sifre = input("şifrenizi giriniz:")

#if sifre == "python123":
#    print("giriş başarılı")
#else:
#print("yanlış şifre tekrar deneyiniz")


#soru20
#yas = int(input("yaşınızı giriniz:"))
#if yas >= 18:
#    print("Reşit")
#else:
#    print("reşit değil")


#soru21
#vize1 = int(input("1.vize notunuzu giriniz:"))
#vize2 = int(input("2.vize notunuzu giriniz:"))
#final = int(input("final notunuzu giriniz:"))

#durum = (vize1 + vize2 + final)/3

#if durum >= 50:
#    print("geçti ort:",durum)
#else:
#    print("kaldınız ort:",durum)



#soru22
#boy = int(input("boyunuzu cm cinsinden giriniz:"))
#kilo = int(input("kilonuzu kg cinsinden giriniz"))

#boy_m_cinsi = boy/100
#vki = kilo / (boy_m_cinsi**2)
#vki = int(vki)
#if vki >= 25:
#    print(f"Vucut kitle endeksiniz:{vki} !!Fazla Kilolu!!")
#else:
#    print(f"Vucut kitle endeksiniz:{vki} !!İdeal Kilo!!")


#soru23
#sayi1 = int(input("1.sayıyı giriniz:"))
#islem =  input("işleminizi giriniz(+,-,/,*)")
#sayi2 = int(input("2.sayıyı giriniz:"))

#match islem:
#    case "+":
#        print(sayi1 + sayi2)
#    case "-":
#        print(sayi1 - sayi2)
#    case "/":
#        print(sayi1 / sayi2)
#    case "*":
#        print(sayi1 * sayi2)
#    case _:
#        print("desteklenmeyen/geçersiz işlem")


#soru24
#sayi11 = int(input("1.sayıyı giriniz:"))
#sayi12 = int(input("2.sayıyı giriniz:"))
#sayi13 = int(input("3.sayıyı giriniz:"))
#sayi14 = int(input("4.sayıyı giriniz:"))

#enkucuk = sayi11

#if sayi12 < enkucuk:
#    enkucuk = sayi12
#if sayi13 < enkucuk:
#    enkucuk = sayi13
#if sayi14 < enkucuk:
#    enkucuk = sayi14

#print("En küçük sayı:",enkucuk)


#soru25
#sayi1 = int(input("1. sayıyı giriniz: "))
#sayi2 = int(input("2. sayıyı giriniz: "))
#sayi3 = int(input("3. sayıyı giriniz: "))

#if sayi1 <= sayi2 and sayi1 <= sayi3:
#    if sayi2 <= sayi3:
#        print(f"{sayi1} < {sayi2} < {sayi3}")
#    else:
#        print(f"{sayi1} < {sayi3} < {sayi2}")
#elif sayi2 <= sayi1 and sayi2 <= sayi3:
#    if sayi1 <= sayi3:
#        print(f"{sayi2} < {sayi1} < {sayi3}")
#    else:
#        print(f"{sayi2} < {sayi3} < {sayi1}")
#else:
#    if sayi1 <= sayi2:
#        print(f"{sayi3} < {sayi1} < {sayi2}")
#    else:
#        print(f"{sayi3} < {sayi2} < {sayi1}")


#soru26
#sinir = int(input("sınır sayınızı giriniz:"))

#toplam = 0
#sayi = 1

#while sayi <= sinir:
#    toplam += sayi
#    sayi += 1

#print(f"1'den {sinir}'e kadar olan sayıların toplamı:",toplam)


#soru27
#sonuc = 1
#for i in range(1,6):
#    sonuc *= i
#print("1 ile 5 arasındaki sayıların çarpımı:",sonuc)


#soru28
#sonuc = 0
#for i in range(1,11):
#    sonuc += i**2
#print("1-10 aralığındaki sayıların kareleri toplamı:",sonuc )


#soru29
#sinirim = int(input("sınır sayınızı giriniz:"))
#sonuc = 0
#for p in range(1,sinirim+1):
#    sonuc += p**3
#print(f"1 ile {sinirim} aralığındaki sayıların küpleri toplamı:",sonuc)


#soru30
#for i in range(1,100):
#    if i % 3 == 0 and i % 5 == 0:
#        print(i)


#soru31
#sinav_notu = int(input("0-100 aralığındaki notunuzu giriniz:"))

#if 100 >= sinav_notu >= 90:
#    print("A")
#elif 89 >= sinav_notu >= 80:
#    print("B")
#elif 79 >= sinav_notu >= 70:
#    print("C")
#elif 69 >= sinav_notu >= 60:
#    print("D")
#elif 59 >= sinav_notu >= 0 or 00:
#    print("F")
#else:
#    print("aralık dışı veya geçersiz değer girdiniz")


#soru32
#sayia = int(input("1.sayıyı giriniz:"))
#sayib = int(input("2.sayıyı giriniz:"))
#sayic = int(input("3.sayıyı giriniz:"))

#if sayia == sayib == sayic:
#    print("tüm sayılar eşit")
#elif sayia == sayib or sayia == sayic or sayib == sayic:
#    print("en az iki sayı eşit")
#else:
#    print("sayılar eşit değil")


#soru33
#yil = int(input("artık yıl kontrolu ıcın sayı gırınız:"))

#if yil %400 == 0:
#    print(f"{yil} artık bir yıldır")
#elif yil %4 == 0 and yil %100 != 0:
#    print(f"{yil} artık bir yıldır")
#else:
#    print(f"{yil} artık bir yıl değildir")


#soru34
#boy = int(input("boyunuzu cm cinsinden giriniz:"))
#kilo = int(input("kilonuzu kg cinsinden giriniz:"))

#boyi = boy /100
#BMI = kilo/(boyi)**2

#if BMI < 18.5:
#    print("Zayıf")
#elif 18.5 <= BMI < 25:
#    print("Normal")
#elif 25 <= BMI < 30:
#    print("Fazla Kilolu")
#elif BMI >= 30:
#    print("Obez")


#soru35
#kenar1 = int(input("1.kenarı giriniz:"))
#kenar2 = int(input("2.kenarı giriniz:"))
#kenar3 = int(input("3.kenarı giriniz:"))

#if kenar1+kenar2>kenar3 and kenar1+kenar3>kenar2 and kenar2+kenar3>kenar1:
#    if kenar1 == kenar2 == kenar3:
#        print("eşkenar üçgen")
#    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
#        print("ikizkenar üçgen")
#    else:
#        print("çeşitkenar üçgen")
#else:
#   print("üçgen için geçersiz ölçüler")


#soru36
#yas = int(input("yaşınızı giriniz:"))

#if 5 >= yas >= 0:
#    print("ücretsiz bilet")
#elif 18 >= yas >= 6:
#    print("bilet ücretiniz 10 TL")
#elif 64 >= yas >= 19:
#    print("bilet ücretiniz 20 TL")
#elif yas >= 65:
#    print("bilet ücretiniz 15 TL")
#else:
#    print("geçersiz yaş bilgisi girdiniz")


#soru37
#hava_durumu = input("Hava Durumunu Giriniz:")
#sicaklik = int(input("Hava Sıcaklıığını Giriniz:"))

#if hava_durumu == "güneşli" and sicaklik >= 25:
#    print("Piknik Yapabilirsiniz")
#elif hava_durumu == "yağmurlu":
#    print("Şemsiye Almayı Unutmayınız")
#elif hava_durumu == "karlı" and sicaklik < 0:
#    print("Kayak Yapmaya Gidebilirsiniz")
#else:
#    print("Evde Kalabilirsiniz")


#soru38
#sayicim = int(input("sayınızı giriniz:"))

#if sayicim > 0:
#    print("sayınız pozitif")
#elif sayicim < 0:
#    print("sayınız negatif")
#else:
#    print("sayınız 0'dır")


#soru39
#a = int(input("birinci sayıyı giriniz:"))
#b = int(input("ikinci sayıyı giriniz:"))

#if a > b:
#    print(f"birinci sayı daha büyük ({a})")
#elif a < b:
#    print(f"ikinci sayı daha büyük ({b})")
#else:
#    print("iki sayı birbirine eşit")


#soru40
#tutar = int(input("Alışveriş Tutarınızı Giriniz:"))
#üyelik = input("Üyelik Durumunuzu Giriniz:(üye/non-üye):")

#if üyelik == "üye":
#    t = tutar - (tutar/10)
#    print(f"indirimli tutarınız {t}")
#elif üyelik == "non-üye":
#    p = tutar - (tutar/20)
#    print(f"indirimli tutarınız {p}")
#else:
#    print("geçersiz üyelik bilgisi")


































































