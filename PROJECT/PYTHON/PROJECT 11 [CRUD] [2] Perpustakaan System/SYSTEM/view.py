import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def header_title():
    print("="*60)
    print(f"{'SISTEM PERPUSTAKAAN MAHASISWA':^60}")
    print("="*60)

def tampilkan_menu_utama(nim):
    print(f"\nUser Login: {nim}")
    print("-" * 60)
    print("1. Tambah Data Peminjaman (Pinjam Baru)")
    print("2. Tampilkan Data & Denda (Cek Status)")
    print("3. Kembalikan Buku ")
    print("0. Keluar / Ganti NIM")
    print("-" * 60)

def tampilkan_data_tabel(list_data, engine_class):
    if not list_data:
        print("\n" + f"{'TIDAK ADa DATA PEMINJAMAN':>60}")
        return

  
    print("\n")
    print(f"{'ID':>10} | {'JUDUL BUKU':>20} | {'LAMA':>5} | {'DENDA (Rp)':>12}")
    print("-" * 60)

    for data in list_data:
        denda = engine_class.hitung_denda(data['lama'])
        print(f"{data['id']:>10} | {data['judul']:>20} | {data['lama']:>5} | {denda:>12,}")
    
    print("-" * 60)

def input_rata_kanan(label):
    return input(f"{label.ljust(20)} : ")