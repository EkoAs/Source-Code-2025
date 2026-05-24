import string
import random


key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

print("Daftar ID Unik:")
print(key)