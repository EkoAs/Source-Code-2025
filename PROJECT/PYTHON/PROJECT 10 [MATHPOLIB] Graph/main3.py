import numpy as np
import matplotlib.pyplot as plt

# 1. Mendefinisikan fungsi parametrik
def x_folium(t): #kordinat x
    return (3 * t) / (1 + t**3)

def y_folium(t): #kordinat Y
    return (3 * t**2) / (1 + t**3)

# 2. Menyiapkan 4 domain parameter 't' untuk menghindari asimtot di t = -1
# dan untuk memisahkan loop di t = 1
epsilon = 1e-5  # Nilai kecil untuk menghindari t = -1
num_points = 500

# Rentang t untuk setiap bagian
t_sayap_atas = np.linspace(-10, -1 - epsilon, num_points)
t_sayap_bawah = np.linspace(-1 + epsilon, 0, num_points)
t_loop_bawah = np.linspace(0, 100, num_points)
t_loop_atas = np.linspace(1, 100, num_points)

# 3. Menghitung nilai x dan y untuk setiap bagian
# Bagian Cabang ATAS (Oranye/Biru)
x_sayap_atas, y_sayap_atas = x_folium(t_sayap_atas), y_folium(t_sayap_atas)
x_loop_atas, y_loop_atas = x_folium(t_loop_atas), y_folium(t_loop_atas)

# Bagian Cabang BAWAH (Ungu)
x_sayap_bawah, y_sayap_bawah = x_folium(t_sayap_bawah), y_folium(t_sayap_bawah)
x_loop_bawah, y_loop_bawah = x_folium(t_loop_bawah), y_folium(t_loop_bawah)

# 4. Memplot grafik dengan warna yang diminta
plt.figure(figsize=(8, 7))

# Plot Cabang ATAS (Anda bisa ganti 'orange' dengan 'blue' agar sama persis dengan gambar)
plt.plot(x_sayap_atas, y_sayap_atas, color='orange', label='Cabang Atas (Sayap Atas)')
plt.plot(x_loop_atas, y_loop_atas, color='orange', label='Cabang Atas (Loop Atas)')

# Plot Cabang BAWAH (Ungu)
plt.plot(x_sayap_bawah, y_sayap_bawah, color='purple', label='Cabang Bawah (Sayap Bawah)')
plt.plot(x_loop_bawah, y_loop_bawah, color='purple', label='Cabang Bawah (Loop Bawah)')

# 5. Mengatur plot agar sesuai dengan Gambar 3.1.3(b)
plt.title('Analisis Gambar 3.1.3(b): Dua Cabang Fungsi', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)

# Menetapkan batas x y garis
plt.xlim(-3.5, 3.5)
plt.ylim(-4.5, 2.5)

# cekk rasio aspek
plt.gca().set_aspect('equal', adjustable='box')
plt.show()