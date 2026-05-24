import random

def generate():
    a = random.randint(10, 50)
    b = random.randint(10, 50)
    jawaban = a + b
    
    opsi = {jawaban}
    while len(opsi) < 4:
        fake = jawaban + random.randint(-20, 20)
        if fake > 0 and fake != jawaban:
            opsi.add(fake)
            
    list_opsi = list(opsi)
    random.shuffle(list_opsi)
    
    return {
        "soal": f"{a} + {b}",
        "opsi": list_opsi,
        "kunci": jawaban,
        "waktu": 6
    }