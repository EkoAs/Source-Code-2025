import random

def generate():
    # Tentukan pembagi (2 sampai 10)
    b = random.randint(2, 10)
    # Tentukan jawaban yang diinginkan (2 sampai 10)
    jawaban_asli = random.randint(2, 12)
    
    # Hitung angka yang mau dibagi
    a = b * jawaban_asli
    
    # Jadi soalnya: A : B = Jawaban Asli
    # Contoh: 20 : 4 = 5
    
    jawaban = jawaban_asli
    
    # Buat Pengecoh
    opsi = {jawaban}
    while len(opsi) < 4:
        fake = jawaban + random.randint(-5, 5)
        if fake > 0 and fake != jawaban:
            opsi.add(fake)
            
    list_opsi = list(opsi)
    random.shuffle(list_opsi)
    
    # Gunakan simbol bagi (:) atau (÷)
    return {
        "soal": f"{a} : {b}",
        "opsi": list_opsi,
        "kunci": jawaban,
        "waktu": 8
    }