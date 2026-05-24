import os
import DATA as DATA

if __name__ == "__main__":
    sistem = os.name 
    match sistem:
        case "nt": os.system("cls")
        case _: os.system("clear")
        
    while(True):
        match sistem:
            case "nt": os.system("cls")
            case _: os.system("clear")
        print("\n")
        print(f"{'='*30}")
        print(f"SELAMAT DATANG DI MESIN ATM!")
        print(f"{'='*30}")
        
        DATA.showMenu()
        

        # DATA.showView()
        # print("Uji coba tahap satu")
        
        done = input("\napakah selesai?/Ingin keluar? (y/n): ")
        if done.lower() != 'n':
            match sistem:
                case "nt": os.system("cls")
            print(f"\n Terimakasih sudah menggunakan perogram kami ^^\n")
            break
