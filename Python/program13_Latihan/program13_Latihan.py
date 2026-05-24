# Operator Logika atau boolean
nilai_1 = int(input("Masukan Nilai 0 atau lainnya :"))
nilai_2 = int(input("Masukan Nilai Ke Dua :"))

nilai_bool1 = bool(nilai_1)
nilai_bool2 = bool(nilai_2)
hasil = nilai_bool1 or nilai_bool2
hasil_bool = bool(hasil)
hasil_int = int(hasil_bool)
print(nilai_bool1, 'or', nilai_bool2)
print('Hasil Boolean :', hasil_bool)
print('hasil int :', hasil_int)