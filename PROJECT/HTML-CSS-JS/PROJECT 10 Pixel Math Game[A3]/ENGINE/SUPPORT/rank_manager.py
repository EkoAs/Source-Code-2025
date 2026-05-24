import os

DB_FILE = "rank_data.txt"

def get_top_rank():
    if not os.path.exists(DB_FILE):
        return "--- : 0"
    
    try:
        # Format file: Nama,Score 
        tertinggi_skor = 0
        tertinggi_nama = "---"
        
        with open(DB_FILE, "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    nama = parts[0]
                    skor = int(parts[1])
                    if skor > tertinggi_skor:
                        tertinggi_skor = skor
                        tertinggi_nama = nama
                        
        return f"{tertinggi_nama} : {tertinggi_skor}"
    except:
        return "--- : 0"

def save_score(nama, score):
   
    with open(DB_FILE, "a") as f:
        f.write(f"{nama},{score}\n")