# multikey dan nesting dictionary
import datetime as dt
# multikey
mahasiswa0 = {
    'nama':'Ucup',
    'kelas':'12',
    'nilai':78,
    'lulus':True,
    'lahir':dt.date(2005, 10, 10)
}

mahasiswa1 = {
    'nama':'Otong',
    'kelas':'12',
    'nilai':70,
    'lulus':True,
    'lahir':dt.date(2007, 11, 10)
}

mahasiswa2 = {
    'nama':'Dudung',
    'kelas':'12',
    'nilai':80,
    'lulus':True,
    'lahir':dt.date(2007,8, 23)
}

mahasiswa3 = {
    'nama':'Dafa',
    'kelas':'12',
    'nilai':89,
    'lulus':True,
    'lahir':dt.date(2007, 5, 29)
}

# Nesting dicy / dict di dalam dict
dataSiswa = {
    '31357':mahasiswa0,
    '31358':mahasiswa1,
    '31359':mahasiswa2,
    '31360':mahasiswa3
}

print(f"{'NAMA':<10} {'KELAS':<8} {'NILAI':^8} {'LULUS':<10} {'LAHIR':<12}")
print(f"{'-'*50}")

for siswa in dataSiswa:
    KEY = siswa
    NAMA = dataSiswa[KEY]['nama']
    KELAS = dataSiswa[KEY]['kelas']
    NILAI = dataSiswa[KEY]['nilai']
    LULUS = dataSiswa[KEY]['lulus']
    LAHIR = dataSiswa[KEY]['lahir'].strftime('%x')

    print(f"{NAMA:<10} {KELAS:<8} {NILAI:^8} {LULUS:^10} {LAHIR:<12}")






