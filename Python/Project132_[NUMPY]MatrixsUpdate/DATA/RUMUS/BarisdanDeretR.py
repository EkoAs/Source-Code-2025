import os
sistem = os.name

class Rumus():
    # tempat perhitungan 
    def deret_aritmatika(a, b, n):
        hasil = a + (n - 1) * b
        return hasil
    def deret_geometri(a, r, n):
        hasil = a * (r ** (n - 1))
        return hasil
    # ======================================================================== Perbaikan !!!
    def deret_tak_hingga(s,r):
        if abs(r) < 1:
            return s / (1 - r)
        else:
            print(f"Rasio harus dibawah satu!!")
            return None



class BarisDeret():
    def __init__(self):
        pass

    def barisan_Aritmatika():
        match sistem:
            case "nt": os.system("cls")
        print('='*60)
        a = input("Masukan Suku pertama: ")
        b = input("Masukan Suku beda: ")
        n = input("Masukan Suku ke -n: ")
        if a.isdigit() and b.isdigit() and n.isdigit():
            suku = float(a)
            beda = float(b)
            nilai_n = float(n)
            try:
                correct = Rumus.deret_aritmatika(suku,beda,nilai_n)
                print('='*50, "\n")
                print(f"Hasil deret aritmatika dengan beda {beda}:\n")
                for i in range(1, int(nilai_n)+1):
                    print(f"Suku ke-{i}:", Rumus.deret_aritmatika(suku, beda, i))
                print(f"Hasil deret aritmatika suku ke-{nilai_n}:", correct, "\n")
            except:
                print(f"Terjadi kesalahan!. Periksa kembali input")
                return False
        else:
            print("Input tidak valid!")
            return False
    
    
    
    def barisan_Geometri():
        match sistem:
            case "nt": os.system("cls")
        print('='*60)
        suku = input("Masukan Suku pertama: ")
        rasio = input("Masukan Rasio: ")
        nilai_n = input("Masukan Suku ke -n: ")
        if suku.isdigit() and rasio.isdigit() and nilai_n.isdigit():
            suku = float(suku)
            rasio = float(rasio)
            nilai_n = int(nilai_n)
            try:
                correct = Rumus.deret_geometri(suku,rasio,nilai_n)
                print('='*50, "\n")
                print(f"Hasil deret geometri dengan rasio {rasio}:\n")
                for i in range(1, nilai_n+1):
                    print(f"Suku ke-{i}:", Rumus.deret_geometri(suku, rasio, i))
                print(f"Hasil deret geometri suku ke-{nilai_n}:", correct, "\n")
            except:
                print(f"Terjadi kesalahan!. Periksa kembali input")
                return False
            
    
    
    def deret_tak_hingga():
        match sistem:
            case "nt": os.system("cls")
        print('='*60)
        print(f"Masukan Suku pertama dan Rasio (tidak lebih dari 1) :")
        suku = input("Masukan suku Pertama: ")
        beda = input("Masukan rasio: ")

        try:
            if suku.isdigit() and beda.count(".") == 1 :
                print('='*50, "\n")
                suku = int(suku)
                rasio = float(beda)

                hasil = Rumus.deret_tak_hingga(suku,rasio)
                print(f"Hasil dari nilai ke {rasio} adalah : {hasil}")
            else: 
                print(f"Input rasio harus dibawah 1!")
                return False
        except:
            print(f"periksa kembali input!")
            return False
    
    def deret_fibonacci():
        match sistem:
            case "nt": os.system("cls")
        print('='*60)
        
        print(f"Kembali lagi nanti!")
        pass
                
    
                