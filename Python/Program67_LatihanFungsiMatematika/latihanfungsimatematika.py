# latihan matematika fungsi
# menghitung keliling dan luas persegi panjang
import math
import os
os.system("cls")
def inputUser():
    panjang = int(input("Masukkan panjang persegi panjang: "))
    lebar = int(input("Masukkan lebar persegi panjang: "))
    option = str(input("Apakah ingin keliling atau luas saja (k/l)? "))
    return panjang, lebar, option

def keliling(panjang, lebar):
    return 2 * (panjang + lebar)
def luas(panjang, lebar):
    return panjang * lebar

    
while True:
    panjang, lebar, option = inputUser()
    if option.lower() == 'k':
        k = keliling(panjang, lebar)
        print(f"Keliling persegi panjang: {k}")
    elif option.lower() == 'l':
        l = luas(panjang, lebar)
        print(f"Luas persegi panjang: {l}")
    end = str(input(f"Ingin lanjut? y/n: "))
    if end.lower() == 'n':
        print("Terima kasih telah menggunakan program ini.")
        break























