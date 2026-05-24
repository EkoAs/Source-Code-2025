import os

class Factorial:
    def factorialMath():
        faktorial2 = lambda n : 1 if n == 0 or n == 1  else  n * faktorial2(n - 1)
        while True:
            
            print('='*60, "\n")
            angka = input("Masukkan bilangan bulat positif (atau -1 untuk keluar): ")
            if angka.isdigit() or angka.count(".") == 1:
                angka = float(angka)
                if angka < 0:
                    print("Silakan masukkan bilangan bulat positif.")
                else:
                    print(f"Faktorial dari {angka} adalah {faktorial2(angka)}\n")
            else: 
                print("Input Harus angka!")
                break
            if angka == -1:
                print("Terima kasih!")
                break
            