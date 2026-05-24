class Reads:
    def __init__(self):
        pass
    
    def option():
        num1= input("Masukan input pertama: ")
        if num1.isdigit():
            num = int(num1)
            num = num/2
            if (num % 2) == 0:
                print(f" {num1} bilangan ini adalah Genap")
            else:
                print(f" adalah bilangan Ganjil")
        else:
            print(f"Input bukan angka")
        print(f"\n")
        num1 = int(num1)
        Reads.kondisi(num1) 
    
    
    def kondisi(num1):
        print(f"input pertama adalah {num1}")
        number2 = input("Masukan input: ")
        if number2.isdigit():
            number2= int(number2)
            if num1 > number2:
                print(f"\n{num1} adalah bilangan paling besar")
            elif num1 < number2:
                print(f"\n{number2} lebih besar")
                
    def jam_kerja():
        nama = input("nama karyawan: ")
        jam_kerja= int(input("masukan jumlah jam kerja: "))
        upah_biasa= 2000
        upah_lembur = 3000
        if jam_kerja > 48:
            sisa_jam = jam_kerja - 48
            jam_awal = jam_kerja - sisa_jam
            result = jam_awal * upah_biasa
            result2 = sisa_jam * upah_lembur
            gaji = result + result2
            print(f"{nama} Upah nya adalah {gaji}")
        elif jam_kerja <=48:
            result = jam_kerja * upah_biasa
            print(f" {nama} gaji tanpa lembur {result}")
      

# Reads.option()
Reads.jam_kerja()  

  