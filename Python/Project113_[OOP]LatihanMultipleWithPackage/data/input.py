# from progres import Math, TrigonometryBasic, Trigonometry, BangunRuang
from progres.operating import Math, TrigonometryBasic, Trigonometry, BangunRuang
# from progres.operating import BangunRuang
def __information__():
    pass
def chose():
    print(f"{'='*10}Modern Calculator")
    print('''
          1 : kalkulator biasa
          2 : Kalkulator Trigonometry
          3 : Kalkulator Bangun Ruang
          4 : Kalkulator Faktorial
          Chose the input with number
          ''')
    pilihan = int(input("Model Kalkulator: "))
    
    if pilihan == 1:
        num1 = float(input("masukan angka pertama: "))
        operator = str(input("masukan operator: "))
        num2 = float(input("masukan angka kedua: "))
        if operator == '+':
            print("Hasil:", Math.add(num1, num2))
        elif operator == '-':
            print("Hasil:", Math.min(num1, num2))
        elif operator == '/':
            print("Hasil:", Math.bagi(num1, num2))
        elif operator == '*' or operator == 'x':
            print("Hasil:", Math.kali(num1, num2))
        elif operator == '**' or operator.lower() == 'pangkat':
            print("Hasil:", Math.pangkat(num1, num2))
        elif operator == '%':
            print("Hasil:", Math.modulus(num1, num2))
            
    elif pilihan == 2:
        print('''
              1. Sisi c
              2. Sisi A
              3. Sisi B
              4. C dari A dan Sin Alpha
              5. c dari b dan cos alpha
              6. a dari c dan sin alpha
              7. a dari b dan tan alpha
              8. b dari c dan cos alpha
              9. b dari a dan tan alpha
              10. alpha dari a c
              11. alpha dari b c
              12. alpha dari a b
              
              
              ''')
        a = float(input("Masukkan sisi a (tinggi): "))
        b = float(input("Masukkan sisi b (alas): "))
        c = float(input("Masukkan sisi c (miring): "))
        operator = str(input("masukan Opsi :"))
        if operator == 1:
            print(f"Hasil Sisi C = {TrigonometryBasic.sisi_c(a,b)}")
        elif operator == 2:
            print(f"Hasil Sisi A = {TrigonometryBasic.sisi_a(c,b)}")
        elif operator == 3:
            print(f"Hasil Sisi B = {TrigonometryBasic.sisi_b(c,a)}")
        elif operator == 4:
            print(f"Hasil = {TrigonometryBasic.c_dari_a_dan_sin_alpha(a)}") 
        elif operator == 5:
            pass    
            
            
            
            
            
             
        return ('trigonometry',a, b, c)
    elif pilihan == 3:
        panjang = int(input("Masukan Panjang"))
        lebar = int(input("Masukan lebar"))
        tinggi = int(input("Masukan tinggi"))
        diameter = input("Masukkan Diameter jika ada (ketik - jika tidak): ")
        diameter = float(diameter) if diameter != '-' else None
        operasi = str(input("masukan Operator :"))
        
        if operasi.lower() == 'vo':
            print(f"Volumenya => {BangunRuang.volumeBalok(panjang, lebar, tinggi)}")
        elif operasi.lower() == 'ke':
            print(f"Kelilingnya => {BangunRuang.kelilingBalok(panjang, lebar)}")
        elif operasi.lower() == 'lu':
            print(f"Kelilingnya => {BangunRuang.luasBalok(panjang, lebar)}")
       
    elif pilihan == 4:
        angka = int(input("Masukkan bilangan bulat positif (atau -1 untuk keluar): "))
        return ('faktorial',angka)