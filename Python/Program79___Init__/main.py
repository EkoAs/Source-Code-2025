import sains
hasil = sains.tambah(1,2,3,4)
print(hasil)

# memanggil nama foldernya lalu nama fungsinya
# dari sub folder ke dua
hasilFisika = sains.pisika.massa(2)
print(hasilFisika(2))
hasilAngin = sains.pisika.angin(2)
print(hasilAngin(2))

# cara lain import
from sains import pisika 
hasilAngin = pisika.angin(2)
print(f"Hasil dari pisika {hasilAngin(2)}")


# cara ke dua 
# from sains import *
# hasil = mtk.tambah(1,2,3)
# print(f"Hasil cara ke 2 {hasil}")

