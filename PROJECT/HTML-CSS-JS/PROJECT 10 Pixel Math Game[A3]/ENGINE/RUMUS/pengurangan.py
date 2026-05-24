import random

def generate():
    # Angka A (20-100)
    a = random.randint(20, 100)
    # Angka B (1 sampai A) -> Agar hasil selalu positif
    b = random.randint(1, a) 
    
    jawaban = a - b
    
    # Buat Pengecoh
    opsi = {jawaban}
    while len(opsi) < 4:
        # Pengecoh di sekitar jawaban (+- 10)
        fake = jawaban + random.randint(-10, 10)
        # Pastikan pengecoh tidak minus dan tidak sama dengan jawaban
        if fake >= 0 and fake != jawaban:
            opsi.add(fake)
            
    list_opsi = list(opsi)
    random.shuffle(list_opsi)
    
    return {
        "soal": f"{a} - {b}",
        "opsi": list_opsi,
        "kunci": jawaban,
        "waktu": 8
    }