
import os as OS
sistem = OS.name

def clear():
    match sistem:
        case "cls": OS.system("cls")
        case _: OS.system("cls")
        
class SUPER:
    def __init__(object, nama, nim):
        object.nama = nama
        object.nim = nim
        
    def tampilkan(object):
        clear()
        print(f"Nama: {object.nama},\nNIm: {object.nim}\nNilai: {object.nilai}")
        
class SUB(SUPER):
    def __init__(object, nama, nim, nilai):
        super().__init__(nama, nim)
        object.nilai = nilai 
        if (object.nilai >= 90 ):
            object.nilai = str(object.nilai)
            object.nilai = " A"
        elif (object.nilai >= 80 ):
            object.nilai = str(object.nilai)
            object.nilai = " B"
        elif (object.nilai >= 70 ):
            object.nilai = str(object.nilai)
            object.nilai = " C"
        elif (object.nilai >= 60 ):
            object.nilai = str(object.nilai)
            object.nilai = " D"
        else:
            object.nilai = str(object.nilai)
            object.nilai = " E"
            
    def tampilkan(object):
        super().tampilkan()
        print(f"====================================")      

class BUKU:
    def __init__(object,judul,pengarang,tahun):
        object.judul = judul
        object.pengarang = pengarang
        object.tahun = tahun
    
    def tampilkan(object):
        clear()
        print(f"Judul: {object.judul},\nPengarang: {object.pengarang},\nTahun: {object.tahun}")
        

class KENDARAAN:
    def __init__(object, merk, tipe, tahun):
        object.merk = merk
        object.tipe = tipe
        object.tahun = tahun
        
    def info(object):
        clear()
        print(f"Merk: {object.merk},\nTipe: {object.tipe},\nTahun: {object.tahun}")
        
        
        
mobil ={
    'merk':"Toyota",
    'tipe':"Avanza T-100 Misille",
    'tahun':2020
}
buku ={
    'judul':"10 dosa besar jokowi",
    'pen': "Jokowi",
    'tahun': 2025
}
data = {
    'nama':"Eko",
    'nim':25143929,
    'nilai': 50
}

# obj = BUKU(buku['judul'], buku['pen'], buku['tahun'])
# obj.tampilkan()

# mbl=KENDARAAN(mobil['merk'], mobil['tipe'], mobil['tahun'])
# mbl.info()

maha=SUB(data['nama'], data['nim'], data['nilai'])
maha.tampilkan()