import numpy as np


# membuat array/Vector
a = np.array([1,2,3,4,5])
print(a,"\n")

# Membuat Vector dengan range
b = np.arange(1,10,1) # start, stop, step
print(b,"\n")

# Membuat linear space
c = np.linspace(1,10,4) # start, stop, Jumlah data
print(c,"\n")

# Array Multidimensi
d = np.array([(1,2,3),(4,5,6)]) 
print(d,"\n")

# Array dengan nilai nol
e = np.zeros(5) 
print(e,"\n")
e = np.zeros((5,5)) 
print(e,"\n")

# array dengan nilai satu
f = np.ones(5)
print(f,"\n")
f = np.ones((5,5)) 
print(f,"\n")

# matriks identitas
g = np.identity(5)
print(g,"\n")

g = np.eye(5)
print(g,"\n")