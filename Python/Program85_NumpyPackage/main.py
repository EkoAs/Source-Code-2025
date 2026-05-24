import numpy as np

# operasi langsung 
matrixA = np.array([1,2,3,4])
print(f"Hasil dari pangkat 2 = \n {matrixA**2}")

# matrik ber ordo
matrixB = np.array([(1,2,3),(4,5,6),(7,8,9)]) # setiap kurung () adalah kolom/ baris baru
print(f"matrix Ber ordo = \n{matrixB}")

# matrix zeros
matrixC = np.zeros((2,2))
print(f"matrix Zeros = \n{matrixC}")

# matrix ones
matrixD = np.ones((3,3))
print(f"matrix ones = \n{matrixD}")

# operasi matrix
x = np.array([(1,2,3),(4,5,6)])
y = np.array([(1,2,3),(4,5,6)])
z = np.array([(1,2),(4,5)])

hasil = x + y
print(f"Hasil matrix = \n {hasil}")


