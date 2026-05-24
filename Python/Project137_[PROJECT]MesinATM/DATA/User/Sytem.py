

class SystemData:
    def __init__(self):
        pass

    def noRek(self):
        while True:
            noRek = input("Masukan Nomor Rekening (6 digit): ")
            if noRek.isdigit() and len(noRek) == 6:
                return noRek
            else:
                print("Nomor rekening harus 6 digit angka.")
                
    def nama(self):
        while True:
            nama = input("Masukan Nama (Min 3 karakter): ")
            if len(nama) >= 3 and nama.isalpha():
                return nama
            else:
                print("Nama harus terdiri dari minimal 3 karakter dan hanya berisi huruf.")
    
    def pin(self):
        while True:
            pin = input("Masukan PIN (4 digit): ")
            if pin.isdigit() and len(pin) == 4:
                return pin
            else:
                print("PIN harus 4 digit angka.")
                
    def saldo(self):
        print("Ingin Masukan Saldo Awal?: ")
        user = input("(y/n): ")
        if user.lower() == "y" and user.isalpha():
            while True:
                saldo = input("Masukan Nominal Saldo : ")
                if saldo.isdigit():
                    return float(saldo)
                else:
                    print("Nominal harus angka!")
        else:
            print("Saldo harus digit!")
            return 0.0
        
    def tambah_saldo(self,jumlah):
        # cari no rek yang dituju lalu tambah saldonya
        pass
