# from Python.Project135_HowTo.DATA import user
from .User.dataUser import DataSaya

def showMenu():
    print(f"===== ATM Menu =====")
    print(f"1. Buat Akun Baru")
    print(f"2. Informasi Akun")
    print(f"3. Cek Saldo")
    print(f"4. Add Saldo")
    print(f"5. Transfer")
    print(f"6. Hapus Akun")
    
    print("\n","="*30)
    userOption = input("Masukan Opsi : ")
    match userOption:
        case "1": DataSaya.createAkun(self=None)
        case "2": DataSaya.show_User(self=None)
        case "3": DataSaya.showSaldo(self=None)
        case "4": DataSaya.add_saldo(self=None, jumlah=0)
        case "5": DataSaya.transfer(self=None, jumlah=0, noRekTujuan="")
        case "6": DataSaya.delete_account(self=None)
        case _: print("Opsi Tidak Ditemukan")
        
        
    
    