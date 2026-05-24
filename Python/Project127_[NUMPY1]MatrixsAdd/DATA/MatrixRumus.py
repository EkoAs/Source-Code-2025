import numpy as np
class Matrixs:
    def matrix_pangkat_costum():
        opsi_ordo = input("Masukan Ordo Matrix (2x2, 3x3, 4x4, costum,): ")
        match opsi_ordo:
            case "2x2":
                print("Masukan input E.X (1234) => (12) Baris pertama. (34) Baris kedua ")
                a = input("Masukan input: ")
                pangkat = input("Masukan pangkat matrix: ")
                if len(a) == 4 and a.isdigit() and pangkat.isdigit():
                    data = [int(x) for x in a]          # Jadi [1, 1, 1, 1]
                    matriks2 = np.array(data).reshape(2, 2)  # Jadi [[1 1], [1 1]]
                    pangkat2 = int(pangkat)
                    print(f"Hasil = \n{matriks2**pangkat2}")
                else:
                    print("Input harus 4 digit untuk ordo 2x2")
            case "3x3":
                print("Masukan input E.X (123456789) => (123) Baris pertama. (456) Baris kedua. (789) Baris ketiga")
                a = input("Masukan input: ")
                pangkat = input("Masukan pangkat matrix: ")
                if len(a) == 9 and a.isdigit() and pangkat.isdigit():
                    data = [int(x) for x in a]          # Jadi [1, 1, 1, 1]
                    matriks3 = np.array(data).reshape(3, 3)  # Jadi [[1 1], [1 1]]
                    pangkat3 = int(pangkat)
                    print(f"Hasil = \n{matriks3**pangkat3}")
                else:
                    print("Input harus 9 digit untuk ordo 3x3")
            case "4x4":
                print("Masukan input E.X (123456789101112131415161718) => (1234) Baris pertama. (5678) Baris kedua. (91011) Baris ketiga. (12131415) Baris keempat")
                a = input("Masukan input: ")
                pangkat = input("Masukan pangkat matrix: ")
                if len(a) == 16 and a.isdigit() and pangkat.isdigit():
                    data = [int(x) for x in a]          # Jadi [1, 1, 1, 1]
                    matriks4 = np.array(data).reshape(4, 4)  # Jadi [[1 1], [1 1]]
                    pangkat4 = int(pangkat)
                    print(f"Hasil = \n{matriks4**pangkat4}")
                else:
                    print("Input harus 16 digit untuk ordo 4x4")
            case "costum":
                print("Masukan input E.X (2x3),(3x2),(4x2), dan lainnya. Maks kolom 4")
                rows = int(input("Masukan jumlah baris: "))
                cols = int(input("Masukan jumlah kolom: "))
                if cols > 4:
                    print("Maksimal kolom adalah 4")
                    return
                data = []
                for i in range(rows):
                    print("\n", "Masukan input ")
                    row = input(f"Masukan baris ke-{i+1}: ")
                    if len(row) != cols or not row.isdigit():
                        print("Input tidak valid")
                        return
                    data.append([int(x) for x in row])
                matriks = np.array(data)
                pangkat = int(input("Masukan pangkat matrix: "))
                print(f"Hasil = \n{matriks**pangkat}")
            case _:
                print("Ordo tidak dikenali! Pilih dari 2x2, 3x3, 4x4, atau costum")
                
    def matrix_operator():
        opsi_ordo = input("Masukan Ordo Matrix (2x2, 3x3, 4x4, costum,): ")
        opsi_ordo_B = input("Masukan Ordo Matrix B (2x2, 3x3, 4x4, costum,): ")
        match opsi_ordo:
            case "2x2":
                print("Masukan input E.X (1234) => (12) Baris pertama. (34) Baris kedua ")
                a = input("Masukan input: ")
                if len(a) == 4 and a.isdigit():
                    data = [int(x) for x in a]          # Jadi [1, 1, 1, 1]
                    matriksA = np.array(data).reshape(2, 2)  # Jadi [[1 1], [1 1]]
                    # return matriksA
                else:
                    print("Input harus 4 digit untuk ordo 2x2")
            case "3x3":
                print("Masukan input E.X (123456789) => (123) Baris pertama. (456) Baris kedua. (789) Baris ketiga")
                a = input("Masukan input: ")
                if len(a) == 9 and a.isdigit():
                    data = [int(x) for x in a]          # Jadi [1, 1, 1, 1]
                    matriksA = np.array(data).reshape(3, 3)  # Jadi [[1 1], [1 1]]
                else:
                    print("Input harus 9 digit untuk ordo 3x3")
            case "4x4":
                print("Masukan input E.X (123456789101112131415161718) => (1234) Baris pertama. (5678) Baris kedua. (91011) Baris ketiga. (12131415) Baris keempat")
                a = input("Masukan input: ")
                if len(a) == 16 and a.isdigit():
                    data = [int(x) for x in a]          # Jadi [1, 1, 1, 1]
                    matriksA = np.array(data).reshape(4, 4)  # Jadi [[1 1], [1 1]]
                else:
                    print("Input harus 16 digit untuk ordo 4x4")
            case "costum":
                print("Masukan input E.X (2x3),(3x2),(4x2), dan lainnya. Maks kolom 4")
                rows = int(input("Masukan jumlah baris: "))
                cols = int(input("Masukan jumlah kolom: "))
                if cols > 4:
                    print("Maksimal kolom adalah 4")
                    return
                data = []
                for i in range(rows):
                    print("\n", "Masukan input ")
                    row = input(f"Masukan baris ke-{i+1}: ")
                    if len(row) != cols or not row.isdigit():
                        print("Input tidak valid")
                        return
                    data.append([int(x) for x in row])
                matriksA = np.array(data)

            case _:
                print("Ordo tidak dikenali! Pilih dari 2x2, 3x3, 4x4, atau costum")
        match opsi_ordo_B:
            case "2x2":
                print("Masukan input E.X (1234) => (12) Baris pertama. (34) Baris kedua ")
                a = input("Masukan input: ")
                if len(a) == 4 and a.isdigit():
                    data = [int(x) for x in a]          # Jadi [1, 1, 1, 1]
                    matriksB = np.array(data).reshape(2, 2)  # Jadi [[1 1], [1 1]]
                    # return matriksB
                else:
                    print("Input harus 4 digit untuk ordo 2x2")
                    
            case "3x3":
                print("Masukan input E.X (123456789) => (123) Baris pertama. (456) Baris kedua. (789) Baris ketiga")
                a = input("Masukan input: ")
                if len(a) == 9 and a.isdigit():
                    data = [int(x) for x in a]          # Jadi [1, 1, 1, 1]
                    matriksB = np.array(data).reshape(3, 3)  # Jadi [[1 1], [1 1]]
                else:
                    print("Input harus 9 digit untuk ordo 3x3")
            case "4x4":
                print("Masukan input E.X (123456789101112131415161718) => (1234) Baris pertama. (5678) Baris kedua. (91011) Baris ketiga. (12131415) Baris keempat")
                a = input("Masukan input: ")
                if len(a) == 16 and a.isdigit():
                    data = [int(x) for x in a]          # Jadi [1, 1, 1, 1]
                    matriksB = np.array(data).reshape(4, 4)  # Jadi [[1 1], [1 1]]
                    
                else:
                    print("Input harus 16 digit untuk ordo 4x4")
            case "costum":
                print("Masukan input E.X (2x3),(3x2),(4x2), dan lainnya. Maks kolom 4")
                rows = int(input("Masukan jumlah baris: "))
                cols = int(input("Masukan jumlah kolom: "))
                if cols > 4:
                    print("Maksimal kolom adalah 4")
                    return
                data = []
                for i in range(rows):
                    print("\n", "Masukan input ")
                    row = input(f"Masukan baris ke-{i+1}: ")
                    if len(row) != cols or not row.isdigit():
                        print("Input tidak valid")
                        return
                    data.append([int(x) for x in row])
                matriksB = np.array(data)
                
            case _:
                print("Ordo tidak dikenali! Pilih dari 2x2, 3x3, 4x4, atau costum")
        
        operator = input("Masukan operator (+,-,*,/,//,%): ")
        match operator:
            case "+": 
                try:
                    result = np.add(matriksA, matriksB)
                    print(f"Hasil penjumlahan: {result}")
                except:
                    print("Ordo matriks tidak sesuai untuk penjumlahan")
            case "-":
                try:
                    result = np.subtract(matriksA, matriksB)
                    print(f"Hasil pengurangan: {result}")
                except:
                    print("Ordo matriks tidak sesuai untuk pengurangan")
            case "*":
                try:
                    result = np.multiply(matriksA, matriksB)
                    print(f"Hasil perkalian: {result}")
                except:
                    print("Ordo matriks tidak sesuai untuk perkalian")
            case "/":
                try:
                    result = np.divide(matriksA, matriksB)
                    print(f"Hasil pebagian : {result}")
                except:
                    print("Ordo matriks tidak sesuai untuk pembagian")
            case "%":
                try:
                    result = np.mod(matriksA, matriksB)
                    print(f"Hasil modulus : {result}")
                except:
                    print("Ordo matriks tidak sesuai untuk modulus")
            case "//":
                try:
                    result = np.floor_divide(matriksA, matriksB)
                    print(f"Hasil Floor Division : {result}")
                except:
                    print("Ordo matriks tidak sesuai untuk floor division")
            case _: print(f"Input tak sesuai!")
            
    def matrix_invers():
        opsi_ordo = input("Masukan Ordo Matrix (2x2, 3x3, 4x4, costum,): ")
        match opsi_ordo:
            case "2x2":
                a = input("Masukan 4 digit angka: ")
                if len(a) == 4 and a.isdigit():
                    # ubah jadi matriks 2x2
                    m = [[int(a[0]), int(a[1])],
                        [int(a[2]), int(a[3])]]

                    print("Matriks:")
                    for row in m:
                        print(row)

                    # hitung determinan
                    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
                    print("Determinan:", det)

                    if det != 0:
                        # hitung invers manual
                        invers = [[ m[1][1]/det, -m[0][1]/det],
                                [-m[1][0]/det,  m[0][0]/det]]

                        print("Invers Matriks:")
                        for row in invers:
                            print(row)
                    else:
                        print("Matriks tidak punya invers (determinan 0)")
                else:
                    print("Input harus 4 digit angka")
