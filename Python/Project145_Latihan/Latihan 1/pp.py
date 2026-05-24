class AplikasiLaundry:
    def __init__(self):
        self.data_laundry = []

    def menu(self):
        while True:
            print("="*40)
            print("1. Tambah Data Laundry")
            print("2. Tampilkan Daftar Laundry")
            print("3. Hitung Total Pembayaran")
            print("4. Keluar")
            print("="*40)
            pilihan = input("Pilih menu (1-4): ")

            if pilihan == '1':
                self.tambah_laundry()
            elif pilihan == '2':
                self.tampilkan_laundry()
            elif pilihan == '3':
                self.hitung_total()
            elif pilihan == '4':
                print("Terima kasih, sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid, silakan ulangi.")

    def tambah_laundry(self):
        print("\n---  Tambah Data Laundry ---")
        kode = input("Masukkan Kode Laundry   : ")
        nama = input("Masukkan Nama Pelanggan : ")
        
        print("Jenis Layanan (Contoh: Cuci / Cuci Setrika / Setrika)")
        jenis = input("Jenis Layanan   : ")
        
        try:
            harga = int(input("Harga per Kg (Rp)       : "))
            berat = float(input("Berat (Kg)              : "))
        except ValueError:
            print("Input Gagal! Harga dan Berat harus berupa angka.")
            return

        data_baru = {
            'kode': kode,
            'nama': nama,
            'jenis': jenis,
            'harga': harga,
            'berat': berat
        }
        
        self.data_laundry.append(data_baru)
        print(">> Data berhasil disimpan!")
    def tampilkan_laundry(self):
        print("\n---  Daftar Laundry ---")
        if not self.data_laundry:
            print("Data masih kosong.")
        else:
            print(f"{'No':<4} {'Kode':<10} {'Nama':<15} {'Layanan':<15} {'Berat':<8} {'Harga/Kg':<12}")
            print("-" * 70)
            no = 1
            for item in self.data_laundry:
                print(f"{no:<4} {item['kode']:<10} {item['nama']:<15} {item['jenis']:<15} {item['berat']:<8} Rp{item['harga']:,}")
                no += 1

    def hitung_total(self):
        print("\n---  Hitung Total Pembayaran ----")
        if not self.data_laundry:
            print("Data masih kosong!")
            return
        total_kotor = 0
        
        print("\nRincian Transaksi:")
        for item in self.data_laundry:
            
            subtotal = item['harga'] * item['berat']
            total_kotor += subtotal
            print(f"- {item['nama']} ({item['jenis']}): {item['berat']}kg x Rp{item['harga']} = Rp{subtotal:,.0f}")

        diskon = 0
        persen = 0
        
        if total_kotor >= 200000:
            persen = 10
            diskon = total_kotor * 0.10
        elif total_kotor >= 100000:
            persen = 5
            diskon = total_kotor * 0.05
        
        total_bersih = total_kotor - diskon


        AplikasiLaundry.clear()
        print("-" * 40)
        print(f"Total Kotot     : Rp {total_kotor:,.0f}")
        print(f"Diskon ({persen}%)     : Rp {diskon:,.0f}")
        print("-" * 40)
        print(f"TOTAL BAYAR     : Rp {total_bersih:,.0f}")
        print("-" * 40)
    
    def clear():
        import os
        nama = os.name
        match nama:
            case 'nt':
                os.system('cls')
    
    

if __name__ == "__main__":
    app = AplikasiLaundry()
    app.menu()