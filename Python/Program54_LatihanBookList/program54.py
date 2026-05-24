# Latihan List 
# membuat Daftar buku 
listEmpty = []
while True:
    print(f"Masukan data buku")
    inputUser = str(input("Masukan Judul : "))
    inputUser2 = str(input("Masukan Penulis : "))
    bookData = [inputUser, inputUser2]
    listEmpty.append(bookData) # Menambahkan data kedalam list kosong
    
    # Perintah
    print(f"Want to countine?")
    inputUserEnd = str(input("y/n :\t"))
    if inputUserEnd.lower() == "n":
        break

print(f"\n")    
# daftar buku setelah di masukan datanya
print(f"Daftar Buku | Penulis")
index = 0
for book in listEmpty:
    index += 1
    print(f"{index} | {book[0]} | {book[1]}")
        # Menampilkan index/nomor, judul buk dan penulis
print("End\n")