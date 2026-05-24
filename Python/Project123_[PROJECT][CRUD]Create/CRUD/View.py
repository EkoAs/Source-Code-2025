from . import Operasi
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
    
    