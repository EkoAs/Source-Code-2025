import os
sistem = os.name
from .TEMPLATE import all_Template
import json
user_data = []
class SISTEM_USER:
    def buat_akun():
        userDict = all_Template()
        while True:
            match sistem:
                case "nt": os.system("cls")
            print('='*20,"BUAT AKUN BARU",'='*20)
            nama = input("Masukkan Nama: ")
            password = input("Masukan Password: ")
            computer = input("Masukan Nama PC: ")
            money = input("Ingin tambah uang? (y/n): ").lower()
            if money == 'y':
                uang1 = input("Masukan jumlah uang: ")
                if uang1.isdigit():
                    uang1 = float(uang1)
                else:
                    print("Input tidak valid. Jumlah uang diatur ke 0.")
                    uang1 = 0.0
            else:
                uang1 = 0.0
            userDict['uang'] += uang1
            userDict['name'] = nama
            userDict['password'] = password
            userDict['computer'] = computer
            with open("DATA_USER.txt", "a", encoding="utf-8") as file:
                file.write(json.dumps(userDict) + "\n")
            newUser = SISTEM_USER(nama, password, computer, uang1)
            SISTEM_USER.user_data.append(newUser)
            if len(SISTEM_USER.user_data) > 0:
                with open("DATA_USER.txt", "w", encoding="utf-8") as file:
                    file.write(f"{nama},{password},{computer},{uang1}\n")
            else:
                with open("dataNasabah.txt", "a", encoding="utf-8") as file:
                    file.write(f"{nama},{password},{computer},{uang1}\n")
                SISTEM_USER.user_data.append(newUser)
            print("\nAkun Berhasil Dibuat!\n\n")
            done = input("apakah selesai membuat akun? (y/n): ")
            if done.lower() != 'n':
                break