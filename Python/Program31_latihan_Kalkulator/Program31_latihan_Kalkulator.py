# kalkulator sederhana dengan if, elif, else

print(f"{'='*8} Kalkulator Sederhana {'='*8}")
userInput = float(input("Masukkan angka pertama: "))
userInput2 = float(input("Masukan angka ke dua: "))
operator = str(input("Masukkan operator (+, -, *, /, //, %, **): "))

if operator == "+":
    hasil = float(userInput + userInput2)
    desimal = int(hasil)
    desimal = int(hasil)
    print(f"Hasil dari {userInput} + {userInput2} = {hasil}")
    print(f"Hasil dalam desimal adalah {desimal}")
elif operator == "-":
    hasil = float(userInput - userInput2)
    desimal = int(hasil)
    print(f"Hasil dari {userInput} - {userInput2} = {hasil}")
    print(f"Hasil dalam desimal adalah {desimal}")
elif operator == "*" or operator == "x":
    # Menggunakan 'x' sebagai alternatif untuk '*'
    hasil = float(userInput * userInput2)
    desimal = int(hasil) 
    print(f"Hasil dari {userInput} * {userInput2} = {hasil}")
    print(f"Hasil dalam desimal adalah {desimal}")
elif operator == "/":
    hasil = float(userInput / userInput2)
    desimal = int(hasil) 
    print(f"Hasil dari {userInput} / {userInput2} = {hasil}")
    print(f"Hasil dalam desimal adalah {desimal}")
elif operator == "//":
    if userInput2 !=0:
        hasil = float(userInput // userInput2)
        desimal = int(hasil) 
        print(f"Hasil dari {userInput} // {userInput2} = {hasil}")
        print(f"Hasil dalam desimal adalah {desimal}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
elif operator == "%":
    if userInput2 != 0:
        hasil = float(userInput % userInput2)
        desimal = int(hasil) 
        print(f"Hasil dari {userInput} % {userInput2} = {hasil}")
        print(f"Hasil dalam desimal adalah {desimal}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
elif operator == "**":
    hasil = float(userInput ** userInput2)
    desimal = int(hasil) 
    print(f"Hasil dari {userInput} ** {userInput2} = {hasil}")
    print(f"Hasil dalam desimal adalah {desimal}")
else:
    print("Error: Operator tidak dikenali. Silakan gunakan salah satu dari +, -, *, /, //, %, **.")