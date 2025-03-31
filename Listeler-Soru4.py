#Enumerate Kullanımı
#Aşağıdaki liste verilmiştir:
#dersler = ["Matematik", "Fizik", "Kimya", "Biyoloji"]
#Bu listeyi enumerate fonksiyonunu kullanarak her elemanın sırasıyla birlikte ekrana
#yazdıran bir kod yazın.


dersler = ["Matematik", "Fizik", "Kimya", "Biyoloji"]
for index, ders in enumerate(dersler):
    print(index, ders)