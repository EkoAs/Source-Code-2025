import numpy as np
import matplotlib.pyplot as plt

# 1. Tentukan rentang parameter 't' untuk setiap cabang
# Kita mengecualikan t = -1 secara numerik
t_wing1 = np.linspace(-50, -1.01, 200)   # Sayap kanan-bawah
t_wing2 = np.linspace(-0.99, -0.01, 200)  # Sayap kiri-atas
t_loop = np.linspace(0, 50, 400)      # Simpul (Loop)

# 2. Gabungkan rentang t, dipisahkan oleh 'nan' untuk memutus garis
# Ini adalah teknik profesional untuk memplot fungsi terputus-putus
t = np.concatenate((t_wing1, [np.nan], t_wing2, [np.nan], t_loop))

# 3. Hitung x(t) dan y(t) menggunakan rumus parametrik (a=1)
x = (3 * t) / (1 + t**3)
y = (3 * t**2) / (1 + t**3)

# 4. Konfigurasi plot agar sesuai dengan buku teks
plt.figure(figsize=(6, 6))
ax = plt.gca()

# Plot kurva folium
plt.plot(x, y, 'b-', label=r'$x^3 + y^3 = 3xy$') # 'b-' untuk garis biru

# Atur sumbu agar berpotongan di (0,0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Atur panah di ujung sumbu
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Atur label sumbu
ax.set_xlabel('x', loc='right')
ax.set_ylabel('y', loc='top', rotation=200)

# Atur batas plot dan tick
ax.set_xticks(np.arange(-3, 3, 1))
ax.set_yticks(np.arange(-3, 3, 1))
ax.set_xlim(-3.5, 2.5)
ax.set_ylim(-4.5, 2.5)

plt.title("Replikasi Gambar 3.1.3(a): Folium of Descartes (Parametrik)")
plt.grid(False) # Sesuai gambar, tidak ada grid
plt.show()