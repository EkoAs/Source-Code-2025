class TugasFungsi:
    def __init__(self):
        print("=== Program Kumpulan Tugas Python (OOP) ===")
        print("Dibuat oleh: Eko Asif Bahri")
        print("-" * 40)

    
    # 1. Studi Kasus: Penghitung Ongkir
   
    def hitung_ongkir(self, berat):
        if berat <= 1:
            biaya = 10000
        elif berat <= 5:
            biaya = 25000
        else:
            biaya = 50000
        return biaya

    def run_tugas_1(self):
        print("\n--- 1. Penghitung Ongkir ---")
        try:
            berat = float(input("Masukkan berat paket (kg): "))
            total = self.hitung_ongkir(berat)
            print(f"Berat: {berat} kg -> Total Ongkir: Rp {total:,}")
        except ValueError:
            print("Input harus berupa angka.")

    
    # 2. Studi Kasus: Sistem Perpustakaan
   
    def cek_denda(self, hari):
        return 2000 * hari

    def laporan_pengembalian(self, nama, hari):
        denda = self.cek_denda(hari)
        print("\n[Laporan Pengembalian]")
        print(f"Nama Peminjam    : {nama}")
        print(f"Terlambat        : {hari} hari")
        print(f"Total Denda      : Rp {denda:,}")

    def run_tugas_2(self):
        print("\n--- 2. Sistem Perpustakaan ---")
        nama = input("Masukkan nama peminjam: ")
        try:
            hari = int(input("Masukkan lama keterlambatan (hari): "))
            self.laporan_pengembalian(nama, hari)
        except ValueError:
            print("Input hari harus berupa angka bulat.")

   
    # 3. Studi Kasus: Perhitungan Listrik
  
    def hitung_pemakaian(self, w1, w2):
        return w2 - w1

    def hitung_biaya_listrik(self, pemakaian):
        return pemakaian * 1500

    def run_tugas_3(self):
        print("\n--- 3. Perhitungan Listrik ---")
        try:
            w1 = float(input("Masukkan Meter Awal (kWh): "))
            w2 = float(input("Masukkan Meter Akhir (kWh): "))
            
            if w2 < w1:
                print("Error: Meter akhir tidak boleh lebih kecil dari meter awal.")
                return

            pemakaian = self.hitung_pemakaian(w1, w2)
            biaya = self.hitung_biaya_listrik(pemakaian)
            
            print(f"Pemakaian Listrik : {pemakaian} kWh")
            print(f"Total Biaya       : Rp {biaya:,}")
        except ValueError:
            print("Input harus berupa angka.")

   
    # 4. Studi Kasus: Hitung BMI
  
    def hitung_bmi(self, berat, tinggi):
        # Rumus: berat / (tinggi dalam meter kuadrat)
        bmi = berat / (tinggi ** 2)
        
        kategori = ""
        if bmi < 18.5:
            kategori = "Kurus"
        elif 18.5 <= bmi <= 24.9:
            kategori = "Normal"
        elif 25 <= bmi <= 29.9:
            kategori = "Gemuk"
        else:
            kategori = "Obesitas"
            
        return bmi, kategori

    def run_tugas_4(self):
        print("\n--- 4. Hitung BMI ---")
        try:
            berat = float(input("Masukkan berat badan (kg): "))
            tinggi_cm = float(input("Masukkan tinggi badan (cm): "))
            tinggi_m = tinggi_cm / 100  # Konversi ke meter
            
            skor_bmi, kategori = self.hitung_bmi(berat, tinggi_m)
            
            print(f"Skor BMI : {skor_bmi:.2f}")
            print(f"Kategori : {kategori}")
        except ValueError:
            print("Input harus berupa angka.")
 
    # 5. Studi Kasus: Penggajian Karyawan
    
    def hitung_gaji_kotor(self, gaji_pokok, tunjangan):
        return gaji_pokok + tunjangan

    def hitung_potongan(self, gaji_kotor):
        bpjs = 0.01 * gaji_kotor  # 1%
        pajak = 0.05 * gaji_kotor # 5%
        return bpjs + pajak

    def hitung_gaji_bersih(self, gaji_pokok, tunjangan):
        kotor = self.hitung_gaji_kotor(gaji_pokok, tunjangan)
        potongan = self.hitung_potongan(kotor)
        bersih = kotor - potongan
        return kotor, potongan, bersih

    def run_tugas_5(self):
        print("\n--- 5. Penggajian Karyawan ---")
        try:
            gapok = float(input("Masukkan Gaji Pokok: Rp "))
            tunjangan = float(input("Masukkan Tunjangan : Rp "))
            
            kotor, pot, bersih = self.hitung_gaji_bersih(gapok, tunjangan)
            
            print("-" * 30)
            print(f"Gaji Kotor  : Rp {kotor:,.0f}")
            print(f"Total Potongan (BPJS+Pajak): Rp {pot:,.0f}")
            print(f"Gaji Bersih : Rp {bersih:,.0f}")
        except ValueError:
            print("Input harus berupa angka.")

    # ==========================================
    # Menu Utama
    # ==========================================
    def main_menu(self):
        while True:
            print("\n" + "="*30)
            print(" MENU TUGAS FUNGSI (OOP)")
            print("="*30)
            print("1. Hitung Ongkir")
            print("2. Sistem Perpustakaan")
            print("3. Hitung Listrik")
            print("4. Hitung BMI")
            print("5. Hitung Gaji Karyawan")
            print("0. Keluar")
            
            pilihan = input("Pilih menu (0-5): ")
            
            if pilihan == '1':
                self.run_tugas_1()
            elif pilihan == '2':
                self.run_tugas_2()
            elif pilihan == '3':
                self.run_tugas_3()
            elif pilihan == '4':
                self.run_tugas_4()
            elif pilihan == '5':
                self.run_tugas_5()
            elif pilihan == '0':
                print("Terima kasih, Asif! Program selesai.")
                break
            else:
                print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    app = TugasFungsi()
    app.main_menu()