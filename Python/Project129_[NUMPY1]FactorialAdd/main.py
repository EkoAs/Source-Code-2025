import DATA as DATA
import os
import sys
print(sys.executable)



if __name__ == "__main__":
    sistem = os.name  # deteksi sistem operasi
    match sistem:
        case "nt": os.system("cls")  # clear tampilan terminal (windows)

    def chose():
        print(f"{'='*10} Kalkulator {'='*10}")
        print('-'*34)
        print(f"1. kalkulator Biasa")
        print(f"2. kalkulator Geometry")
        print(f"3. kalkulator Matriks")
        print(f"4. kalkulator Faktorial")
        print(f"5. Masukan Dev")
        print('='*34)
        
        user = input("Masukan Opsi [1,2,3,4] : ")
        match user:
            case "1": 
                while(True):
                    match sistem:
                        case "nt": os.system("cls")
                    DATA.kalkulator_biasa()
                    isDone = input("Apakah ingin keluar dari rumus? (y/n) : ")
                    if isDone.lower() != 'n':
                        break
            case "2":
                while(True):
                    match sistem:
                        case "nt": os.system("cls")
                    DATA.kalkulator_Trinogo()
                    isDone = input("Apakah ingin keluar dari rumus? (y/n) : ")
                    if isDone.lower() != 'n':
                        break
            case "3": 
                while(True):
                    match sistem:
                        case "nt": os.system("cls")
                    DATA.matrix_Math()
                    isDone = input("Apakah ingin keluar dari rumus? (y/n) : ")
                    if isDone.lower() != 'n':
                        break
            case "4": 
                while(True):
                    match sistem:
                        case "nt": os.system("cls")
                    DATA.Factorial.factorialMath()
                    isDone = input("Apakah ingin keluar dari rumus? (y/n) : ")
                    if isDone.lower() != 'n':
                        break
            case "5": 
                try: 
                    with open("data.txt", "r", encoding='utf-8') as file:
                        content = file.read()
                        print(f"{content}")
                except:
                    print(f"Baca gagal")
            case _: print("Opsi tidak sesuai!")
            
    while(True):
        match sistem:
            case "nt": os.system("cls")  # clear tampilan terminal (windows)
        chose()
        done = input("apakah selesai(y/n): ") # lanjut atau selesai. kaloo lanjut kembali ke menu awal
        if done.lower() != 'n':
            match sistem:
                case "nt": os.system("cls")
                
            print(f"\n Terimakasih Sudah menggunkana program kami!")
            break
        