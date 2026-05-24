import numpy as np

a = np.array(([1,2,3],
              [4,5,6]))

# ukuran cek. pakai .shape
print(f"Matrix a ukuran {a.shape}: \n{a}")

# tranpose matrix. baris jadi kolom
print(f"\nMatrix Transpose {a.shape}: \n{a.transpose()}")
# atau np.transpose(a) atau a.T => pakai getter setter

# flatten array. vector baris
# merubah menjadi satu baris
print(f"\nMatrix vector {a.shape}: \n{a.ravel()}")
# atau np.ravel(a)


# reshape matrix. ubah jadi 3 2
print(f"\nMatrix reshape {a.shape}: \n{a.reshape(3,2)}")
print(f"Matrix reshape {a.shape}: \n{a.reshape(6,1)}")


# jadi mereka semua itu gak mengubah secara fix
# nah kalo ini bener2 dirubah permanen
print(f"\nMatrix ori {a.shape}: \n{a}")

# resize
a.resize(3,2)
print(f"\nMatrix resize {a.shape}: \n{a}")

