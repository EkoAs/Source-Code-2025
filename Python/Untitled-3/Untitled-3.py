
userInput = int(input("Masukan angka :\n"))
userInput2 = int(input("Masukan angka 2 :\n"))

hasil = userInput | userInput2
hasil2 = userInput & userInput2
print("Hasil OR adalah", hasil, format(hasil, '08b'))
print("Hasil AND adalah", hasil2, format(hasil2, '08b'))