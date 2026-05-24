# from ..PROGRES import Battle


class Option:
    def __init__():
        pass
    
    def opsi():
        print('='*50)
        print(f"1. Battle Mode")
        print(f"2. Story Mode")
        print(f"3. Daftar Hero")
        print(f"User pilih opsi : ")
        print("\n",'='*50)
        inputUser = input("Masukan Opsi (1,2,3,4): ")
        if inputUser.isdigit() and inputUser <= '4':
            inputUser = int(inputUser)
            match inputUser:
                case 1: print("Battle Mode")
                case 1: print("Battle Mode")
                case 1: print("Battle Mode")
                case 1: print("Battle Mode")
                case _: print("Battle Mode")
            
        else: 
            print(f"Input Bukan angka, silakan coba lagi!")
            return None
        