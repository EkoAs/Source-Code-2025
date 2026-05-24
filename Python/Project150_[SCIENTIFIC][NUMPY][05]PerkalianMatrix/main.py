# perkalian matrix
import numpy as np
a = np.array(([1,2, 5],
              [3,4,6]))


b = np.ones([3,1])
 
print(f"Matrix a adalah  =\n {a}")
print(f"Matrix b adalah  =\n {b}")
#  perkallian matrix a dengan matrix b


# c = a * b
# print(f"perkalian a x  b biasa adalah { c}")

# perkalian cara pertama
c = np.dot(a,b) # biar ada dua fungsi di numpy
print(f"perkalian a x  b dengan dot adalah\n { c}")

# cara kedua posisi a dan b sudah di tentukan 
c1 = a.dot(b) # berbasii oop. objek b ditambahkan kedalam fungsi dot yg menempel di objek a
print(f"perkalian a x  b dengan dot adalah\n { c}")

print(f"\n multiplication")
# melakukan perkalian matriks (matrix multiplication). Sama seperti 
# np.dot() untuk matriks 2D, tetapi berbeda untuk array berdimensi lebih tinggi.
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(c)
c = np.matmul(a, b)
print(c)
# Output:
# [[19 22]
#  [43 50]]

# matrix tranpose
print(f"\n Tranpose")
a = np.array([[1, 2], [3, 4]])
print(a)
print(np.transpose(a))  # atau a.T
# Output:
# [[1 3]
#  [2 4]]

print(f"\n invers")
# Menghitung invers matriks (hanya untuk matriks persegi).
a = np.array([[1, 2], [3, 4]])
print(a)
inv_a = np.linalg.inv(a)
print(inv_a)
# Output:
# [[-2.   1. ]
#  [ 1.5 -0.5]]


print(f"\n determinan")
# hitung determinan
a = np.array([[1, 2], [3, 4]])
det_a = np.linalg.det(a)
print(det_a)
# Output:
# -2.0



print(f"\n nilai eigen ()")
# Fungsi: Menghitung nilai eigen (eigenvalues) dan vektor eigen (eigenvectors) dari matriks persegi.
a = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(a)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

print(f"\n Sistem Persamaan Linear (np.linalg.solve)")
# Menyelesaikan sistem persamaan linear Ax = B
A = np.array([[3, 1], [1, 2]])
B = np.array([9, 8])
x = np.linalg.solve(A, B)
print(f"Matriks A:\n{A}")
print(f"Vektor B:\n{B}")
print(f"Hasil x (solusi Ax = B):\n{x}")
# Output:
# [2. 3.]

print(f"\n Jejak Matriks (np.trace)")
# Menghitung jumlah elemen diagonal utama dari matriks
a = np.array([[1, 2], [3, 4]])
trace_a = np.trace(a)
print(f"Matriks a:\n{a}")
print(f"Jejak matriks (trace): {trace_a}")
# Output:
# 5

print(f"\n Norma Matriks (np.linalg.norm)")
# Menghitung norma (panjang) dari matriks
a = np.array([[1, 2], [3, 4]])
norm_a = np.linalg.norm(a)
print(f"Matriks a:\n{a}")
print(f"Norma matriks: {norm_a}")
# Output:
# 5.477225575051661

print(f"\n Perkalian Luar (np.outer)")
# Menghitung perkalian luar (outer product) dari dua vektor
a = np.array([1, 2])
b = np.array([3, 4])
outer = np.outer(a, b)
print(f"Vektor a: {a}")
print(f"Vektor b: {b}")
print(f"Perkalian luar (outer product):\n{outer}")
# Output:
# [[3 4]
#  [6 8]]

print(f"\n Perkalian Dalam (np.inner)")
# Menghitung perkalian dalam (inner product) dari dua vektor
a = np.array([1, 2])
b = np.array([3, 4])
inner = np.inner(a, b)
print(f"Vektor a: {a}")
print(f"Vektor b: {b}")
print(f"Perkalian dalam (inner product): {inner}")
# Output:
# 11

print(f"\n Dekomposisi QR (np.linalg.qr)")
# Menghitung dekomposisi QR dari matriks
a = np.array([[1, 2], [3, 4]])
q, r = np.linalg.qr(a)
print(f"Matriks a:\n{a}")
print(f"Matriks Q:\n{q}")
print(f"Matriks R:\n{r}")
# Output:
# Q dan R adalah hasil dekomposisi QR

print(f"\n Dekomposisi Nilai Singular (np.linalg.svd)")
# Menghitung dekomposisi nilai singular (Singular Value Decomposition, SVD)
a = np.array([[1, 2], [3, 4]])
u, s, vh = np.linalg.svd(a)
print(f"Matriks a:\n{a}")
print(f"Matriks U:\n{u}")
print(f"Nilai singular (S): {s}")
print(f"Matriks Vh:\n{vh}")
# Output:
# U, S, dan Vh adalah hasil dekomposisi SVD

print(f"\n Matriks Identitas (np.identity)")
# Membuat matriks identitas
identity = np.identity(3)
print(f"Matriks identitas 3x3:\n{identity}")
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

print(f"\n Matriks Diagonal (np.diag)")
# Membuat matriks diagonal atau mengambil elemen diagonal dari matriks
a = np.array([[1, 2], [3, 4]])
diag = np.diag(a)
print(f"Matriks a:\n{a}")
print(f"Elemen diagonal dari matriks a: {diag}")
# Output:
# [1 4]