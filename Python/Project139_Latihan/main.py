# Tugas 2. Biodata Pribadi
def information():

    nama = input("Masukan nama: ")
    while True:
        nim = input("Masukan nama: ")
        if nim.isdigit() and len(nim) == 9:
            break
        else:
            print(f"Nim harus 9 digit angka.")
    while True:
        jurusan = input("Masukan jurusan: (informatika/mesin/industri) ")
        if jurusan.isalpha():
            if jurusan.lower() == "informatika" or jurusan.lower() == "mesin" or jurusan.lower()=="industri":
                break
            else:
                print(f"Jurusan tak ada dalam daftar")
        else:
            print(f"Jurusan harus berupa huruf")
    gender = input("Masukan jenis kelamin: (L/P) ")
    # tempat tgl lahir
    ttl = input("Masukan tempat lahir: ")
    while True:
        tgl_lahir = input("Masukan tanggal lahir (dd-mm-yyyy): ")
        if len(tgl_lahir) == 10 and tgl_lahir[2] == '-' and tgl_lahir[5] == '-':
            if tgl_lahir[:2].isdigit() and tgl_lahir[3:5].isdigit() and tgl_lahir[6:].isdigit():
                break
            else:
                print(f"Tanggal lahir harus berupa angka")
        else:
            print(f"Format tanggal salah, gunakan dd-mm-yyyy")
        
    alamat = input("Masukan alamat: ")
    while True:
        no_hp = input("Masukan nomor handphone: ")
        if no_hp.isdigit() and len(no_hp) == 12:
            break
        else:
            print(f"Nomor handphone harus 12 digit angka")
    hobi = input("Masukan hobi: ")
    asal_sekolah = input("Masukan sekolah asal: ")

    return nama, nim, jurusan, gender, ttl, tgl_lahir, alamat, no_hp, hobi, asal_sekolah

nama, nim, jurusan, gender, ttl, tgl_lahir, alamat, no_hp, hobi, asal_sekolah = information()
print(f"\nNama: {nama}")
print(f"NIM: {nim}")
print(f"Jurusan: {jurusan}")
print(f"Jenis Kelamin: {gender}")
print(f"Tempat Tanggal Lahir: {ttl}, {tgl_lahir}")
print(f"Alamat: {alamat}")
print(f"Nomor Handphone: {no_hp}")
print(f"Hobi: {hobi}")
print(f"Sekolah Asal: {asal_sekolah}")