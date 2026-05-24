import math
import os
print(f"{'='*100}")
print(f"{'LATIHAN FUNGSI MATEMATIKA':^100}")
print(f"{'Operator: Keliling = k, Luas = l, Rasio = r, Volume = v, Diagonal = d, parimeter = p ':<100}")
print(f"{'Operator: Keliling Segitiga = ks, Luas Segitiga = ls':<100}")
print(f"{'='*100}")

typeOperator = str(input("Masukan tipe operator (biasa/lanjutan):"))

if typeOperator.lower() == 'lanjutan':
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
    def parameter(panjang):
        return 4 * panjang
    def kelilingSegitiga(panjang):
        return panjang ** 3
    def luasSegitiga(panjang, lebar):
        return (panjang * lebar) / 2

    while True:
        panjang, lebar, tinggi, operator = inputUs()
        if operator.lower() == 'k':
            ke = keliling(panjang, lebar)
            print(f"Keliling persegi panjang: {ke}")
        elif operator.lower() == 'l':
            lu = luas(panjang, lebar)
            print(f"Luas persegi panjang: {lu}")
        elif operator.lower() == 'r':
            ra = rasio(panjang, lebar)
            print(f"Rasio panjang dan lebar: {ra}")
        elif operator.lower() == 'v':
            vo = volume(panjang, lebar, tinggi)
            print(f"Volume persegi panjang: {vo}")
        elif operator.lower() == 'd':
            di = diagonal(panjang, lebar)
            print(f"Diagonal persegi panjang: {di}")
        elif operator.lower() == 'p':
            pa = parameter(panjang)
            print(f"Parameter persegi: {pa}")
        elif operator.lower() == 'ks':
            ks = kelilingSegitiga(panjang)
            print(f"Keliling segitiga: {ks}")
        elif operator.lower() == 'ls':
            ls = luasSegitiga(panjang, lebar)
            print(f"Luas segitiga: {ls}")
        else:
            print("Operator tidak valid. Silakan coba lagi.")
        endProgram = str(input(f"Ingin lanjut?? (y/n):"))
        if endProgram.lower() == 'n':
            print("Terima kasih telah menggunakan program ini.")
            break
elif typeOperator.lower() == 'biasa':
    pass
    def inputUs2():
        inputuser2 = int(input("Masukan Angka Pertama :"))
        inputuser3 = int(input("Masukan Angka Kedua :"))
        operator1 = input("Masukan Operator +,-,x,/,**,% :")
        return inputuser2, inputuser3, operator1
    def tambah(num1, num2):
        return num1 + num2
    def kurang(num1, num2):
        return num1 - num2
    def kali(num1, num2):
        return num1 * num2
    def bagi(num1, num2):
        return num1 / num2
    def pangkat(num1, num2):
        return num1 ** num2
    def modulus(num1, num2):
        return num1 % num2
    
    while True:
        num1, num2, operator1 = inputUs2()
        if operator1.lower() == "+":
            t = tambah(num1, num2)
            print(f"Hasil = {t}")
        elif operator1.lower() == "-":
            k = kurang(num1, num2)
            print(f"Hasil = {k}")
        elif operator1.lower() == "x" or operator1.lower() == "*":
            z = kali(num1, num2)
            print(f"Hasil = {z}")
        elif operator1.lower() == "/":
            b = bagi(num1, num2)
            print(f"Hasil = {b}")
        elif operator1.lower() == "**" or "xx":
            p = pangkat(num1, num2)
            print(f"Hasil = {p}")
        elif operator1.lower() == "%":
            m = tambah(num1, num2)
            print(f"Hasil = {m}")
        else:
            print(f"Operator Tidak Valid :")
        endProgram = str(input(f"Ingin lanjut?? (y/n):"))
        if endProgram.lower() == 'n':
            print("Terima kasih telah menggunakan program ini.")
            break
    
else: 
    print("Operator Tidak Valid")
print("Program Berakhir")  
    
    
    