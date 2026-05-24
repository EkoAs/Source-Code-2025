from . import Database
from .Util import random_kode
import time



def create_fist_data():
    penulis = input("penulis: ")
    judul = input("Judul: ")
    tahun =input("tahun :")
    data = Database.TEMPLATE.copy()
    data["pk"] = random_kode(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())

    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["penulis"][len(judul):]
    data["tahun"] = tahun
    
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
    
    