from numbers import Number
def inputUS():
    global num1
    num1 = input("Masukkan angka (contoh: 5!): ").strip()
    try:
        if len(num1) == 2:
            angka = int(num1[0])  # Mengambil karakter pertama dan mencoba konversi ke integer
            tanda = num1[1]
            if tanda == "!":
                def faktorial(n):
                    return 1 if n <= 1 else n * faktorial(n - 1)
                hasil = faktorial(angka)
                print(f"Hasil dari {angka}! adalah {hasil}")
            else:
                print("Tanda tidak valid! Gunakan '!' untuk faktorial.")
        else:
            print("Format salah! Masukkan dalam bentuk 'angka!' (contoh: 5!)")
        if len(num1) ==3:
            num = int(angka)
            
            tanda = num1[2]
            
            if tanda == "!":
                num.pop()
                angka = int(num)
                def faktorial(n):
                    return 1 if n <= 1 else n * faktorial(n - 1)
                hasil = faktorial(angka)
                print(f"Hasil dari {angka}! adalah {hasil}")
            else:
                print("Tanda tidak valid! Gunakan '!' untuk faktorial.")
        else:
            print("Format salah! Masukkan dalam bentuk 'angka!' (contoh: 5!)")
            
    except ValueError:
        print("Input pertama bukan angka! Masukkan digit angka (0-9).")
    except Exception as e:
        print(f"Terjadi error: {e}")

while(True):
    inputUS()
    if num1 == -0:
        break