# Komparasi dan logika
# 0 > lebih dari, di kanan lebih besar, dan < kurang dari, di kiri lebih kecil 4 < 9
# ------0+++++++5--------8++++++11---------
inputUser = float(input("Masukan angka :\n"))
lebihDari0 = inputUser > 0 # -------------0
kurangDari5 = inputUser < 5 # +++++++++++++5
lebihDari8 = inputUser > 8 # ---------8
kurangDari11 = inputUser < 11 # +++++++11

hasilAwal = lebihDari0 and kurangDari5 
hasilAkhir = lebihDari8 and kurangDari11
hasilFInal = hasilAwal or hasilAkhir
print(lebihDari0, "dan", kurangDari5, "=", hasilAwal)
print(lebihDari8, "dan", kurangDari11, "=", hasilAkhir)
print("Hasil akhir adalah", hasilFInal)

print(10*'=', "kebalikannya", 20*'=')
#+++++++0------5++++++8-------11++++++
inputUser = float(input("Masukan nilai \n:"))
kurangDari0 = inputUser > 0  # +++++++++0
lebihdari5 = inputUser < 5 # ----------5
kurangDari8 = inputUser > 8 # ++++++++++ 8
lebihDari11 = inputUser < 11 #----------11++++++++++++
hasilAwal = kurangDari0 or lebihdari5
hasilAkhir = kurangDari8 or lebihDari11
hasilFInal = hasilAwal and hasilAkhir
print(kurangDari0, "dan", lebihdari5, "=", hasilAwal)
print(kurangDari8, "dan", lebihDari11, "=", hasilAkhir)
print("Hasil akhir adalah", hasilFInal)