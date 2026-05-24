from . import Database
from .Util import random_kode
import time
    
def update(no_buku, pk, data_add, tahun, judul, penulis):
    data = Database.TEMPLATE.copy()
    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)
    data = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    
    data_legth = len(data)
    try : # r+ menimpa data
        with open(Database.DB_NAME, 'r+', encoding='utf-8') as file:
            file.seek(data_legth *(no_buku-1))
            file.write(data)
    except:
        print("Data gagal di update.")
        return False     
    
    
def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()
    data["pk"] = random_kode(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["penulis"][len(judul):]
    data["tahun"] = str(tahun)
    data = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    try:
        with open(Database.DB_NAME, 'a', encoding='utf-8') as file:
            file.write(data)
    except:
        print("Data gagal di simpan.")




def create_fist_data():
    penulis = input("penulis: ")
    judul = input("Judul: ")
    while(True):
        try:
            tahun = int(input("Masukan tahun :"))
            if len(str(tahun)) == 4:
                break
        except ValueError:
            print("Tahun harus berupa angka.")
            print("Silakan masukan tahun lagi (yyyy)")
    
    data = Database.TEMPLATE.copy()
    data["pk"] = random_kode(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["penulis"][len(judul):]
    data["tahun"] = str(tahun)
    
    data = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    
    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data)
    except:
        print("gagal")

def read(**kwargs):
    
    try:
        with open(Database.DB_NAME, 'r',encoding='utf-8') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if jumlah_buku == 0:
                print("Database kosong.")
                return False
            
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku >= jumlah_buku:
                    print("Nomor buku tidak valid.")
                    return False
                else:
                    return content[kwargs["index"]-1]
                
            else:
                return content
    
    except:
        print("database error")
        return False
    
    