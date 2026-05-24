# Operasi List 
data = [1, 3, 4, 6, 7, 8, 9, 5, 6, 7, 4, 6, 6, 2, 6, 3, 4, 5, 6, 7, 8, 9, 10]
# menghiutng jumlah data 
jumlahData = data.count(6)  # menghitung jumlah kemunculan angka 6
print(f"Jumlah angka 6 dalanm data adalah {jumlahData}")

# posisi data index 
dataIndex = data.index(3)  # mencari posisi angka 3 dalam list
print(f" posisi angka 3 dalam list adalah {dataIndex}")

# mengurutkan posisi
data.sort()  # mengurutkan data secara ascending
print(f"data setelah di urutkan : \n{data}")
data.reverse()  # membalik urutan data
print(f"urutan data secara terbalik : \n{data}")