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
        operator = str(input("masukan operator: "))
        num1 = float(input("masukan angka pertama: "))
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
        # Tampilkan menu sub-operator trigonometri 1-12
        print('''
              1. Sisi c
              2. Sisi a
              3. Sisi b
              4. c dari a dan sin(alpha)
              5. c dari b dan cos(alpha)
              6. a dari c dan sin(alpha)
              7. a dari b dan tan(alpha)
              8. b dari c dan cos(alpha)
              9. b dari a dan tan(alpha)
              10. alpha dari a dan c
              11. alpha dari b dan c
              12. alpha dari a dan b
              ''')
        operator = int(input("Masukan opsi (1-12): "))

        result = None  # Tempat menyimpan hasil perhitungan
        if operator < 1 or operator > 12:
            print("Pilihan operator tidak valid!")
        else:
            # Jika operator 4–9, minta input sudut alpha sekali saja
            if 4 <= operator <= 9:
                alpha_deg = float(input("Masukkan sudut alpha (dalam derajat): "))
                alpha_rad = Trigonometry.to_radians(alpha_deg)
            
            # Hitung sesuai operator
            if operator == 1:
                a = float(input("Masukkan sisi a (tinggi): "))
                b = float(input("Masukkan sisi b (alas): "))
                result = TrigonometryBasic.sisi_c(a, b)  # c = sqrt(a^2 + b^2)
                print(f"Hasil sisi c = {result:.2f}")
            elif operator == 2:
                c = float(input("Masukkan sisi c (miring): "))
                b = float(input("Masukkan sisi b (alas): "))
                result = TrigonometryBasic.sisi_a(c, b)  # a = sqrt(c^2 - b^2)
                print(f"Hasil sisi a = {result:.2f}")
            elif operator == 3:
                c = float(input("Masukkan sisi c (miring): "))
                a = float(input("Masukkan sisi a (tinggi): "))
                result = TrigonometryBasic.sisi_b(c, a)  # b = sqrt(c^2 - a^2)
                print(f"Hasil sisi b = {result:.2f}")
            elif operator == 4:
                a = float(input("Masukkan sisi a (tinggi): "))
                result = TrigonometryBasic.c_dari_a_dan_sin_alpha(a, alpha_rad)  # c = a / sin(alpha)
                print(f"Hasil sisi c = {result:.2f}")
            elif operator == 5:
                b = float(input("Masukkan sisi b (alas): "))
                result = TrigonometryBasic.c_dari_b_dan_cos_alpha(b, alpha_rad)  # c = b / cos(alpha)
                print(f"Hasil sisi c = {result:.2f}")
            elif operator == 6:
                c = float(input("Masukkan sisi c (miring): "))
                result = TrigonometryBasic.a_dari_c_dan_sin_alpha(c, alpha_rad)  # a = c * sin(alpha)
                print(f"Hasil sisi a = {result:.2f}")
            elif operator == 7:
                b = float(input("Masukkan sisi b (alas): "))
                result = TrigonometryBasic.a_dari_b_dan_tan_alpha(b, alpha_rad)  # a = b * tan(alpha)
                print(f"Hasil sisi a = {result:.2f}")
            elif operator == 8:
                c = float(input("Masukkan sisi c (miring): "))
                result = TrigonometryBasic.b_dari_c_dan_cos_alpha(c, alpha_rad)  # b = c * cos(alpha)
                print(f"Hasil sisi b = {result:.2f}")
            elif operator == 9:
                a = float(input("Masukkan sisi a (tinggi): "))
                result = TrigonometryBasic.b_dari_a_dan_tan_alpha(a, alpha_rad)  # b = a / tan(alpha)
                print(f"Hasil sisi b = {result:.2f}")
            elif operator == 10:
                a = float(input("Masukkan sisi a (tinggi): "))
                c = float(input("Masukkan sisi c (miring): "))
                result_rad = TrigonometryBasic.alpha_dari_a_c(a, c)  # radian
                result = Trigonometry.to_degrees(result_rad)
                print(f"Sudut alpha = {result:.2f}°")
            elif operator == 11:
                b = float(input("Masukkan sisi b (alas): "))
                c = float(input("Masukkan sisi c (miring): "))
                result_rad = TrigonometryBasic.alpha_dari_b_c(b, c)  # radian
                result = Trigonometry.to_degrees(result_rad)
                print(f"Sudut alpha = {result:.2f}°")
            elif operator == 12:
                a = float(input("Masukkan sisi a (tinggi): "))
                b = float(input("Masukkan sisi b (alas): "))
                result_rad = TrigonometryBasic.alpha_dari_a_b(a, b)  # radian
                result = Trigonometry.to_degrees(result_rad)
                print(f"Sudut alpha = {result:.2f}°")

        input("Tekan Enter untuk kembali ke menu...")
        return ('trigonometry', result)

            
            
            
            
            
            
             
        # return ('trigonometry',a, b, c)
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