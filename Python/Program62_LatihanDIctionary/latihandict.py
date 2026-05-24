# Latihan input data data
dataSiswa1 = {}
while True:
    idSiswa = input("Masukan ID data(ketik exit untuk keluar)")
    if idSiswa.lower() == 'exit':
        break
    if idSiswa in dataSiswa1:
        print(f"ID {idSiswa} sudah ada, silahkan masukan ID lain")
        continue
    
    inputName = str(input("Masukan Nama Siswa :"))
    inputKelas = str(input("Masukan Kelas Siswa :"))
    
    try:
        inputNilai = int(input("Masukan Nilai Siswa :"))
    except ValueError:
        print("Nilai harus berupa angka")
        continue
    
    inputLulus = input("Masukan Kelulusan Siswa y/n :").lower().strip()
    if inputLulus == 'y':
        kelulusan = 'Lulus'
    elif inputLulus == 'n':
        Kelulusan = "Tidak Lulus"
    else :
        print(f"Masukan Y/N")
        
         
    dataSiswa1[idSiswa] = {
        'nama': inputName,
        'kelas': inputKelas,
        'nilai': inputNilai,
        'lulus': kelulusan
    }
    
    inputCountinue = str(input("jika ingin lanjut tekan y/n :"))
    if inputCountinue.lower() == 'n':
        break
    
print(f"{'NAMA':<10} {'KELAS':<8} {'NILAI':^8} {'LULUS':<10}")
print(f"{'-'*40}")

for data, id_Siswa in dataSiswa1.items():
    KEYS = data
    # ID = dataSiswa1[data][]
    NAMA = dataSiswa1[data]['nama']
    KELAS = dataSiswa1[data]['kelas']
    NILAI = dataSiswa1[data]['nilai']
    LULUS = dataSiswa1[data]['lulus']
    

    print(f"{NAMA:<10} {KELAS:<8} {NILAI:^8} {LULUS:^10} ")
# print(ID)