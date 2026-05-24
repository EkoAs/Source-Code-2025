# String width and alignment
# String width and alignment    

nama = "Ucup"
umur = 17
tinggi = 290

string = f"Nama : {nama} + umur : {umur} + tinggi : {tinggi}"
print(string)

print("="*5+"String"+"="*5) # Rata kanan
print(f"""
nama   : {nama:.<10}
Umur   : {umur:.<10}
tinggi : {tinggi:.<10}
      """)
print("="*5+"String"+"="*5) # Rata tengah
print(f"""
nama   : {nama:.^10}
Umur   : {umur:.^10}
tinggi : {tinggi:.^10}
      """)
