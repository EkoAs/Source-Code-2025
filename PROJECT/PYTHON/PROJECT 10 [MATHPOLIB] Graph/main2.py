import pandas as pd
import matplotlib.pyplot as plt
import io # Modul untuk membaca string seolah-olah file

# 1. Data teks yang Anda berikan, disimpan sebagai string
# (Tanda """ di awal dan akhir membuatnya jadi satu blok teks)
data_string = """
        t      x(t)      y(t)  Unnamed: 3   t.1     x(t).1     y(t).1
0   -3.00  0.346154 -1.038462         NaN -3.00   0.346154  -1.038462
1   -2.95  0.358701 -1.058167         NaN -2.95   0.358701  -1.058167
2   -2.90  0.371970 -1.078712         NaN -2.90   0.371970  -1.078712
3   -2.85  0.386020 -1.100156         NaN -2.85   0.386020  -1.100156
4   -2.80  0.400916 -1.122566         NaN -2.80   0.400916  -1.122566
5   -2.75  0.416732 -1.146014         NaN -2.75   0.416732  -1.146014
6   -2.70  0.433549 -1.170583         NaN -2.70   0.433549  -1.170583
7   -2.65  0.451458 -1.196363         NaN -2.65   0.451458  -1.196363
8   -2.60  0.470560 -1.223456         NaN -2.60   0.470560  -1.223456
9   -2.55  0.490971 -1.251976         NaN -2.55   0.490971  -1.251976
10  -2.50  0.512821 -1.282051         NaN -2.50   0.512821  -1.282051
11  -2.45  0.536257 -1.313829         NaN -2.45   0.536257  -1.313829
12  -2.40  0.561447 -1.347473         NaN -2.40   0.561447  -1.347473
13  -2.35  0.588585 -1.383175         NaN -2.35   0.588585  -1.383175
14  -2.30  0.617892 -1.421152         NaN -2.30   0.617892  -1.421152
15  -2.25  0.649624 -1.461654         NaN -2.25   0.649624  -1.461654
16  -2.20  0.684080 -1.504975         NaN -2.20   0.684080  -1.504975
17  -2.15  0.721608 -1.551457         NaN -2.15   0.721608  -1.551457
18  -2.10  0.762620 -1.601501         NaN -2.10   0.762620  -1.601501
19  -2.05  0.807603 -1.655587         NaN -2.05   0.807603  -1.655587
20  -2.00  0.857143 -1.714286         NaN -2.00   0.857143  -1.714286
21   2.00  0.666667  1.333333         NaN -1.95   0.666667  -1.778289
22   2.05  0.639617  1.311215         NaN -1.90   0.639617  -1.848438
23   2.10  0.613975  1.289348         NaN -1.85   0.613975  -1.925773
24   2.15  0.589667  1.267784         NaN -1.80   0.589667  -2.011589
25   2.20  0.566621  1.246566         NaN -1.75   0.566621  -2.107527
26   2.25  0.544767  1.225725         NaN -1.70   0.544767  -2.215691
27   2.30  0.524037  1.205286         NaN -1.65   0.524037  -2.338834
28   2.35  0.504369  1.185266         NaN -1.60   0.504369  -2.480620
29   2.40  0.485699  1.165677         NaN -1.55   0.485699  -2.646047
30   2.45  0.467970  1.146527         NaN -1.50   0.467970  -2.842105
31   2.50  0.451128  1.127820         NaN -1.45   0.451128  -3.078894
32   2.55  0.435120  1.109555         NaN -1.40   0.435120  -3.371560
33   2.60  0.419897  1.091731         NaN -1.35   0.419897  -3.743901
34   2.65  0.405413  1.074345         NaN -1.30   0.405413  -4.235589
35   2.70  0.391626  1.057390         NaN -1.25   0.391626  -4.918033
36   2.75  0.378495  1.040860         NaN -1.20   0.378495  -5.934066
37   2.80  0.365981  1.024747         NaN -1.15   0.365981  -7.616991
38   2.85  0.354050  1.009043         NaN -1.10   0.354050 -10.966767
39   2.90  0.342668  0.993737         NaN -1.05   0.342668 -20.983347
40   2.95  0.331804  0.978822         NaN  0.00   0.000000   0.000000
41   3.00  0.321429  0.964286         NaN -0.99 -99.996633  98.996667
42    NaN       NaN       NaN         NaN -0.94 -16.645417  15.646692
43    NaN       NaN       NaN         NaN -0.89  -9.049896   8.054408
44    NaN       NaN       NaN         NaN -0.84  -6.187146   5.197203
45    NaN       NaN       NaN         NaN -0.79  -4.674916   3.693183
46    NaN       NaN       NaN         NaN -0.74  -3.732498   2.762048
47    NaN       NaN       NaN         NaN -0.69  -3.082692   2.127058
48    NaN       NaN       NaN         NaN -0.64  -2.602134   1.665366
49    NaN       NaN       NaN         NaN -0.59  -2.227477   1.314211
50    NaN       NaN       NaN         NaN -0.54  -1.922767   1.038294
51    NaN       NaN       NaN         NaN -0.49  -1.666004   0.816342
52    NaN       NaN       NaN         NaN -0.44  -1.442913   0.634882
53    NaN       NaN       NaN         NaN -0.39  -1.243780   0.485074
54    NaN       NaN       NaN         NaN -0.34  -1.061730   0.360988
55    NaN       NaN       NaN         NaN -0.29  -0.891749   0.258607
56    NaN       NaN       NaN         NaN -0.24  -0.730093   0.175222
57    NaN       NaN       NaN         NaN -0.19  -0.573937   0.109048
58    NaN       NaN       NaN         NaN -0.14  -0.421156   0.058962
59    NaN       NaN       NaN         NaN -0.09  -0.270197   0.024318
60    NaN       NaN       NaN         NaN -0.04  -0.120008   0.004800
61    NaN       NaN       NaN         NaN  0.01   0.030000   0.000300
62    NaN       NaN       NaN         NaN  0.06   0.179961   0.010798
63    NaN       NaN       NaN         NaN  0.11   0.329561   0.036252
64    NaN       NaN       NaN         NaN  0.16   0.478042   0.076487
65    NaN       NaN       NaN         NaN  0.21   0.624219   0.131086
66    NaN       NaN       NaN         NaN  0.26   0.766528   0.199297
67    NaN       NaN       NaN         NaN  0.31   0.903096   0.279960
68    NaN       NaN       NaN         NaN  0.36   1.031858   0.371469
69    NaN       NaN       NaN         NaN  0.41   1.150693   0.471784
70    NaN       NaN       NaN         NaN  0.46   1.257591   0.578492
71    NaN       NaN       NaN         NaN  0.51   1.350813   0.688915
72    NaN       NaN       NaN         NaN  0.56   1.429038   0.800261
73    NaN       NaN       NaN         NaN  0.61   1.491466   0.909794
74    NaN       NaN       NaN         NaN  0.66   1.537869   1.014993
75    NaN       NaN       NaN         NaN  0.71   1.568586   1.113696
76    NaN       NaN       NaN         NaN  0.76   1.584460   1.204190
77    NaN       NaN       NaN         NaN  0.81   1.586741   1.285260
78    NaN       NaN       NaN         NaN  0.86   1.576963   1.356188
79    NaN       NaN       NaN         NaN  0.91   1.556823   1.416709
80    NaN       NaN       NaN         NaN  0.96   1.528065   1.466943
81    NaN       NaN       NaN         NaN  1.01   1.492390   1.507313
82    NaN       NaN       NaN         NaN  1.06   1.451381   1.538464
83    NaN       NaN       NaN         NaN  1.11   1.406469   1.561181
84    NaN       NaN       NaN         NaN  1.16   1.358899   1.576323
85    NaN       NaN       NaN         NaN  1.21   1.309731   1.584775
86    NaN       NaN       NaN         NaN  1.26   1.259842   1.587401
87    NaN       NaN       NaN         NaN  1.31   1.209941   1.585023
88    NaN       NaN       NaN         NaN  1.36   1.160589   1.578401
89    NaN       NaN       NaN         NaN  1.41   1.112215   1.568223
90    NaN       NaN       NaN         NaN  1.46   1.065140   1.555104
91    NaN       NaN       NaN         NaN  1.51   1.019593   1.539585
92    NaN       NaN       NaN         NaN  1.56   0.975729   1.522137
93    NaN       NaN       NaN         NaN  1.61   0.933643   1.503166
94    NaN       NaN       NaN         NaN  1.66   0.893386   1.483021
95    NaN       NaN       NaN         NaN  1.71   0.854970   1.461999
96    NaN       NaN       NaN         NaN  1.76   0.818379   1.440348
97    NaN       NaN       NaN         NaN  1.81   0.783579   1.418278
98    NaN       NaN       NaN         NaN  1.86   0.750519   1.395965
99    NaN       NaN       NaN         NaN  1.91   0.719138   1.373554
100   NaN       NaN       NaN         NaN  1.96   0.689369   1.351164
101   NaN       NaN       NaN         NaN  2.01   0.661141   1.328893
102   NaN       NaN       NaN         NaN  2.06   0.634379   1.306820
103   NaN       NaN       NaN         NaN  2.11   0.609009   1.285009
104   NaN       NaN       NaN         NaN  2.16   0.584959   1.263512
105   NaN       NaN       NaN         NaN  2.21   0.562157   1.242367
106   NaN       NaN       NaN         NaN  2.26   0.540533   1.221604
107   NaN       NaN       NaN         NaN  2.31   0.520021   1.201248
108   NaN       NaN       NaN         NaN  2.36   0.500557   1.181313
109   NaN       NaN       NaN         NaN  2.41   0.482080   1.161812
110   NaN       NaN       NaN         NaN  2.46   0.464533   1.142750
111   NaN       NaN       NaN         NaN  2.51   0.447861   1.124131
112   NaN       NaN       NaN         NaN  2.56   0.432014   1.105955
113   NaN       NaN       NaN         NaN  2.61   0.416942   1.088219
114   NaN       NaN       NaN         NaN  2.66   0.402601   1.070920
115   NaN       NaN       NaN         NaN  2.71   0.388948   1.054050
116   NaN       NaN       NaN         NaN  2.76   0.375944   1.037605
117   NaN       NaN       NaN         NaN  2.81   0.363549   1.021574
118   NaN       NaN       NaN         NaN  2.86   0.351731   1.005950
119   NaN       NaN       NaN         NaN  2.91   0.340455   0.990723
120   NaN       NaN       NaN         NaN  2.96   0.329691   0.975884
121   NaN       NaN       NaN         NaN  3.01   0.319410   0.961423
"""

# 2. Membaca data string menggunakan pandas
# 'io.StringIO' membuat string tadi bisa dibaca seperti file
# 'delim_whitespace=True' berarti data dipisahkan oleh spasi
# 'index_col=0' berarti kolom pertama (0, 1, 2...) adalah index
data_io = io.StringIO(data_string.strip())
df = pd.read_csv(data_io, delim_whitespace=True, index_col=0)

# 3. Mengganti nama kolom yang kita butuhkan ('t.1', 'x(t).1', 'y(t).1')
df = df.rename(columns={'t.1': 't', 'x(t).1': 'x', 'y(t).1': 'y'})

# 4. Menemukan titik putus (asymptote)
# Kita cari index pertama di mana 't' mulai bernilai lebih besar dari -1
break_index = df[df['t'] > -1].index[0]

# 5. Bagi data menjadi dua bagian di titik putus itu
# iloc[:break_index] -> mengambil baris SEBELUM break_index
# iloc[break_index:] -> mengambil baris MULAI DARI break_index
df_part1 = df.iloc[:break_index] 
df_part2 = df.iloc[break_index:]

# --- Mulai Menggambar ---
plt.figure(figsize=(6, 6))

# 6. Gambar kedua bagian secara terpisah
plt.plot(df_part1['x'], df_part1['y'], label='Cabang 1 (t < -1)')
plt.plot(df_part2['x'], df_part2['y'], label='Cabang 2 (t > -1)')

# --- Atur tampilan grafik ---
plt.xlabel('x')
plt.ylabel('y')
plt.title('Folium of Descartes (dari Data Teks Anda)')
plt.xlim(-4, 4) # Atur batas sumbu x
plt.ylim(-4, 4) # Atur batas sumbu y
# plt.x
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()

# 7. Simpan gambar
plt.savefig('grafik_final_dari_teks.png')

print("Grafik yang benar telah dibuat dari data teks Anda.")
print("File disimpan sebagai 'grafik_final_dari_teks.png'")