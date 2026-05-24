import package
print(f"__name__ adalah => '{__name__}'")
print(f"__name__ adalah => '{package.__name__}'\n")

# deklarasi 
def tambah(a:int,b:int)->int:
    return a+b

# program utama
if __name__ == '__main__':
    a = 5
    b = 2
    hasil = tambah(a,b)
    print(f"Program Telah berjalan, dengan hasil {hasil}")