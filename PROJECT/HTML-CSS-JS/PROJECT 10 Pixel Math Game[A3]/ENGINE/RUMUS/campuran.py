import random

def rn():
    # Angka Standar (1-9)
    return random.randint(1, 9)

def rn_big():
   
    return random.randint(10, 20)

def ro():

    return random.choice(['+', '-', '*'])

def generate():
    # ==========================================================================
    # DAFTAR TEMPLATE 
    # Menggunakan ;ambda agar angka digenerate ulang setiap kali dipanggil;l
  
    templates = [
       
        lambda: f"{rn()} + {rn()} - {rn()}",              # 5 + 3 - 2
        lambda: f"{rn()} * {rn()} - {rn()}",              # 5 x 3 - 2
        lambda: f"{rn_big()} - {rn()} * {rn()}",          # 15 - 2 x 3

       
        lambda: f"({rn()} + {rn()}) * {rn()}",            # (2 + 3) x 4
        lambda: f"{rn()} * ({rn()} + {rn()})",            # 2 x (3 + 4)
        lambda: f"({rn_big()} - {rn()}) * {rn()}",        # (15 - 5) x 2

       
        lambda: f"{rn()} + {rn()} + {rn()} - {rn()}",     # 2 + 3 + 4 - 5
        lambda: f"{rn()} * {rn()} + {rn()} * {rn()}",     # 2 x 2 + 3 x 3
        
      
        lambda: f"({rn()} + {rn()}) - ({rn()} + {rn()})", # (5+5) - (2+1)
        lambda: f"({rn()} * {rn()}) + ({rn()} * {rn()})", # (2x3) + (4x4)
        lambda: f"({rn()} * {rn()}) - ({rn()} * {rn()})", # (5x5) - (2x2)

       
        lambda: f"(({rn()} + {rn()}) * {rn()}) - {rn()}", # ((2+1) x 5) - 4
        lambda: f"{rn_big()} - (({rn()} * {rn()}) - {rn()})", # 20 - ((3x3) - 2)
        
     
        lambda: f"({rn_big()} * {rn_big()}) * 0",         # Hasil pasti 0
        lambda: f"({rn()} + {rn_big()}) * 1",             # Cuma penjumlahan biasa
        
        
        lambda: f"({rn()} + {rn()}) + ({rn_big()} - {rn()}) + {rn()}", 
        lambda: f"{rn()} + ({rn()} * {rn()}) - ({rn()} + {rn()})"
    ]
    
    # 1. Pilih Struktur secara acak
    pembuat_soal = random.choice(templates)
    
    # 2. Generate String Soal
    soal_raw = pembuat_soal()
    
    # 3. Hitung Jawaban (Python eval() otomatis tau urutan kurung)
    jawaban = eval(soal_raw)
    
    # 4. Format Tampilan (Ganti * jadi x untuk user)
    soal_tampil = soal_raw.replace('*', 'x')
    
    # 5. Buat Pengecoh (Lebih rapat range-nya biar susah ditebak)
    opsi = {jawaban}
    while len(opsi) < 4:
        
        fake = jawaban + random.randint(-10, 10)
        # Pastikan pengecoh beda dengan jawaban
        if fake != jawaban:
            opsi.add(fake)
            
    list_opsi = list(opsi)
    random.shuffle(list_opsi)
    
    return {
        "soal": soal_tampil,
        "opsi": list_opsi,
        "kunci": jawaban,
        "waktu": 5  
    }