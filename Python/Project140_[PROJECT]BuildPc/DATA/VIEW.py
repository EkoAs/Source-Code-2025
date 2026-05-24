
from .SYSTEM import SISTEM_USER as STM
from unittest import case
import os
sistem = os.name

class UserMenu:
    def __init__(self):
        pass
    
    def menu_User(self):
        print('='*20,"MENU AWAL",'='*20)
        print("1. Pilih Akun")
        print("2. Daftar Akun")
        print("3. Hapus Akun")
        
        print("\n",'='*30)
        menuAwal = input("Masukan Opsi: (1/2/3) ").lower()
        match menuAwal:
            case "1": self.pilih_Akun()
            case "2": print("Daftar Akun")
            case "3": print("Hapus Akun")
            case _: print("Opsi Tidak Ditemukan")
    
    
    # ====================================================================================
    def pilih_Akun(self):
        match sistem:
            case "nt": os.system("cls")
            case "posix": os.system("clear")
            
        print('='*20,"PILIH AKUN",'='*20)
        print("1. Buat Akun)")
       
        menuakun = input("Masukan Opsi: (1/2/3) ").lower()
        match menuakun:
            case "1": STM.buat_akun()
            case "2": print("Daftar Akun")
            case "3": print("Hapus Akun")
            case _: print("Opsi Tidak Ditemukan")
        