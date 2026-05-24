import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def analisis_dan_plot_folium():
    """
    Fungsi komprehensif untuk menghitung, memisahkan, dan memplot Folium of Descartes
    berdasarkan metode dekomposisi fungsi kubik analitik.
    Menghasilkan visualisasi Figure 3.1.3c dan data tabel.
    """
    
    # ---------------------------------------------------------
    # 1. Konfigurasi Parameter dan Domain
    # ---------------------------------------------------------
    a = 1.0  # Parameter skala kurva
    
    # Menghitung batas x untuk tangen vertikal (x_vt)
    # Rumus: x_vt = a * 4^(1/3)
    x_vt = a * (4**(1/3))
    
    # Membuat array x dari 0 hingga x_vt
    # Kita menggunakan linspace dengan kerapatan tinggi untuk kehalusan kurva
    # epsilon ditambahkan pada start untuk menghindari div-by-zero di turunan jika diperlukan,
    # namun solusi analitik aman di 0. Kita mulai dari 0.
    N_points = 1000
    x = np.linspace(0, x_vt, N_points)
    
    # ---------------------------------------------------------
    # 2. Solver Persamaan Kubik (Metode Trigonometri)
    # ---------------------------------------------------------
    # Persamaan: y^3 - 3axy + x^3 = 0
    # Bentuk Depressed: y^3 + py + q = 0
    # p = -3ax, q = x^3
    
    # Menghitung p dan q untuk setiap x
    p = -3 * a * x
    q = x**3
    
    # Masking untuk x=0 guna menghindari warning pada pembagian, meskipun limit valid
    # Kita akan menangani x=0 secara terpisah atau menggunakan np.where
    safe_x = np.where(x == 0, 1e-9, x) # hindari 0 untuk pembagi
    
    # Rumus Vieta untuk 3 akar real (kasus Discriminant <= 0)
    # Faktor Skala R = 2 * sqrt(-p/3) = 2 * sqrt(ax)
    R = 2 * np.sqrt(a * safe_x)
    
    # Argumen Arccos (Psi)
    # Psi = -0.5 * (x/a)^(1.5)
    Psi = -0.5 * ((safe_x / a)**1.5)
    
    # Penanganan Stabilitas Numerik: Clamping argumen ke [-1, 1]
    # Di ujung loop (x_vt), Psi teoritis adalah -1. Float error bisa membuatnya -1.0000001
    Psi = np.clip(Psi, -1.0, 1.0)
    
    # Menghitung sudut theta dasar
    theta = np.arccos(Psi) / 3.0
    
    # Menghitung ketiga akar (k=0, 1, 2)
    root0 = R * np.cos(theta)
    root1 = R * np.cos(theta - 2*np.pi/3)
    root2 = R * np.cos(theta - 4*np.pi/3)
    
    # ---------------------------------------------------------
    # 3. Logika Pemisahan Sayap (Segmentation Logic)
    # ---------------------------------------------------------
    # Pada setiap x, kita memiliki 3 akar.
    # Salah satunya negatif (Lengan kuadran 4) -> Abaikan.
    # Dua lainnya positif (Bagian Loop).
    # Dari dua positif: Yang Besar = Sayap Atas, Yang Kecil = Sayap Bawah.
    
    y_upper = np.zeros_like(x)
    y_lower = np.zeros_like(x)
    
    # Iterasi untuk sorting (bisa di-vectorize tapi loop lebih eksplisit untuk logika)
    for i in range(N_points):
        roots = np.array([root0[i], root1[i], root2[i]])
        
        # Filter akar positif (dengan toleransi kecil untuk 0)
        pos_roots = roots[roots > -1e-6]
        
        # Sorting
        pos_roots = np.sort(pos_roots)
        
        # Assign ke array
        # Jika x=0, semua akar 0.
        if len(pos_roots) >= 2:
            y_lower[i] = pos_roots # Terkecil positif
            y_upper[i] = pos_roots[-1] # Terbesar positif
        elif len(pos_roots) == 1:
            # Kasus di ujung tangen vertikal dimana akar ganda
            y_lower[i] = pos_roots
            y_upper[i] = pos_roots
        else:
            y_lower[i] = 0
            y_upper[i] = 0
            
    # Memastikan nilai di x=0 tepat 0
    y_upper = 0
    y_lower = 0

    # ---------------------------------------------------------
    # 4. Visualisasi (Matplotlib)
    # ---------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot Sayap Atas (Orange)
    ax.plot(x, y_upper, color='#ff7f0e', linewidth=2.5, label='Sayap Atas (Upper Wing)')
    
    # Plot Sayap Bawah (Biru)
    ax.plot(x, y_lower, color='#1f77b4', linewidth=2.5, label='Sayap Bawah (Lower Wing)')
    
    # Plot Garis Tangen Vertikal
    ax.axvline(x=x_vt, color='black', linestyle='--', alpha=0.5, label='Vertical Tangent Split')
    
    # Plot Titik Temu (Singularitas Tangen)
    y_vt = a * (2**(1/3))
    ax.scatter([x_vt], [y_vt], color='red', s=50, zorder=5)
    ax.text(x_vt + 0.05, y_vt, f'Tangent\n({x_vt:.2f}, {y_vt:.2f})', verticalalignment='center')
    
    # Kosmetik Grafik sesuai Figure 3.1.3c
    ax.set_title(f'Figure 3.1.3c: Folium of Descartes (a={a})\nFunctional Separation at Vertical Tangent', fontsize=14)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.legend(loc='upper right', frameon=True, shadow=True)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_aspect('equal') # Penting untuk geometri akurat
    
    # Batas axis untuk fokus pada loop
    ax.set_xlim(-0.1, x_vt + 0.5)
    ax.set_ylim(-0.1, x_vt + 0.5)
    
    plt.tight_layout()
    plt.show()
    
    # ---------------------------------------------------------
    # 5. Generasi Data Tabel (Excel Export Simulation)
    # ---------------------------------------------------------
    # Membuat DataFrame untuk representasi tabel
    df = pd.DataFrame({
        'X': x,
        'Y_Upper_Orange': y_upper,
        'Y_Lower_Blue': y_lower,
        'Discriminant_Check': (x**3/4) * (x**3 - 4*(a**3)), # Validasi Delta < 0
        'Theoretical_X_VT': np.full_like(x, x_vt)
    })
    
    # Menampilkan 10 baris data sampel (sekitar titik tengah dan ujung)
    sample_indices = np.linspace(0, N_points-1, 10, dtype=int)
    print("Data Tabel Sampel (Excel Preview):")
    print(df.iloc[sample_indices].to_markdown(index=False, floatfmt=".4f"))

    # Instruksi: Untuk menyimpan ke Excel, user bisa menggunakan df.to_excel('folium_data.xlsx')
    return df

if __name__ == "__main__":
    df_result = analisis_dan_plot_folium()