import os


sistem = os.name
if __name__ == "__main__":
    class Reads:
        def __init__(self):
            pass
        
        def Tugas_satu(self="None"):
            user_input = input("Masukan Total Pembelian: ")
            while True:
                if user_input.isdigit():
                    user_input = int(user_input)
                    break
                else:
                    print(f"Input harus berupa angka! ")
                    return False
            if user_input > 100000:
                print(f"Anda mendapat diskon 20% menjadi {user_input / 20}")
            elif ((user_input < 100000) and (user_input > 50000)):
                print(f"Anda mendapat diskon 15% menjadi {user_input / 15}")
            elif ((user_input < 50000) and (user_input > 10000)):
                print(f"Anda mendapat diskon 10% menjadi {user_input / 10}")
            elif user_input < 10000:
                print(f"Anda tidak mendapat diskon")
            else:
                print(f"Anda tidak mendapat diskon")
                
                
        def Tugas_dua(self="None"):
            jam_lembur = 3000
            
            def golongan_satu():
                nama = input("nama karyawan: ")
                jam_kerja= int(input("masukan jumlah jam kerja: "))
                upah_biasa= 4000
                upah_lembur = 3000
                if jam_kerja > 48:
                    sisa_jam = jam_kerja - 48
                    jam_awal = jam_kerja - sisa_jam
                    result = jam_awal * upah_biasa
                    result2 = sisa_jam * upah_lembur
                    gaji = result + result2
                    print(f"{nama} Upah nya adalah {gaji}")
                    
            
            def golongan_dua():  
                nama = input("nama karyawan: ")
                jam_kerja= int(input("masukan jumlah jam kerja: "))
                upah_biasa= 5000
                upah_lembur = 3000
                if jam_kerja > 48:
                    sisa_jam = jam_kerja - 48
                    jam_awal = jam_kerja - sisa_jam
                    result = jam_awal * upah_biasa
                    result2 = sisa_jam * upah_lembur
                    gaji = result + result2
                    print(f"{nama} Upah nya adalah {gaji}")
                    
    
            def golongan_tiga():  
                nama = input("nama karyawan: ")
                jam_kerja= int(input("masukan jumlah jam kerja: "))
                upah_biasa= 6000
                upah_lembur = 3000
                if jam_kerja > 48:
                    sisa_jam = jam_kerja - 48
                    jam_awal = jam_kerja - sisa_jam
                    result = jam_awal * upah_biasa
                    result2 = sisa_jam * upah_lembur
                    gaji = result + result2
                    print(f"{nama} Upah nya adalah {gaji}")
                    
            def golongan_empat():  
                nama = input("nama karyawan: ")
                jam_kerja= int(input("masukan jumlah jam kerja: "))
                upah_biasa= 7500
                upah_lembur = 3000
                if jam_kerja > 48:
                    sisa_jam = jam_kerja - 48
                    jam_awal = jam_kerja - sisa_jam
                    result = jam_awal * upah_biasa
                    result2 = sisa_jam * upah_lembur
                    gaji = result + result2
                    print(f"{nama} Upah nya adalah {gaji}")
                    
                    
                    
                    
        def Tugas_3(self):
            namasiswa_1 = input("Masukan nama siswa: ")
            namasiswa_2 = input("Masukan nama siswa: ")
            namasiswa_3 = input("Masukan nama siswa: ")
            namasiswa_4 = input("Masukan nama siswa: ")
            namasiswa_5 = input("Masukan nama siswa: ")
            while(True):
                siswa_1 = input("Masukan nilai : ")
                siswa_2 = input("Masukan nilai : ")
                siswa_3 = input("Masukan nilai : ")
                siswa_4 = input("Masukan nilai : ")
                siswa_5 = input("Masukan nilai : ")
                if siswa_1.isdigit() and siswa_2.isdigit() and siswa_3.isdigit() and siswa_3.isdigit() and siswa_5.isdigit():
                    break
                else:
                    print(f"Input harus berupa angka!")
            result = ((siswa_1+siswa_2+siswa_3+siswa_4+siswa_5) / 5)
            print(f"{namasiswa_1} memiliki nilai {siswa_1}")
            print(f"{namasiswa_2} memiliki nilai {siswa_2}")
            print(f"{namasiswa_3} memiliki nilai {siswa_3}")
            print(f"{namasiswa_4} memiliki nilai {siswa_4}")
            print(f"{namasiswa_5} memiliki nilai {siswa_5}")
            print(f"nilai rata rata seluruh siswa adalah {result}")
            
            
            
            
            
        def Tugas_4():
            produksi = int(input("masukan jumlah produksi perhari: "))
            per_minggu = 7
            sisa = produksi / 7
            num = 0
            for sisa in range(7):
                sisa += sisa
            hasil = sisa/per_minggu
            print(f"rata rata produksi per hari adalah {hasil}, dan per minggu {sisa}")
            
        def Tugas_5():
            def Tugas_5(self="None"):
                total = 0.0
                for hari in range(1, 11):
                    while True:
                        nilai = input(f"Masukkan tabungan hari ke-{hari}: ")
                        try:
                            jumlah = float(nilai)
                            if jumlah < 0:
                                print("Input harus berupa angka non-negatif!")
                                continue
                            break
                        except ValueError:
                            print("Input harus berupa angka!")
                    total += jumlah
                if total.is_integer():
                    total = int(total)
                print(f"Total tabungan setelah 10 hari adalah {total}")
                
            
            
            
            
    Reads.Tugas_satu()
                

