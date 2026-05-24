# break
number = int(input("Masukkan angka: "))
userInput = str(input("Masukkan nama anda: "))
# Program untuk mencetak "Hello World" sebanyak angka yang dimasukkan oleh pengguna
num = 0
while True:
    num += 1
    print(f"{userInput}")
    if num == number:
        break 
        print("Berhenti di angka 200")
        print(f"Tidak di cetak lagi")
print("Selesai")