# Global and Local scope 

# contoh global
nama = 'Ucup' # ini adalah global. berada di luar fungsi
def hello():
    print(f"Halo {nama}")  # bisa di akses dimana saja
hello()

# Contoh 2
def hello2():
    name = "Otong" # ini adalah lokal, berada di dalam fungsi
    print(f"local = {name}") # hanya bisa di panggil di dalam fungsi
hello2()
# print(f"tidak bisa di akses {name}") # akan error

#  menggunakan global untuk ubah # contoh 3
numb = 0
print(f"Nilai awal {numb}")
def num(new):
    global numb # global hanya berlaku dalam fungsi
    numb = new
num(100)
print(f"Nilai baru {numb}")

#  contoh 4
# baca ah no 4 di buku. males ngetik aku
number = 0
for i in range(0, 5):
    number += i
    print(f"Number ke - {number}")
print(f"nilai baru {number}")


# contoh lainnya 
nam = 'dudung'
print(f"sebelum di ganti {nam}")
def pengganti(newname):
    global nam
    nam = newname
pengganti('ucup')
print(f"setelah di ganti {nam}")