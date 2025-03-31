#Küme (Set) İşlemleri
#Aşağıda iki küme verilmiştir:
#A = {10, 20, 30, 40, 50}
#B = {30, 40, 50, 60, 70}
#Bu kümeleri kullanarak aşağıdaki işlemleri gerçekleştirin:
#A) A ve B kümelerinin birleşimini bulun.
#B) A ve B kümelerinin kesişimini bulun.
#C) A kümesinde olup B kümesinde olmayan elemanları bulun.
#D) B kümesinde olup A kümesinde olmayan elemanları bulun.


A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}
print("A ve B birleşimi:", A | B)
print("A ve B kesişimi:", A & B)
print("A kümesinde olup B'de olmayanlar:", A - B)
print("B kümesinde olup A'da olmayanlar:", B - A)