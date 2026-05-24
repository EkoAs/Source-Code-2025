import numpy as np
import os 
import json
from .Sytem import SystemData as SD
sistem = os.name

class DataSaya:
    def __init__(self, nama="Anda", noRek="221122", pin="1234", saldo=0):
        self.nama = nama
        self.__noRek = noRek
        self._pin = pin
        self.saldo = saldo
    
    # untuk cek saldo/ambil nilai pakai
    def show_saldo(self):
        print(f"saldo {self.nama}: {self.saldo} ")
        
    # tambah saldo
    
    def add_saldo(self,jumlah):
        self.saldo += jumlah
        
        print(f"saldo {self.nama} berhasil ditambah sebesar {jumlah}")
        print(f"saldo {self.nama} sekarang: {self.saldo}")
    
    @property
    def noRek(self):
        return self.__noRek
    
    userData = []
    template = {
        "nama": "",
        "noRek": "",
        "pin": "",
        "saldo": 0
    }
    def showSaldo(self):
        while(True):
            match sistem:
                case "nt": os.system("cls")
            print("=========== Cek Saldo ============\n")
            
            show_saldo = DataSaya()
            show_saldo.show_saldo()
            print("\n","="*30)
            usersaldo = input("Ingin masukan saldo? (y/n) : ")
            if usersaldo.lower() == "y":
                while(True):
                    jumlah = input("Masukan nominal saldo :")
                    if jumlah.isdigit():
                        jumlah = float(jumlah)
                        try:
                            show_saldo.add_saldo(jumlah)
                            break
                        except:
                            print("Nominal harus angka!")
                    else:
                        print("Nominal harus angka!")
            print(f"\n saldo mu sekarang {show_saldo.saldo}")
            
           
            done = input("apakah selesai melihat saldo? (y/n): ")
            if done.lower() != 'n':
                break
    def createAkun(self):
        while(True):
            match sistem:
                case "nt": os.system("cls")
            print("=========== Buat Akun Baru ============\n")
            nama = SD.nama(self=None)
            noRek = SD.noRek(self=None)
            pin = SD.pin(self=None)
            saldo = SD.saldo(self=None)
            
            # Gunakan template untuk menyimpan data akun secara terstruktur
            user_dict = DataSaya.template.copy()
            user_dict["nama"] = nama
            user_dict["noRek"] = noRek
            user_dict["pin"] = pin
            user_dict["saldo"] = saldo

            
            with open("dataNasabah.txt", "a", encoding="utf-8") as file:
                file.write(json.dumps(user_dict) + "\n")
            newUser = DataSaya(nama, noRek, pin, saldo)
            DataSaya.userData.append(newUser)
            if len(DataSaya.userData) == 0:
                with open("dataNasabah.txt", "w", encoding="utf-8") as file:
                    file.write(f"{nama},{noRek},{pin},{saldo}\n")
            else: 
                with open("dataNasabah.txt", "a", encoding="utf-8") as file:
                    file.write(f"{nama},{noRek},{pin},{saldo}\n")
                DataSaya.userData.append(newUser)
            print(f"Akun baru berhasil dibuat untuk {nama} dengan no rekening {noRek}")
            print("\n","="*30)
            
            done = input("apakah selesai membuat akun? (y/n): ")
            if done.lower() != 'n':
                break
    
    def show_User(self):
        user = input("Masukan No Rekening: ")
        if user.isdigit() and len(user) == 6:
            try:
                with open("dataNasabah.txt", "r", encoding="utf-8") as file:
                    found = False
                    for line in file:
                        try:
                            data = json.loads(line.strip())
                        except json.JSONDecodeError:
                            continue
                        # Cari berdasarkan noRek
                        if data.get("noRek") == user:
                            print("Informasi Nasabah:")
                            for key, value in data.items():
                                print(f"{key.capitalize()}: {value}")
                            found = True
                            break
                    if not found:
                        print("No Rekening tidak ditemukan.")
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
    def transfer(self):
        # cara transfer ke rekening lain
        with open("dataNasabah.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            
    def add_saldo(self,jumlah):
        print("="*20, "Masukan No rekening tujuan", "="*20)
        while True:
            no = input("No Rekening: ")
            if no.isdigit() and len(no) == 6:
                break
            else:
                print("No rekening harus 6 digit angka!")
        while True:
            jumlah = input("Masukan nominal saldo: ")
            if jumlah.isdigit():
                jumlah = float(jumlah)
                break
            else:
                print("Nominal harus angka!")  
        
        # cari no rek yang dituju lalu tambah saldonya
        updated_lines = []
        found = False
        with open("dataNasabah.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        for line in lines:
            try:
                data = json.loads(line.strip())
            except json.JSONDecodeError:
                updated_lines.append(line)
                continue
            if data.get("noRek") == no:
                data["saldo"] += jumlah
                found = True
                print(f"Saldo berhasil ditransfer ke rekening {no}. Saldo baru: {data['saldo']}")
                updated_lines.append(json.dumps(data) + "\n")
            else:
                updated_lines.append(json.dumps(data) + "\n")
        if not found:
            print("No rekening tujuan tidak ditemukan.")
        else:
            with open("dataNasabah.txt", "w", encoding="utf-8") as file:
                file.writelines(updated_lines)
        # nilai = SD.tambah_saldo(jumlah)

    def transfer(self, jumlah, noRekTujuan):
        while True:
            match sistem:
                case "nt": os.system("cls")
            while True:
                print("="*30, "Masukan No Rekening mu", "="*30)
                noRekAsal = input("No Rekening Asal: ")
                if noRekAsal.isdigit() and len(noRekAsal) == 6:
                    break
                else:
                    print("No rekening harus 6 digit angka!")
            while True:
                print("="*30, "Masukan No rekening tujuan", "="*30)
                noRekTujuan = input("No Rekening Tujuan: ")
                if noRekTujuan.isdigit() and len(noRekTujuan) == 6:
                    break
                else:
                    print("No rekening harus 6 digit angka!")
            while True:
                jumlah = input("Masukan nominal saldo: ")
                if jumlah.isdigit():
                    jumlah = float(jumlah)
                    break
                else:
                    print("Nominal harus angka!")
                    
            match sistem:
                case "nt": os.system("cls")
            
            lines2 = []
            foundAsal = False
            foundTujuan = False
            with open("dataNasabah.txt","r", encoding="utf-8") as file:
                lines = file.readlines()
            for line in lines:
                try:
                    data = json.loads(line.strip())
                except json.JSONDecodeError:
                    lines2.append(line)
                    continue
                # nomor rekening asal
                if data.get("noRek") == noRekAsal:
                    if data["saldo"] >= jumlah:
                        data["saldo"] -= jumlah
                        foundAsal = True
                        print(f"\nSaldo berhasil ditarik dari rekening {noRekAsal}. Saldo baru: {data['saldo']}")
                    else:
                        print("Saldo tidak mencukupi untuk transfer.")
                    lines2.append(json.dumps(data) + "\n")
                # nomor rekening tujuan
                elif data.get("noRek") == noRekTujuan:
                    data["saldo"] += jumlah
                    foundTujuan = True
                    print(f"\nSaldo berhasil ditransfer ke rekening {noRekTujuan}. Saldo baru: {data['saldo']}")
                    lines2.append(json.dumps(data) + "\n")
                else:
                    lines2.append(json.dumps(data) + "\n")
            # tulid ulang data (updare)
            with open("dataNasabah.txt", "w", encoding="utf-8") as file:
                file.writelines(lines2)
            
            
            # info setelah update
            if foundAsal:
                print("="*30,"Informasi rekening asal","="*30)
                for line in lines2:
                    try:
                        data = json.loads(line.strip())
                        if data.get("noRek") == noRekAsal:
                            for key, value in data.items():
                                print(f"{key.capitalize()}: {value}")
                            print(f"Saldo anda berkurang {jumlah}\n")
                    except Exception:
                        continue
            if foundTujuan:
                print("="*30,"Informasi rekening tujuan","="*30)
                for line in lines2:
                    try:
                        data = json.loads(line.strip())
                        if data.get("noRek") == noRekTujuan:
                            for key, value in data.items():
                                print(f"{key.capitalize()}: {value}")
                            print(f"Saldo anda bertambah {jumlah}")
                    except Exception:
                        continue
            if not foundAsal or not foundTujuan:
                print("No rekening asal atau tujuan tidak ditemukan atau saldo tidak mencukupi.")
            isdone = input("\nApakah selesai transfer? (y/n): ")
            if isdone.lower() != 'n':
                break
            else:
                continue
    def delete_account(self):
        while True:
            match sistem:
                case "nt": os.system("cls")
            print("="*20, "Hapus Akun", "="*20)
            no = input("Masukan No Rekening yang ingin dihapus: ")
            if not (no.isdigit() and len(no) == 6):
                print("No rekening harus 6 digit angka!")
                continue

            found = False
            password_benar = False
            lines3 = []
            with open("dataNasabah.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()

            # Cari akun dengan no rek
            for line in lines:
                try:
                    data = json.loads(line.strip())
                except Exception:
                    lines3.append(line)
                    continue

                if data.get("noRek") == no:
                    found = True
                    userPassword = input("Masukan Password untuk konfirmasi: ")
                    if userPassword == data.get("pin"):
                        password_benar = True
                        print(f"Akun dengan no rekening {no} berhasil dihapus.")
                        # Tidak menambahkan akun ini ke lines3, sehingga terhapus
                        continue
                    else:
                        print("Password salah. Akun tidak dihapus.")
                        lines3.append(json.dumps(data) + "\n")
                else:
                    lines3.append(json.dumps(data) + "\n")

            if not found:
                print("No rekening tidak ditemukan.")
            elif found and not password_benar:
                print("Konfirmasi gagal. Akun tidak dihapus.")

            with open("dataNasabah.txt", "w", encoding="utf-8") as file:
                file.writelines(lines3)

            isdone = input("\nApakah selesai menghapus akun? (y/n): ")
            if isdone.lower() != 'n':
                break
