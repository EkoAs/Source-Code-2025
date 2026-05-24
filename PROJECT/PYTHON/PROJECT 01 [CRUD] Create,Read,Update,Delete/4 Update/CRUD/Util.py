import random
import string


def random_kode(panjang:int)->int:
    hasil =''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil
    
