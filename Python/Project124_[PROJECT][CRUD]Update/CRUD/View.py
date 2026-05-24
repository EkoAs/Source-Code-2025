from . import Operasi


def update_console():
    read_console()
    while(True):
        print("Pilih Nomor yang akan di update.")
        no_buku = int(input("Nomor Buku : "))
        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            break
        
        else:
            print("Nomor buku tidak valid. Silakan coba lagi.")
            
    data_break = data_buku.split(",")
    pk = data_break[0]
    data_add  = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1] # menghilangkan \n di akhir
    
    while(True):
        # data yg ingin di ubah/ update
        print("\n","="*100)
        print("Silakan pilih data apa yg anda ubah :")
        print(f"1. Judul ({judul:.40})")
        print(f"2. Penulis ({penulis:.40})")
        print(f"3. Tahun ({str(tahun):.40})")
        
        # memilih mode untukk update
        user_option = input("Masukan Opsi [1,2,3] :")
        
        print("\n","="*100)
        match user_option:
            case "1": judul = input("Masukan Judul Baru :")
            case "2": penulis = input("Masukan Penulis Baru :")
            case "3": 
                while(True):
                    try:
                        tahun = int(input("Masukan tahun :"))
                        if len(str(tahun)) == 4:
                            break
                    except:
                        print("Tahun harus berupa angka.")
                        print("Silakan masukan tahun lagi (yyyy)")
            case _: print("data yg di pilih, tidak cocok")    
            
        print("\n")
        print("data Baru Anda : ")
        print(f"1. Judul ({judul:.40})")
        print(f"2. Penulis ({penulis:.40})")
        print(f"3. Tahun ({str(tahun):.40})\n")   
         
        done = input("apakah selesai Update? (y/n): ") # lanjut atau selesai. kaloo lanjut kembali ke menu awal
        if done.lower() != 'n':
            break
    Operasi.update(no_buku, pk, data_add, tahun, judul, penulis)   
    
    
    
    
def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")
    penulis = input("Masukan penulis :")
    judul = input("Masukan judul :")
    while(True):
        try:
            tahun = int(input("Masukan tahun :"))
            if len(str(tahun)) == 4:
                break
        except ValueError:
            print("Tahun harus berupa angka.")
            print("Silakan masukan tahun lagi (yyyy)")
            return
    Operasi.create(tahun,judul,penulis)
    print("\n berikut data baru anda: \n")
    read_console()
    
    
    
def read_console():
    data_file = Operasi.read()
    index = "NO"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"
    
    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5} ")
    print('-'*100)
    
    # data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index +1:4} | {judul:.40} | {penulis:.40} | {tahun:4} ", end="")
    
    print("\n"+"="*100)
    
    