import numpy as np
import matplotlib.pyplot as plt

# 1. Mendefinisikan fungsi parametrik
def x_folium(t):
    """Menghitung koordinat x dari Folium of Descartes."""
    return (3 * t) / (1 + t**3)

def y_folium(t):
    """Menghitung koordinat y dari Folium of Descartes."""
    return (3 * t**2) / (1 + t**3)

# 2. Membuat tiga domain t yang terpisah untuk menghindari t = -1
# Epsilon kecil digunakan untuk menjauh dari diskontinuitas t=-1
epsilon = 1e-5
num_points = 500  # Jumlah titik untuk setiap cabang

# Bagian 1: Sayap atas (Kuadran II)
t_wing_upper = np.linspace(-100, -1 - epsilon, num_points)

# Bagian 2: Sayap bawah (Kuadran IV)
t_wing_lower = np.linspace(-1 + epsilon, 0, num_points)

# Bagian 3: Loop (Kuadran I)
t_loop = np.linspace(0, 100, num_points)

# 3. Menghitung nilai x dan y untuk setiap bagian
x1, y1 = x_folium(t_wing_upper), y_folium(t_wing_upper)
x2, y2 = x_folium(t_wing_lower), y_folium(t_wing_lower)
x3, y3 = x_folium(t_loop), y_folium(t_loop)

# 4. Memplot setiap bagian secara terpisah pada grafik yang sama
plt.figure(figsize=(8, 7))
# Menggunakan satu warna (misal 'b' untuk biru) dan tidak ada label terpisah
# untuk meniru plot tunggal pada Gambar 3.1.3(a)
plt.plot(x1, y1, 'b-')
plt.plot(x2, y2, 'b-')
plt.plot(x3, y3, 'b-')

# 5. Mengatur plot agar sesuai dengan Gambar 3.1.3(a)
plt.title('Folium of Descartes: $x^3 + y^3 = 3xy$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)

# Menetapkan batas yang mirip dengan gambar di materi
plt.xlim(-3.5, 3.5)
plt.ylim(-4.5, 2.5)

# Memastikan rasio aspek sama agar kurva tidak terdistorsi
plt.gca().set_aspect('equal', adjustable='box')
plt.show()