# Args pada fungsi 
# def namaFungsi(*args) menggunakan satu bintang di depan

def fungsiBiasa(hello):
    print(hello )
fungsiBiasa("Ucup")

# fungsi dengan args 
# def fungsiargs(*args):
#     for num in args:
#         print(num)
#     return num
# data = fungsiargs(1, 2, 3, 4, 5, 6, 7, 8)
# print(data)

# contoh 2
def hello(*dataS):
    total = 0
    for angka in dataS:
        total += angka
    return total
dataHe = hello(5, 5, 5, 5)
print(dataHe)


# contoh 3 
def number(*hola):
    for i in hola:
        print(i)
    return hola
duarr = number("Mobil", 'pesawat', 'tank', 'ucup')
print(duarr)