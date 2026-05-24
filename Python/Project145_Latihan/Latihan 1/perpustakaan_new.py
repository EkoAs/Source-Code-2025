import random 
import time
import os
import datetime

class PERPUS:
    def __init__(self,kode,nama,buku,tgl_p,tgl_k,denda):
        self.kode = kode
        self.nama = nama
        self.buku = buku
        self.tgl_p = tgl_p
        self.tgl_k = tgl_k
        self.denda = denda
        self.pusat_data = []
        
    def clear():
        sistem = os.name
        match sistem:
            case 'nt' : os.system("cls")
            case _: os.system('clear')
            
    def menu(self):
        PERPUS.clear()
        print(f"{'='*20} SELAMAT DATANG DIPERPUSTAKAAN {'='*20}")
        print(f"1. Pinjam Buku")
        print(f"2. Kembalikan Buku")
        print(f"3. Cek denda\n")
        print(f"4. Diskon denda\n")
        user = input("Masukan pilihan (1-3): ")
        if user == "1":
            print(f"Hello")
            PERPUS.pinjam(self)
        elif user == "3":
            PERPUS.denda(self)
        elif user == "4":
            PERPUS.diskon(self)
            
    def pinjam(self):
        PERPUS.clear()
        print(f"{'='*20} SELAMAT DATANG DIPERPUSTAKAAN {'='*20}")
        nama = input("masukan Nama: ")
        buku = input("Masukan judul Buku: ")
        tgl_p = input("Pinjam sekarang (y/n): ")
        if tgl_p != "n":
            today = datetime.date.today()
            self.tgl_p = int(today.strftime("%Y%m%d"))  # Format as YYYYMMDD integer
            print(f"Tanggal pinjam: {self.tgl_p}")
   
        kode = random.randint(1000,9999)
        self.kode = kode
        self.denda=20
        self.nama = nama
        data_dict = {
            "nama": self.nama,
            "buku": buku,
            "tgl_p": self.tgl_p if tgl_p != "n" else None,
            "id": self.kode,
            "denda": self.denda
        }
        self.pusat_data.append(data_dict)
        print("Data berhasil disimpan.")
        input("Tekan Enter untuk kembali ke menu...")
        
    
    def denda(self):
        denda_cek = 0
        for i in self.pusat_data:
            print(f"Nama : {i['nama']}")
            print(f"Buku : {i['buku']}")
            denda_cek += i['denda']
        print(f"denda anda {denda_cek}" )

    def diskon(self):
        sudah_diskon= 0
        for i in self.denda:
            sudah_diskon += i['denda']
        if (sudah_diskon <= 20):
            sudah_diskon /=2
        else:
            sudah_diskon /=2
        print(sudah_diskon)
            
    

if __name__ == '__main__':
    # Initialize the PERPUS instance with default values
    app = PERPUS(None, None, None, None, None, None)
    while True:
        app.menu() 
        kanjut = input("ingin lanjut? (y/n): ")
        if kanjut.lower() == "n":
            break

