inputUser = str(input("Typing Here :\t"))
inputUser2 = str(input("Typing Here :\t"))
program = len(inputUser) + len(inputUser2)
programFor = f"{inputUser} {inputUser2}"
print(f"{program}")
print(f"{programFor:}")
if program > 10:
    print(f"Jumlah karakter dari {inputUser} dan {inputUser2} adalah {program}, lebih dari 10 karakter")
    hasil = int(program)
    print(f"{hasil} ==>> {format(hasil, '08b')}")
    jumlah_1 = bin(hasil).count('1') # mengkonversi hasil ke biner dan menghitung jumlah angka satu
    jumlah_2 = f"{jumlah_1 ** 2}" # menghitung kuadrat dari jumlah angka satu
    print(f"jumlah angka satu dalam bit adalah. {jumlah_1} dengan hasil {jumlah_2}")
elif program < 10:
    print(f"Jumlah karakter dari {inputUser} dan {inputUser2} adalah {program}, kurang dari 10 karakter")
    hasil = int(program)
elif program == 10:
    print(f"Jumlah karakter dari {inputUser} dan {inputUser2} adalah {program}, Sama jumlahnya")
else:
    print(f"Program tidak valid")