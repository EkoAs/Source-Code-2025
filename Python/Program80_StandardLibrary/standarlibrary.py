# standar library
# contoh 1
import datetime
waktu = datetime.datetime.now()
print(f"Waktu sekarang = {waktu}")
# mengambil salah satunya saja
print(f"Sekarang hari {waktu.strftime('%A')}")
print(f"Sekarang tahun {waktu.year}")
print(f"Sekarang bulan ke {waktu.month}")

print("\n")
# contoh 2 import output file
import io # standard library
file = io.open("buku.txt","r")
print(f"Isi dari file adalah : \n {file.read()}")

print("\n")
# contoh tiga
from collections import Counter
data = [1,2,3,2,1,4,1,4,1,4,4]
hasil = Counter(data)
print(f"Hasil count = {hasil}")
# menghitung salah satunya saja 
print(f"Hasil 1 adalah = {hasil[1]}")
print(f"Hasil 4 adalah = {hasil[4]}")




