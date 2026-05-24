# Simple calculator part 2

print(r"""
    Pilih 1 untuk penjumlahan.
    Pilih 2 untuk pengurangan.
    Pilih 3 untuk perkalian.
    Pilih 4 untuk pembagian.
    Pilih 5 untuk pangkat.
""")

# input dari user
inputUser = int(input("Masukan Angka pertama :\t"))
inputUser2 = int(input("Masukan Angka kedua :\t"))
inputUser3 = int(input("Masukan Pilihan :\t"))

if inputUser3 == 1:
    hasil = inputUser + inputUser2
    print("Hasil penjumlahan dari", inputUser, "+", inputUser2, "=", hasil)
elif inputUser3 == 2:
    hasil = inputUser - inputUser2
    print("Hasil pengurangan dari", inputUser, "-", inputUser2, "=", hasil)
elif inputUser3 == 3:
    hasil = inputUser * inputUser2
    print("Hasil perkalian dari", inputUser, "*", inputUser2, "=", hasil)
elif inputUser3 == 4:
    hasil = inputUser / inputUser2
    hasilModulus = inputUser % inputUser2
    print("Hasil pembagian dari", inputUser, "/", inputUser2, "=", hasil)
    print("Hasil modulus dari", inputUser, "%", inputUser2, "=", hasilModulus)