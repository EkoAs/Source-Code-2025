# def faktorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * faktorial(n - 1)
faktorial2 = lambda n : 1 if n == 0 or n == 1  else  n * faktorial2(n - 1)
while True:
    angka = int(input("Masukkan bilangan bulat positif (atau -1 untuk keluar): "))
    if angka == -1:
        print("Terima kasih!")
        break
    elif angka < 0:
        print("Silakan masukkan bilangan bulat positif.")
    else:
        print(f"Faktorial dari {angka} adalah {faktorial2(angka)}")
