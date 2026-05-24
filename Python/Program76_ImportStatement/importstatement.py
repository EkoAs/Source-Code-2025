# import statement 

# mengambil program dari file lain
# contoh 1
import hello

# contoh 2 import dengan data
import data
print(f"{data.num}") # memanggil menggunakan nama file.nama variabel
print(f"{data.nama}")

# contoh 3 dengan fungsi
import fungsi
hasil = fungsi.tambah(2, 6)
print(hasil)

# contoh 4 dengan input

x = int(input("masukan angka1: "))
y = int(input("masukan angka2: "))

print(f"hasil {fungsi.end(x,y)}")