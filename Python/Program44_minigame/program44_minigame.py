# latihan membuat mini game tebak angka
import random
number = random.randint(1, 10)  # angka acak antara 1 sampai 10
print("Selamat datang di mini game tebak angka!")
userInput = int(input("Masukan angka :\t"))
if userInput == number:
    print(f"Selamat! kamu menebak {number} dengan benar")
else:
    print(f"Anda gagal")
    print(f" yang benar adalah {number}")