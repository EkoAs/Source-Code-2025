import math as mt

def powcalt(num,num2):
    result = mt.pow(num,num2)
    print(f"\n\nHasil {num} Pangkat {num2} = {result}")
    
def absolute(num):
    result=mt.fabs(num)
    print(f"Nilai absolute dari {num} adalah {result}")
    
def akar(num):
    result=mt.sqrt(num)
    print(f"Akar kuadrat dari {num} adalah {result}")
    
def pembulatan(num):
    result=mt.ceil(num)
    result2=mt.floor(num)
    print(f"Pembulatan ke atas {num} = {result}")
    print(f"Pembulatan ke bawah {num} = {result2}")
    
def luas_lingkaran(self=None):
    r=7
    result=mt.pi * r ** 2
    print(f"Luas lingkaran dgn jari2 {r} = {result}")
    
def latihan(num):
    result = mt.sqrt(num)
    print(f"hasil akar kuadrat dari {num} = {result}")
num = float(input("Masukan angkan pertama: "))
num2 = float(input("Masukan angkan kedua: "))

# deklarasi function
powcalt(num,num2)
absolute(num)
akar(num)
pembulatan(num)
luas_lingkaran(self=None)
latihan(num)