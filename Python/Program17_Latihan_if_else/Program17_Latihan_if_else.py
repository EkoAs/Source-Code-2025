inputUser = int(float(input('Masukan Angka :\t')))
inputUser2 = int(float(input('Masukan Angka ke dua :\t')))
if inputUser > inputUser2:
    print('Angka Pertama lebih besar dari Angka kedua', inputUser, '>', inputUser2)
elif inputUser == inputUser2:
    print('Angka Pertama sama dengan Angka kedua', inputUser, '=', inputUser2)
elif inputUser < inputUser2:
    print('Angka Pertama lebih kecil dari Angka kedua', inputUser, '<', inputUser2)
elif inputUser is inputUser2:
    print('Angka Pertama sama dengan Angka kedua', inputUser, 'is', inputUser2)
else:
    print('Angka Pertama tidak sama dengan Angka kedua', inputUser, 'is not', inputUser2)
