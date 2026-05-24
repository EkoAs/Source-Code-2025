# deep list pada nested list
# mengambil data dalam list dalam list

data0 = [1, 2, 3, 4]
data1 = [1, 2, 3, 4]
data2D = [data0, data1]
print(f"data gabung = {data2D}")
# mengambil data 4 pada data0
print(f"data ke 3 pada list ke 0 = {data2D[0][3]}")

# untuk menggunakan deep copy
from copy import deepcopy
dataCopy = data2D.copy()
dataDeep = deepcopy(data2D)

data2D[0][2] = 9 # perbandingan antar copy dam deepcopy
dataDeep[0][2] = 9
dataCopy[0][2] = 6

print(f"Data setelah di ubah = {data2D}")
print(f"addres dari data 2d = {hex(id(data2D))}")
print(f"addres dari data copy = {hex(id(dataCopy))}")
print(f"addres dari data deep = {hex(id(deepcopy))}\n")

print(f"addres dari 9 = {hex(id(data2D))}")
print(f"addres dari 9 deep = {hex(id(dataDeep))}")
print(f"addres dari 6 copy = {hex(id(dataCopy))}\n")


import copy
a = [1, 2, 3]
c = copy.deepcopy(a)  # Deep copy dari a
print(hex(id(a)))  # Alamat memori dari elemen pertama di a
print(f"{hex(id(c))}\n ") # Alamat memori dari elemen pertama di c
c[1] = 8
print(f"{c}")
print(f"{hex(id(a[2]))}\n ") # Alamat memori dari elemen pertama di a
print(f"{hex(id(c[2]))}\n ") # Alamat memori dari elemen pertama di c
