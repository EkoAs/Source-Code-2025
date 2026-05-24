import math
import os

print(f"{'LATIHAN FUNGSI MATEMATIKA':^60}")
print(f"{'Operator: Keliling = k, Luas = l, Rasio = r, Volume = v, Diagonal = d  ':^60}")

def inputUs():
    panjang = int(input("Masukan panjang :"))
    lebar = int(input("Masukan lebar :"))
    tinggi = int(input("Masukan tinggi :"))
    operator = str(input("Masukan Operator :"))
    return panjang, lebar, tinggi, operator
def keliling(panjang, lebar):
    return 2 * (panjang + lebar)
def luas(panjang, lebar):
    return panjang * lebar
def rasio(panjang, lebar):
    return panjang / lebar if lebar != 0 else "Tidak bisa dibagi dengan nol"
def volume(panjang, lebar, tinggi):
    return panjang * lebar * tinggi
def diagonal(panjang, lebar):
    return math.sqrt(panjang**2 + lebar**2)


while True:
    panjang, lebar, tinggi, operator = inputUs()
    if operator.lower() == 'k':
        k = keliling(panjang, lebar)
        print(f"Keliling persegi panjang: {k}")
    elif operator.lower() == 'l':
        l = luas(panjang, lebar)
        print(f"Luas persegi panjang: {l}")
    elif operator.lower() == 'r':
        r = rasio(panjang, lebar)
        print(f"Rasio panjang dan lebar: {r}")
    elif operator.lower() == 'v':
        v = volume(panjang, lebar, tinggi)
        print(f"Volume persegi panjang: {v}")
    elif operator.lower() == 'd':
        d = diagonal(panjang, lebar)
        print(f"Diagonal persegi panjang: {d}")
    else:
        print("Operator tidak valid. Silakan coba lagi.")
    endProgram = str(input(f"Ingin lanjut?? (y/n):"))
    if endProgram.lower() == 'n':
        print("Terima kasih telah menggunakan program ini.")
        break
    
    
    
    
    
    
    
    
    
    