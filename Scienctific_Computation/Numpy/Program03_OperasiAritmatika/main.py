import numpy as np

a = [1,2,3,4,5]
b = [6,7,8,9,10]

# // array numpy
np_a = np.array([1,2,3,4,5])
np_b = np.array([6,7,8,9,10])

# operasi aaritmatika
# penjumlaham

# list = hasil nempel
hasil = a+b
print(hasil)

# numpy = hasil di tambahkan
# disebut elementwise operation = operasinya per elemen
hasil = np_a + np_b
print(hasil)

# pengurangan list tidak bisa. harus array
hasil = np_a - np_b
print(hasil)

# perkallian
hasil = np_a * np_b
print(hasil)

# bagi 
hasil = np_a / np_b
print(hasil)

# kuadrat
hasil = np_a **2
print(hasil)

# multidimensi array numpy
c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[10,11,12]))
hasil = c + d
print(hasil)
# kalau dikali bukan perkalian matrik, setiap operator di numpy, dikalikan atau apapun di 
# pada setiap elemennya. bukan kayak matriks