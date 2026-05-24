from . import Operasi


DB_NAME = "data.txt" 
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
    }

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("database tersedia, init done!")
    except:
        print("database tdak di temukan, silakan buat buat data baru")
        Operasi.create_fist_data()  
            
            
            
            
            
            
            