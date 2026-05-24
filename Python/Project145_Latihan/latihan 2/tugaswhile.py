import sys

class KumpulanTugasWhile:
    def __init__(self):
        pass

    # 1. Studi Kasus: Penghitung Donasi
    def soal_satu(self):
        print("\nSoal 1\n")
        total_donasi = 0
        jumlah_donatur = 0
        
        while True:
            try:
                donasi = int(input("Masukkan nominal donasi (0 untuk berhenti): "))
                
                if donasi == 0:
                    break
                elif donasi < 0:
                    print("Nominal tidak boleh negatif, silakan coba lagi.")
                    continue
                    
                total_donasi += donasi
                jumlah_donatur += 1
                
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
        
        print("\nHasil Penghitung Donasi")
        print(f"Total donasi yang terkumpul: Rp {total_donasi}")
        print(f"Total jumlah donatur: {jumlah_donatur} orang")

    # 2. Studi Kasus: Perhitungan Stok Barang
    def soal_dua(self):
        print("\nSoal 2\m")
        stok = 100
        print(f"Stok awal: {stok} unit")
        
        while stok > 0:
            try:
                pembelian = int(input(f"Stok saat ini {stok}. Masukkan jumlah pembelian: "))
                
                if pembelian < 0:
                    print("Jumlah pembelian tidak boleh negatif.")
                    continue
                
                stok -= pembelian
                
                if stok <= 0:
                    print(f"Stok habis (Sisa: {stok}). Program berhenti.")
                else:
                    print(f"Sisa stok: {stok} unit")
                    
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
        
        print("--- Perhitungan Stok Selesai ---")

    # 3. Studi Kasus: Mesin Antrian
    def soal_tiga(self):
        print("\nSoal 3\n")
        nomor_antrian = 1
        print("Ketik 'next' untuk mengambil nomor. Ketik 'stop' untuk berhenti.")
        
        while True:
            perintah = input("Masukkan perintah (next/stop): ").strip().lower()
            
            if perintah == 'next':
                print(f"Nomor antrian: {nomor_antrian}")
                nomor_antrian += 1
            elif perintah == 'stop':
                print("Mesin antrian dihentikan.")
                break
            else:
                print("Perintah tidak dikenali. Gunakan 'next' atau 'stop'.")
        
        print("Mesin Antrian Selesai")

    # 4. Studi Kasus: Mesin Kasir
    def soal_empat(self):
        print("\nSoal 4\n")
        total_harga = 0
        
        while True:
            try:
                harga = int(input("Masukkan harga barang (0 untuk selesai): "))
                
                if harga == 0:
                    break
                elif harga < 0:
                    print("Harga tidak boleh negatif.")
                    continue
                    
                total_harga += harga
                
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
        
        print("\nHasil Mesin Kasir\n")
        print(f"Total harga semua barang: Rp {total_harga}")

    # 5. Studi Kasis: Penghitung Langkah hingga Target
    def soal_lima(self):
        print("\nSoal 5")
        target = 10000
        total_langkah = 0
        jumlah_sesi = 0
        print(f"Target langkah hari ini: {target} langkah")
        
        while total_langkah < target:
            try:
                sesi = int(input(f"Langkah saat ini {total_langkah}. Masukkan langkah sesi ini: "))
                
                if sesi < 0:
                    print("Langkah tidak boleh negatif.")
                    continue
                
                total_langkah += sesi
                jumlah_sesi += 1
                
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
        
        print("\nTarget Tercapai!\n")
        print(f"Total langkah: {total_langkah}")
        print(f"Jumlah sesi dilakukan: {jumlah_sesi} kali")



def main():
    tugas_while = KumpulanTugasWhile()
    tugas_while.soal_satu()
    # tugas_while.soal_dua()
    # tugas_while.soal_tiga()
    # tugas_while.soal_empat()
    # tugas_while.soal_lima()
    
    
    
       
if __name__ == "__main__":
    main()