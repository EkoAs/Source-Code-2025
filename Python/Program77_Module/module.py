#  module python
import os 
os.system("cls")

# cara biasa
# import mtk
# hasil = mtk.tambah(2, 4)
# print(hasil)

# import menggunakan from
from mtk import tambah, kali, kurang, pangkat
# hasil = tambah(2, 4) # tidak perlu menggunakan namafile.tambah()
# print(hasil)
print(f"tambah = {tambah(2, 4, 2, 2)}")
print(f"kurang = {kurang(2, 4, 2, 1, 1)}")
print(f"kali = {kali(3, 2, 2, 2)}")
print(f"pangkat = {pangkat(2)(2)}")

#  menggunakan alias # harus satu satu
from mtk import tambah as add 
print(f"tambah with add = {add(2, 4, 2, 2)}")

# cara lain
import mtk as math
hasil = math.tambah(2, 6)
print(f"Hasil math = {hasil}")
