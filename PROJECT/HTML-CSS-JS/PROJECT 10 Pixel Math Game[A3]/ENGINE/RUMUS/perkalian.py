import random

def generate():
  
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    jawaban = a * b
    
   # bagian jebakanm
    opsi = {jawaban}
    while len(opsi) < 4:
        fake = jawaban + random.randint(-10, 10)
        if fake > 0 and fake != jawaban:
            opsi.add(fake)
            
    list_opsi = list(opsi)
    random.shuffle(list_opsi)
    
    return {
        "soal": f"{a} x {b}",
        "opsi": list_opsi,
        "kunci": jawaban,
        "waktu": 5
    }