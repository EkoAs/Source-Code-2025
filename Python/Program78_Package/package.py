# package adalah tempat untuk menyimpan module. 
# tinggal bilang folder apa susahnya
# cara memanggil 
from sains import mtk
hasil = mtk.tambah(1,2,3,4)
print(hasil)
hasil = mtk.kurang(1)
print(hasil)
hasil = mtk.kali(3)(2)
print(hasil)

from sains.fisika import massa as berat
hasil = berat(2)
print(hasil)