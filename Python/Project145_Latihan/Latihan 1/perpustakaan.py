import random
import os
data_list=[]
class Perpustakaan:
    def __init__(value,kode=None,nama=None,buku=None,tgl_p=None,tgl_k=None,denda=0):
        value.kode = kode
        value.nama = nama
        value.buku = buku
        value.tgl_p = tgl_p
        value.tgl_k = tgl_k
        value.denda = denda
        
    def user_input(value):
        print(f"{'='*30}")
        value.kode = random.randint(0,200)
        nama_s = input("Masukan nama: ")
        buku_s = input("masukan Nama Buku: ")
        tgl_p_s = input("Masukan tgl pinjam, Ex(12/32/2025): ")
        tgl_k_s = input("Masukan tgl kapan dikembalikan: ")
        value.nama = nama_s
        value.buku = buku_s
        value.tgl_p = tgl_p_s
        value.tgl_k = tgl_k_s
        
        value.denda = float(value.denda)
        value.denda = 100
        
        
        data_Dict = {
            "kode":value.kode,
            "nama":value.nama,
            "buku":value.buku,
            "pinjam":value.tgl_p,
            "kembali":value.tgl_k,   
            "denda":value.denda
        }
        try:
            data_list.append(data_Dict)
        except ValueError:
            print("Kesalahan data")
        Perpustakaan.view(value)
        
    def view(value):
        number = 1
        print(f"\n{'No':<2} | {'kode':<8} | {'nama':<15} | {'buku':<15} | {'pinjam':<8} | {'kembali':<8} | {'denda':<10}")
        for a in data_list:
            if not data_list:
                print(f"Belum ada data!.")
            else:
                os.system('cls' if os.name=='nt' else "clear")
                print(f"{'='*70}")
                print(f"\n{number:<2} | {a['kode']:<8} | {a['nama']:<15} | {a['buku']:<15} | {a['pinjam']:<8} | {a['kembali']:<8} | {a['denda']:<10}")
            number+=1
      
    def hitung(value):
        total = 0
        for i in data_list:
            if not data_list:
                print("Data masih kosng")
            else:
                total += i['denda']
        print(f"\n\ntotal Denda {total}")
    def run_Engine(value):
        while True:
            Perpustakaan.user_input(value)
            Perpustakaan.hitung(value)
            yyy = input("\nIngin menambah data lagi? (y/n): ")
            if yyy.lower() != 'y':
                print("Terima kasih telah menggunakan program ini.")
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
if __name__=='__main__':
    run = Perpustakaan()
    run.run_Engine()
    
        
        