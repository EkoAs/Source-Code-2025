inputUser = int(input("Masukan Angka 1 sampai 9: \t"))
if inputUser == 2:
    print(f"Selamat kamu memilih angka {inputUser}")
    bit = format(inputUser, '08b')
    # buat kode agar bit dari user bisa di hitung 0 nya atau 1 nya
    #
    jumlah = bit.count("0")
    print(f"Anda berada di peringkat {jumlah}%")
elif inputUser == 3:
    pass
    
print(f"You Won!!!")
    



    