# Type hints pada fungsi
# def nama_fungsi(argumen:int)
#   print()

def fungsi(num:int) :
    hasil = num ** 2
    return hasil
end = fungsi(5)  
print(end)


def hello(num:int) ->int:
    print(f"{num}")
   
hello("helo")

import string
def strin(kalimat:string) -> str:
    return strin
halo = strin("halo kawan")
print(halo)
