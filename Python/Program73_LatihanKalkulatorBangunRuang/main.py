# latihan fungsi kalkulator bangun ruang 
import math

def inputUser():
    panjang = int(input("Masukan Panjang"))
    lebar = int(input("Masukan lebar"))
    tinggi = int(input("Masukan tinggi"))
    diameter = input("Masukkan Diameter jika ada (ketik - jika tidak): ")
    diameter = float(diameter) if diameter != '-' else None
    operasi = str(input("masukan Operator :"))
    return panjang, lebar, tinggi, diameter, operasi
# Rumus Balok
volumeBalok = lambda panjang, lebar, tinggi:panjang*lebar*tinggi
kelilingBalok = lambda panjang, lebar:(panjang+lebar)*2
luasBalok = lambda panjang, lebar:panjang*lebar

while True:
    panjang, tinggi, lebar, diameter, operasi = inputUser()
    if operasi.lower() == 'vo':
        print(f"Volumenya => {volumeBalok(panjang, lebar, tinggi)}")
    elif operasi.lower() == 'ke':
        print(f"Kelilingnya => {kelilingBalok(panjang, lebar)}")
    elif operasi.lower() == 'lu':
        print(f"Kelilingnya => {luasBalok(panjang, lebar)}")
    
        
        
        
    endProgram = str(input(f"Ingin lanjut?? (y/n):"))
    if endProgram.lower() == 'n':
        print("Terima kasih telah menggunakan program ini.")
        break