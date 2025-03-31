#1.Liste İşlemleri
#meyveler = ["elma", "muz", "çilek", "kiraz"]
#Listenin sonuna "portakal" ekleyin.
#Listenin 2. indeksindeki öğeyi "armut" ile değiştirin.
#"muz" öğesini listeden kaldırın.
#Listenin uzunluğunu ekrana yazdırın.

meyveler = ["elma", "muz", "çilek", "kiraz"]
meyveler.append("portakal")
meyveler[2] = "armut"
meyveler.remove("muz")
print("Listenin uzunluğu:", len(meyveler))
