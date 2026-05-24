# latihan list # membuat list dari input user
listInput = str(input("Masukan daftar nama :/t")) # contoh input: Ucup, Otong, Deden, Ujang, Asep
listJoin = listInput.split(',')  # memisahkan string menjadi list
listJoin.sort()  # mengurutkan list secara descending
print(f"List nama : {listJoin}")
listJoin.reverse()
print(f"dengan urutan terbalik :\n {listJoin}")
