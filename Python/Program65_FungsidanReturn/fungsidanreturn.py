# Fungsi dengan return 

def fungsi(x):
    hasil = x ** 2
    return hasil # return memasukan hasil pangkat ke dalam y
y = fungsi(2) 
print(y)

# fungsi return langsung
def tambah(a):
    return a ** 2
b = tambah(2)
print(b)

# fungsi dengan banyak operator
def banyak(c):
    t = c + 1    
    k = c - 1    
    b = c / 1    
    return t, k, b
t, k, b = banyak(2)
print(t)
print(k)
print(b)
    
    
    
    
    
    
    
    
    