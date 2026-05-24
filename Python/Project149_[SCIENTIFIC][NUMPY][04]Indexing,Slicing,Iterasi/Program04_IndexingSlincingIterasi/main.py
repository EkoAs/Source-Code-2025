# mengambil nilai dari sebuah array nilai

import numpy as np

a=np.arange(10)**2
print(a)

# mengambil nilai
print("elemen kesatu dari a adalah ", a[0])
print("elemen kesatu dari a adalah ", a[6])
print("elemen kesatu dari a adalah ", a[-1]) #elemen paling akhir pakai -1

# slicing mengambil rentang dari array tersebut
print("elemen satu sampai enam", a[0:5]) # batas sebelum akhir disebut eksusif [start,end]
print("elemen satu sampai enam", a[0:6]) # pakai langsung ke 6

# ambil dari 4 sampai akhir
print("elemen 4 sampai akhir", a[3:]) # end nya dikosongkan

# kebalikannya, dari awal sampai lima
print("elemen awal sampai 5", a[:5]) # start nya dikosongkan


# Iterasi
for i in a:
    print(f"value = {i}")