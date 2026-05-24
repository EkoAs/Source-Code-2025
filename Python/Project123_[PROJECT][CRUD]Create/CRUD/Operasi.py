from . import Database
from .Util import random_kode
import time
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

def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    
    except:
        print("database error")
        return False
    
    