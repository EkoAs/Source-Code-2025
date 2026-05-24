# latihan string 
userInput = str(input("Masukan Nama :\t"))
userInput2 = int(input("Masukan Usia :\t"))

print("Nama anda adalah :\t", userInput)
print("Usia anda adalah :\t", userInput2)

if userInput2 > 30:
    print("Selamat kamu")
elif userInput2 < 20:
    print("Anda masih muda")
elif userInput2 == 20:
    print("Anda sudah dewasa")
elif userInput2 == 30:
    print("Anda sudah tua")