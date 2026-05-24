# Nested list/ list dalam list
list0 = ["Ucup", "Otong", "Ujang"]
list1 = ["Udin", "Rian", "Mikael"]
listJoin = [list0, list1, 2, 4, 5, 6 ] # gabungan list 0 dan 1 serta list campuran di belakangnya
print(f"Gabungan list = {listJoin}")

listNama0 = ["Ucup", 17, "Laki-Laki"]
listNama1 = ["Otong", 16, "Laki-Laki"]
listNama2 = ["Dedeng", 19, "Laki-Laki"]
listAnggota = [listNama0, listNama2, listNama2]
# program daftar anggota sedehana dengan nested list dan loop
for peserta in listAnggota :
    print(f"Nama = {peserta[0]}")
    print(f"Umur = {peserta[1]}")
    print(f"Gender = {peserta[2]} \n")
    
    
