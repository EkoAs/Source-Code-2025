import datetime
import os
import string
import random
os.system("cls")
data_siswa = []
while True:
    templateSiswa = {
        'nama': 'nama',
        'nisn': 'nisn',
        'kelas': 'kelas',
        'nilai': 0,
        'status': 'status',
        'tanggal':'tanggal'
    }
    KEY = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    templateSiswa['id'] = KEY
    siswa  = dict.fromkeys(templateSiswa.keys(), None)

    print(f"{'SELAMAT DATANG DI FORMULIR':^40}")
    print(f"{'DATA SISWA':^40}")
    print(f"{'-'*40}\n")
    siswa['nama'] = str(input("Masukan Nama Siswa: "))
    siswa['nisn'] = str(input("Masukan Nisn SIswa: "))
    siswa['kelas'] = str(input("Masukan Kelas SIswa: "))
    siswa['nilai'] = int(input("Masukan Nilai Siswa: "))
    tanggal = int(input("Masukan tanggal Lahir(1-31):"))
    bulan = int(input("Masukan Bulaln Lahir(1-12):"))
    tahun = int(input("Masukan Tahun Lahir(1900-2025):"))
    siswa['tanggal'] = datetime.date(tahun, bulan, tanggal)
    # siswa['tanggal'] = datetime.date(tahun, bulan, tanggal)
    siswaStatus = str(input("Masukan Status Siswa: "))
    if siswaStatus.lower() == 'lulus':
        siswa['status'] = 'Lulus'
    else:
        siswa['status'] = 'Tidak Lulus'
    data_siswa.append(siswa)
    end = str(input("Apakah anda ingin mengisi data siswa lagi? (y/n): "))
    if end.lower() == 'n':
        break
    
    
print(f"{'DATA SISWA':^60}")
print(f"{'-'*60}")
print(f"{'KEY':^7} {'NISN':^6} {'NAMA':^14} {'NISN':^6} {'KELAS':^6} {'NILAI':^8} {'TAHUN LAHIR':^10} {'LULUS':^8}")
print(f"{'-'*60}")
for allSiswa in data_siswa:
    NAMA = allSiswa['nama']
    KELAS = allSiswa['kelas']
    TANGGAL = allSiswa['tanggal'].strftime('%x')
    NISN = allSiswa['nisn']
    NILAI = allSiswa['nilai']
    LULUS = allSiswa['status']  
    print(f"{KEY:^7} {NISN:^6} {NAMA:^14} {NISN:^6} {KELAS:^6} {NILAI:^8} {TANGGAL:^10} {LULUS:^8}")
    



















