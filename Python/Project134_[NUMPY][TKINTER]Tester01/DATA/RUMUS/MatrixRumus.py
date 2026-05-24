import numpy as np
import os
sistem = os.name
class Matrixs:
    matriksA = None
    matrix=ksB = None
    def matrix_pangkat_costum():
        match sistem:
            case "nt": os.system("cls")
        print('='*80)
        opsi_ordo = input("Masukan Ordo Matrix (2x2, 3x3, 4x4, costum,): ")
        match opsi_ordo:
            case "2x2":
                try:
                    print('='*80)
                    print("Masukan input E.X (1234) => (12) Baris pertama. (34) Baris kedua ")
                    a = input("Masukan input: ")
                    pangkat = input("Masukan pangkat matrix: ")
                    # if len(a) == 4 and a.isdigit() and pangkat.isdigit():
                    data = [int(x) for x in a]          # Jadi [1, 1, 1, 1]
                    matriks2 = np.array(data).reshape(2, 2)  # Jadi [[1 1], [1 1]]
                    pangkat2 = int(pangkat)
                    print(f"Hasil = \n{matriks2**pangkat2}")
                        
                except:
                    match sistem:
                        case "nt": os.system("cls")
                    print("\nOps. Sepertinya Input Puluhan/Ratusan, Coba yang ini:")
                    print('='*80)
                    print("Masukan input E.X (12 34 56 78) => (12 34) Baris pertama. (56 78) Baris kedua ")
                    a = input("Masukan input untuk Matriks A (pisahkan dengan spasi): ")
                    pangkat = input("Masukan Pangkat: ")
                    if pangkat.isdigit():
                        pangkat = int(pangkat)
                        try:
                            data_str = a.split()
                            if len(data_str) == 4 and all(s.isdigit() for s in data_str):
                                data = [int(x) for x in data_str]
                                matriksA = np.array(data).reshape(2, 2)
                                print(f"Hasil pangkat adalah:\n {matriksA**pangkat}")
                            else:
                                print("Input Matriks A tidak valid. Pastikan ada 4 angka yang dipisahkan spasi.")
                        except ValueError:
                            print("Kesalahan input Matriks A. Pastikan semua elemen adalah angka.")
                    else:
                        print(f"Ops. Sepertinya pangkat bukan angka!")



            case "3x3":
                try:
                    print('='*80)
                    print("Masukan input E.X (123456789) => (123) Baris pertama. (456) Baris kedua. (789) Baris ketiga")
                    a = input("Masukan input: ")
                    pangkat = input("Masukan pangkat matrix: ")
                    data = [int(x) for x in a]          # Jadi [1, 1, 1, 1]
                    matriks3 = np.array(data).reshape(3, 3)  # Jadi [[1 1], [1 1]]
                    pangkat3 = int(pangkat)
                    print(f"Hasil = \n{matriks3**pangkat3}")
                except:
                    match sistem:
                        case "nt": os.system("cls")
                    print("\nOps. Sepertinya Input Puluhan/Ratusan, Coba yang ini:")
                    print('='*100)
                    print("Masukan input E.X (12 34 56 78 22 12 10 20 23)")
                    print("=> (12 34 56) Baris pertama. (78 22 12) Baris kedua. (10 20 23) Baris ketiga.")
                    a = input("Masukan input untuk Matriks A (pisahkan dengan spasi): ")
                    pangkat = input("Masukan Pangkat: ")
                    if pangkat.isdigit():
                        pangkat = int(pangkat)
                        try:
                            data_str = a.split()
                            if len(data_str) == 9 and all(s.isdigit() for s in data_str):
                                data = [int(x) for x in data_str]
                                matriksA = np.array(data).reshape(3, 3)
                                print(f"Hasil pangkat adalah:\n {matriksA**pangkat}")
                            else:
                                print("Input Matriks A tidak valid. Pastikan ada 9 angka yang dipisahkan spasi.")
                        except ValueError:
                            print("Kesalahan input Matriks A. Pastikan semua elemen adalah angka.")
                    else:
                        print(f"Ops. Sepertinya pangkat bukan angka!")
                    
                    
            case "4x4":
                try:
                    print("Masukan input E.X (123456789101112131415161718)")
                    print("=> (1234) Baris pertama. (5678) Baris kedua. (91011) Baris ketiga. (12131415) Baris keempat")
                    a = input("Masukan input: ")
                    pangkat = input("Masukan pangkat matrix: ")
                    data = [int(x) for x in a]          # Jadi [1, 1, 1, 1]
                    matriks4 = np.array(data).reshape(4, 4)  # Jadi [[1 1], [1 1]]
                    pangkat4 = int(pangkat)
                    print(f"Hasil = \n{matriks4**pangkat4}")
                except:
                    match sistem:
                        case "nt": os.system("cls")
                    print("\nOps. Sepertinya Input Puluhan/Ratusan, Coba yang ini:")
                    print('='*100)
                    print("Masukan input E.X (12 34 56 78 22 12 10 20 23 10 20 30 40 55 60 100).")
                    print("=> (12 34 56 78) Baris pertama. (22 12 10 20) Baris kedua.")
                    print("=> (23 10 20 30) Baris ketiga. (40 55 60 100)  Baris ke empat.")
                    a = input("Masukan input untuk Matriks A (16 Angkap per spasi) (pisahkan dengan spasi)\n\t: ")
                    pangkat = input("Masukan Pangkat: ")
                    if pangkat.isdigit():
                        pangkat = int(pangkat)
                        try:
                            data_str = a.split()
                            if len(data_str) == 16 and all(s.isdigit() for s in data_str):
                                data = [int(x) for x in data_str]
                                matriksA = np.array(data).reshape(4, 4)
                                print(f"Hasil pangkat adalah:\n {matriksA**pangkat}")
                            else:
                                print("Input Matriks A tidak valid. Pastikan ada 16 angka yang dipisahkan spasi.")
                        except ValueError:
                            print("Kesalahan input Matriks A. Pastikan semua elemen adalah angka.")
                    else:
                        print(f"Ops. Sepertinya pangkat bukan angka!")
                        
                    
                    
            case "costum":
                print("Masukan input E.X (2x3),(3x2),(4x2), dan lainnya. Maks kolom 4")
                try:
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
                except:
                    print(f"Kesalahan data, input, ordo")
            case _:
                print("Ordo tidak dikenali! Pilih dari 2x2, 3x3, 4x4, atau costum")
                
    def matrix_operator():
        opsi_ordo = input("Masukan Ordo Matrix (2x2, 3x3, 4x4, costum,): ")
        opsi_ordo_B = input("Masukan Ordo Matrix B (2x2, 3x3, 4x4, costum,): ")
        match opsi_ordo:
            case "2x2":
                match sistem:
                    case "nt": os.system("cls")
                print('='*80)
                print("Masukan input E.X (12 34 56 78) => (12 34) Baris pertama. (56 78) Baris kedua ")
                a = input("Masukan input untuk Matriks A (pisahkan dengan spasi): ")
                try:
                    data_str = a.split()
                    if len(data_str) == 4 and all(s.isdigit() for s in data_str):
                        data = [int(x) for x in data_str]
                        matriksA = np.array(data).reshape(2, 2)
                                
                    else:
                        print("Input Matriks A tidak valid. Pastikan ada 4 angka yang dipisahkan spasi.")
                except ValueError:
                    print("Kesalahan input Matriks A. Pastikan semua elemen adalah angka.")
                

            case "3x3":
                print("Masukan input E.X (12 34 56 78 11 22 33 44 55)")
                print("=> (12 34 56) Baris pertama. (78 11 22) Baris kedua. Baris ketiga (33 44 55)")
                a = input("Masukan input untuk Matriks A (pisahkan dengan spasi): ")
                try:
                    data_str = a.split()
                    if len(data_str) == 9 and all(s.isdigit() for s in data_str):
                        data = [int(x) for x in data_str]
                        matriksA = np.array(data).reshape(3, 3)      
                    else:
                        print("Input Matriks A tidak valid. Pastikan ada 9 angka yang dipisahkan spasi.")
                except ValueError:
                    print("Kesalahan input Matriks A. Pastikan semua elemen adalah angka.")



            case "4x4":
                print('='*100)
                print("Masukan input E.X (12 34 56 78 22 12 10 20 23 10 20 30 40 55 60 100).")
                print("=> (12 34 56 78) Baris pertama. (22 12 10 20) Baris kedua.")
                print("=> (23 10 20 30) Baris ketiga. (40 55 60 100)  Baris ke empat.")
                a = input("Masukan input untuk Matriks B (16 Angkap per spasi) (pisahkan dengan spasi)\n\t: ")
                try:
                    data_str = a.split()
                    if len(data_str) == 16 and all(s.isdigit() for s in data_str):
                        data = [int(x) for x in data_str]
                        matriksB = np.array(data).reshape(4, 4)          
                    else:
                        print("Input Matriks B tidak valid. Pastikan ada 16 angka yang dipisahkan spasi.")
                except ValueError:
                    print("Kesalahan input Matriks B. Pastikan semua elemen adalah angka.")
                    
                    
            case "costum":
                print("Masukan input E.X (2x3),(3x2),(4x2), dan lainnya. Maks kolom 4")
                try:
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
                except:
                    print("Kesalahan data, input, ordo")
            case _:
                print("Ordo tidak dikenali! Pilih dari 2x2, 3x3, 4x4, atau costum")
                
                
                
        match opsi_ordo_B:
            case "2x2":
                print("Masukan input E.X (12 34 56 78) => (12 34) Baris pertama. (56 78) Baris kedua ")
                a = input("Masukan input untuk Matriks B (pisahkan dengan spasi): ")
                try:
                    data_str = a.split()
                    if len(data_str) == 4 and all(s.isdigit() for s in data_str):
                        data = [int(x) for x in data_str]
                        matriksB = np.array(data).reshape(2, 2)          
                    else:
                        print("Input Matriks B tidak valid. Pastikan ada 4 angka yang dipisahkan spasi.")
                except ValueError:
                    print("Kesalahan input Matriks B. Pastikan semua elemen adalah angka.")
                    
                    
            case "3x3":
                print("Masukan input E.X (12 34 56 78 11 22 33 44 55)")
                print("=> (12 34 56) Baris pertama. (78 11 22) Baris kedua. Baris ketiga (33 44 55)")
                a = input("Masukan input untuk Matriks B (pisahkan dengan spasi): ")
                try:
                    data_str = a.split()
                    if len(data_str) == 9 and all(s.isdigit() for s in data_str):
                        data = [int(x) for x in data_str]
                        matriksB = np.array(data).reshape(3, 3)          
                    else:
                        print("Input Matriks B tidak valid. Pastikan ada 9 angka yang dipisahkan spasi.")
                except ValueError:
                    print("Kesalahan input Matriks A. Pastikan semua elemen adalah angka.")
                    
                          
            case "4x4":
                print("Masukan input E.X (12 34 56 78 22 12 10 20 23 10 20 30 40 55 60 100).")
                print("=> (12 34 56 78) Baris pertama. (22 12 10 20) Baris kedua.")
                print("=> (23 10 20 30) Baris ketiga. (40 55 60 100)  Baris ke empat.")
                a = input("Masukan input untuk Matriks B (16 Angkap per spasi) (pisahkan dengan spasi)\n\t: ")
                try:
                    data_str = a.split()
                    if len(data_str) == 16 and all(s.isdigit() for s in data_str):
                        data = [int(x) for x in data_str]
                        matriksB = np.array(data).reshape(4, 4)          
                    else:
                        print("Input Matriks B tidak valid. Pastikan ada 16 angka yang dipisahkan spasi.")
                except ValueError:
                    print("Kesalahan input Matriks B. Pastikan semua elemen adalah angka.")
                    
                    
                    
                    
            case "costum":
                print("Masukan input E.X (2x3),(3x2),(4x2), dan lainnya. Maks kolom 4")
                try:  
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
                except:
                    print(f"Ordo tidak sesuai!")
            case _:
                print("Ordo tidak dikenali! Pilih dari 2x2, 3x3, 4x4, atau costum")
                
                
        # ============================OPERASI PENJUMLAHAN MATRIKS==================================
        operator = input("Masukan operator (+,-,*,/,//,%): ")
        match operator:
            case "+": 
                try:
                    print('='*80)
                    print(f"Matriks A:\n{matriksA}\n")
                    print(f"Matriks B:\n{matriksB}\n")
                    result = np.add(matriksA, matriksB)
                    print(f"Hasil penjumlahan:\n{result}")
                except:
                    print("Ordo matriks tidak sesuai untuk penjumlahan")
            case "-":
                try:
                    print('='*80)
                    print(f"Matriks A:\n{matriksA}\n")
                    print(f"Matriks B:\n{matriksB}\n")
                    result = np.subtract(matriksA, matriksB)
                    print(f"Hasil pengurangan:\n{result}")
                except:
                    print("Ordo matriks tidak sesuai untuk pengurangan")
            case "*":
                try:
                    print('='*80)
                    print(f"Matriks A:\n{matriksA}\n")
                    print(f"Matriks B:\n{matriksB}\n")
                    result = np.multiply(matriksA, matriksB)
                    print(f"Hasil perkalian:\n{result}")
                except:
                    print("Ordo matriks tidak sesuai untuk perkalian")
            case "/":
                try:
                    print('='*80)
                    print(f"Matriks A:\n{matriksA}\n")
                    print(f"Matriks B:\n{matriksB}\n")
                    result = np.divide(matriksA, matriksB)
                    print(f"Hasil pebagian :\n{result}")
                except:
                    print("Ordo matriks tidak sesuai untuk pembagian")
            case "%":
                try:
                    print('='*80)
                    print(f"Matriks A:\n{matriksA}\n")
                    print(f"Matriks B:\n{matriksB}\n")
                    result = np.mod(matriksA, matriksB)
                    print(f"Hasil modulus :\n{result}")
                except:
                    print("Ordo matriks tidak sesuai untuk modulus")
            case "//":
                try:
                    print('='*80)
                    print(f"Matriks A:\n{matriksA}\n")
                    print(f"Matriks B:\n{matriksB}\n")
                    result = np.floor_divide(matriksA, matriksB)
                    print(f"Hasil Floor Division :\n{result}")
                except:
                    print("Ordo matriks tidak sesuai untuk floor division")
            case _: print(f"Input tak sesuai!")


# from ..User import dataNew

class MatrixInvers:    
    def __init__(self):
        pass
    
    
    def matrix_invers():
        opsi_ordo = input("Masukan Ordo Matrix (2x2, 3x3, 4x4, costum): ")
        match opsi_ordo:
            case "2x2":
                try:
                    a = input("Masukan 4 digit angka (1234) => baris ke 1 (12), baris ke 2 (34): ")
                    if len(a) == 4 and a.isdigit():
                        # ubah jadi matriks 2x2
                        m = [[int(a[0]), int(a[1])],
                            [int(a[2]), int(a[3])]]
                        print("Matriks:")
                        for row in m:
                            print(row)

                        det = m[0][0] * m[1][1] - m[0][1] * m[1][0] # hitung determinan
                        print("Determinan:", det, "\n")

                        if det != 0:
                            # hitung invers manual
                            invers = [[ m[1][1]/det, -m[0][1]/det],
                                    [-m[1][0]/det,  m[0][0]/det]]

                            print("Invers Matriks:")
                            for row in invers:
                                print(row)
                        else:
                            print(f"Matriks tidak punya invers (determinan 0)")
                    else:
                        print("Input harus 4 digit angka")
                except:
                    print(f"Kesalahan sistm, go back again!")
                    return False
                        
            case "3x3":
                print(f"Logikanya dimana pake invers di ordo 3x3")
                print(f"Coming Son!")
                userScret = input("Masukan untuk Dev : ")
                try: 
                    from ..User  import dataNew 
                    with open("data.txt", 'a', encoding='utf-8') as file:
                        file.write(userScret)
                except:
                    print(f"Membuat data baru.")
                    dataNew()
            case "4x4":
                print(f"Apalagi ini")
                
                
                
class MatrixsTranspose:
    def __init__(self):
        pass
    
    def matrix_transpose():
        match sistem:
            case "nt": os.system("cls")
        print('='*80)
        print("1. 2x2 To 2x2")
        print("2. 2x3 To 3x2")
        print("3. 3x2 To 2x3")
        print("4. 3x3 To 3x3")
        print("5. 3x4 To 4x3")
        print("6. 4x3 To 3x4")
        print("7. Costum")
        user_Opsi = input("Masukan Opsi [1,2,3,4,5,6,7] : ")
        match user_Opsi:
            case "1":
                match sistem:
                    case "nt": os.system("cls")
                print('='*80)
                print("Masukan input E.X (12 34 56 78) => (12 34) Baris pertama. (56 78) Baris kedua ")
                a = input("Masukan input untuk Matriks (pisahkan dengan spasi): ").split()
                if len(a) == 4 and all(i.isdigit() for i in a):
                    a = list(map(int, a))
                    # a = int(a)
                    try:
                        matriks = np.array(a).reshape(2,2)
                        print(f"Matrik Awal :\n{matriks}\n")
                        matriks[0,1], matriks[1,0] = matriks[1,0], matriks[0,1]
                        print(f"Hasil Transpose:\n{matriks}\n")
                    except:
                        print(f"Kesalahan Data")
                        return False
                else:
                    print(f"Input bukan angka!")
                    return False   
            case "2":
                match sistem:
                    case "nt": os.system("cls")
                print('='*80)
                print(f"(2 = baris, 3 = kolom). 2x3 => 3x2")
                print(f"Masukan Input (1 2 3 4 5 6) => (1 2 3) Baris pertama. (4 5 6) Baris Kedua")
                a = input("Masukan input untuk Matriks (pisahkan dengan spasi): ").split()
                if len(a) == 6 and all(i.isdigit() for i in a):
                    a = list(map(int,a))
                    try:
                        matriks = np.array(a).reshape(2,3)
                        print(f"Matrik Awal :\n{matriks}\n")
                        matriks = matriks.T # T adalah Transpose
                        print(f"Matrik Awal :\n{matriks}\n")
                    except:
                        print(f"Kesalahan Data")
                        return False
                else:
                    print(f"Input bukan angka!")
                    return False
            case "3":
                match sistem:
                    case "nt": os.system("cls")
                print('='*100)
                print(f"(3 = baris, 2 = kolom). 3x2 => 2x3")
                print("Masukan Input (1 2 3 4 5 6). => (1 2) Baris Kesatu. (3 4) Baris kedua. (5 6) Baris ke 3")
                a = input("Masukan Input (pisahkan dengan spasi): ").split()
                if len(a) == 6 and all(i.isdigit for i in a):
                    a = list(map(int, a))
                    try:
                        matriks = np.array(a).reshape(3,2)
                        print(f"Matrik Awal :\n{matriks}")
                        matriks = matriks.T 
                        print(f"Matrik Transpose :\n{matriks}")
                    except:
                        print(f"Kesalahan Data") 
                        return False
                else: 
                    print("Input Harus Angka!") 
                    return False
            # print("4. 3x3 To 3x3")
            # print("5. 3x4 To 4x3")
            # print("6. 4x3 To 3x4")
            # print("7. 3x4 To 4x3")
            case "4":
                match sistem:
                    case "nt": os.system("cls")
                print('='*100)
                print(f"(3 = baris, 3 = kolom). 3x3 => 3x3")
                print("Masukan Input (1 2 3 4 5 6 7 8 9). => (1 2 3) Baris Kesatu. (4 5 6) Baris kedua. (7 8 9) Baris ke 3")
                a = input("Masukan Input (pisahkan dengan spasi): ").split()
                if len(a) == 9 and all(i.isdigit for i in a):
                    a = list(map(int, a))
                    try:
                        matriks = np.array(a).reshape(3,3)
                        print(f"Matriks Awal :\n{matriks}\n")
                        matriks = matriks.T
                        print(f"Matriks Transpose :\n{matriks}\n")
                    except:
                        print(f"Kesalahan Data")
                        return False
                else:
                    print("Input Harus Angka!")
                    return False
            # print("5. 3x4 To 4x3")
            # print("6. 4x3 To 3x4")
            # print("7. 3x4 To 4x3")
            case "5":
                match sistem:
                    case "nt": os.system("cls")
                print('='*100)
                print('='*100)
                print(f"(3 = baris, 4 = kolom). 3x4 => 4x3")
                print("Masukan Input (1 2 3 4 5 6 7 8 9 10 11 12). => (1 2 3 4) Baris Kesatu. (5 6 7 8) Baris kedua. (9 10 11 12) Baris ke 3")
                a = input("Masukan Input (pisahkan dengan spasi): ").split()
                if len(a) == 12 and all(i.isdigit() for i in a):
                    a = list(map(int, a))
                    try: 
                        matriks = np.array(a).reshape(3,4)
                        print(f"Matriks Awal :\n{matriks}\n")
                        matriks = matriks.T
                        print(f"Matriks Transpose :\n{matriks}\n")
                    except:
                        print(f"Kesalahan Data")
                        return False
                else: 
                    print("Jumlah angka melebihi jumlah Ordo!")
                    return False
            # print("6. 4x3 To 3x4")
            case "6": 
                match sistem:
                    case "nt": os.system("cls")
                print('='*100)
                print(f"(4 = baris, 3 = kolom). 4x3 => 3x4")
                print("Masukan Input (1 2 3 4 5 6 7 8 9 10 11 12). => (1 2 3) Baris Kesatu. (4 5 6) Baris kedua. ")
                print("(7 8 9) Baris ke 3. (10 11 12) Bariske 4")
                a = input("Masukan Input (pisahkan dengan spasi): ").split()
                if len(a) == 12 and all(i.isdigit() for i in a):
                    a = list(map(int, a))
                    try: 
                        matriks = np.array(a).reshape(4,3)
                        print(f"Matriks Awal :\n{matriks}\n")
                        matriks = matriks.T
                        print(f"Matriks Transpose :\n{matriks}\n")
                    except:
                        print(f"Kesalahan Data")
                        return False
                else: 
                    print("Jumlah angka melebihi jumlah Ordo!")
                    return False
            
            # costum
            case "7":
                def costum(a,b):
                    if a.isdigit() and b.isdigit():
                        a = int(a)
                        b = int(b)
                        
                        print(f"Jumlah Baris: {a}, Jumlah Kolom: {b} => {a}'X'{b}")
                        print("Masukan Input dalam satu baris, dibatasi spasi (1 2 3 4 5)")
                        print("(1 2 3) Adalah baris ke 1 dan seterusnya.... \n")
                        user = input("Masukan Input : ").split()
                        ordo = a + b
                        if all(i.isdigit() for i in user):
                            try:
                                
                                c = np.array(user, dtype=int).reshape(a,b)
                                print(f"Matriks Awal :\n{c}\n")
                                c = c.T
                                print(f"Matriks Transpose :\n{c}\n")
                            except:
                                print("Pasti ada kesalahan Input.")
                                return False
                        else:
                            print("Jumlah angka melebihi jumlah Ordo!")
                            return False
                    else:
                        print("Input harus angka!")
                        return False
                match sistem:
                    case "nt": os.system("cls")
                print('='*100)
                baris = input("Masukan Jumlah baris: ")
                kolom = input("Masukan Jumlah kolom: ")
                matriks = costum(baris,kolom)
            case _:
                print(f"Input tidak sesuai!")