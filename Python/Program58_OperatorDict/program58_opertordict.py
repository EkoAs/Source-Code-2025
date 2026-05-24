# Operator DIctionary
dataDict = {
    'cup':"ucup",
    'tong':"otong"
}

# menghitung jumlah data
LENPICT = len(dataDict)
print(f"Jumlah data dict : {LENPICT}")

# mengecek key ada atau tidak
KEY = 'cup'
CHECKKEY = KEY in dataDict
print(f"Data cup : {CHECKKEY}")

# mengakses value read dengan get
print(f"data cup : {dataDict.get('cup')}")
print(f"data cup : {dataDict.get('kiss','data is not found')}")
# penggunaan get untuk mencegah error ketika data tak di temukan 

# mengubah data
dataDict['cup'] = 'rian'
print(f"data setelah di ubah {dataDict}")

# menambah data 
dataDict['sep'] = 'asep'
print(f"Data setelah di tambah {dataDict}")

# update stattement
# baca buku untuk selengkapnya 
dataDict.update({'dung':'dudung'})
dataDict.update({'cup':'ucup'}) # dijelaskan di buku
print(f"data setelah di kembalikan nilainya {dataDict}")

# menghapus data 
del dataDict['tong']
print(f"data setelah di hapus {dataDict}")