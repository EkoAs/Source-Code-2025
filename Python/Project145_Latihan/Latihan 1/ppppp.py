nama_list=[]

def masukin ():
    nama=input("Masukan nama:")
    nomor=int(input("Masukan nomor:"))
    modal=int(input("Masuan Harga:"))
    
    data={
    'nama':nama,
    'nomor':nomor,
    'modal':modal,
    }
    
    nama_list.append(data)
    print("Berhasil")
    
def tampilkan():
    for data in nama_list:
        print("Nama anda :", data['nama'])
        print("Nomor anda adalah :", data['nomor'])
        
def hitung():
    awal=0
    diskon=0
    for data in nama_list:
    if data['modal'] >= 100:
        diskon=0.10
    elif data['modal'] >= 50:
        diskon=0.05
    else :
        diskon=0
    awal = data['modal'] * diskon  
    harga = data['modal'] - awal
    
def menu():
    while(True):
        print("1. Input Data")
        print("2. Tampilkan Data")
        print("3. Menghitung Diskon")
        print("4. Keluar")
        
    input=input("Masukan nomor")
    if 
    
menu()
        
        
    
          
    