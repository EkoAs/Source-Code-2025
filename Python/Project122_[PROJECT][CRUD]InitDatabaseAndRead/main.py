import os
import CRUD as CRUD




if __name__ == "__main__": # supaya running biar lebih rapih
    sistem = os.name # lalu deteksi didtem operasi
    match sistem: # case itu cek. bisa beberapa opsi case juga, cocoknya ke yang mana
        case "nt": os.system("cls") #clear tampilna terminal (windows)
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN ")
    print("=========================")
    
    # cek databaseadau tidak
    CRUD.init_console()
    
    while(True):
        match sistem: # case itu cek. bisa beberapa opsi case juga, cocoknya ke yang mana
            case "nt": os.system("cls") #clear tampilna terminal (windows)
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN ")
        print("=========================")
    
        print(f"1. read data")
        print(f"2. Create data")
        print(f"3. Update Date")
        print(f"4. Delete Data\n")
        
        userOption = input("Masukan Opsi :")
        print("\n===================================\n")
        
        match userOption:
            case "1": CRUD.read_console()
            case "2": print("Create data")
            case "3": print("Update data")
            case "4": print("Delete data")
            
        print("\n===================================\n")
        done = input("apakah selesai(y/n): ") # lanjut atau selesai. kaloo lanjut kembali ke menu awal
        if done.lower() != 'n':
            break
        
    print("Perogram Berakhir")