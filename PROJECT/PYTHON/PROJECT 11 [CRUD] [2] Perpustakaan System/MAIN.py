from SYSTEM import engine, view

def main():
    library = engine.LibraryEngine()

    while True:
        view.clear_screen()
        view.header_title()
        
        nim = view.input_rata_kanan("Masukkan NIM")
        
        if not nim:
            break
            
        while True:
            view.clear_screen()
            view.header_title()
            
            data_user = library.get_data_by_nim(nim)
          
            view.tampilkan_menu_utama(nim)
            pilihan = input("Pilih Menu [0-3]: ")
            # ====================================================ADD BUKU BARU===============================
            if pilihan == '1':
                view.clear_screen()
                view.header_title()
                print(f"{'FORM PEMINJAMAN':^60}")
                
                nama = view.input_rata_kanan("Nama Peminjam")
                judul = view.input_rata_kanan("Judul Buku")
                try:
                    lama = int(view.input_rata_kanan("Lama Pinjam (hari)"))
                    library.tambah_peminjaman(nim, nama, judul, lama)
                    print(f"\n{'Data Berhasil Disimpan!':>60}")
                except ValueError:
                    print(f"\n{'Input hari harus angka!':>60}")
                
                input("\nEnter untuk kembali...")


            # ====================================TAMPILKAN DATA DAN HITUNG DENFA===============
            elif pilihan == '2':
                view.clear_screen()
                view.header_title()
                print(f"{'DATA PEMINJAMAN ANDA':^60}")
                if not data_user:
                    print(f"\n{'Belum ada buku yang dipinjam.':>60}")
                else:
                    for item in data_user:
                        denda = library.hitung_denda(item['lama'])
                        print("-" * 60)
                        print(f"{'ID Peminjaman':<20}: {item['id']:>15}")
                        print(f"{'Nama':<20}: {item['nama']:>15}")
                        print(f"{'Judul Buku':<20}: {item['judul']:>15}")
                        print(f"{'Lama Pinjam':<20}: {item['lama']:>10} hari")
                        print(f"{'Denda':<20}: Rp{denda:>13,}")
                
                input("\nEnter untuk kembali...")

            #================================================= Kembalikan Buku ================
            elif pilihan == '3':
                view.clear_screen()
                view.header_title()
                view.tampilkan_data_tabel(data_user, library)
                
                if data_user:
                    id_hapus = view.input_rata_kanan("Masukan ID Buku")
                    berhasil = library.kembalikan_buku(id_hapus)
                    
                    if berhasil:
                        print(f"\n{'Buku berhasil dikembalikan & data dihapus.':>60}")
                    else:
                        print(f"\n{'ID tidak ditemukan!':>60}")
                
                input("\nEnter untuk kembali...")

            elif pilihan == '0':
                break
            
            else:
                print("Pilihan tidak valid.")
                input("Enter...")
        
      
        view.clear_screen()
        lanjut = input("Apakah ingin login dengan NIM lain? (y/n): ")
        if lanjut.lower() != 'y':
            view.clear_screen()
            print("Terimakasih telah menggunakan program kami :)")
            break

if __name__ == "__main__":
    main()