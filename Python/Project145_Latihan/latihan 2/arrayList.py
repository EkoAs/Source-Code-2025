import arrayList as al
import array as ar

class ARRAY:
    def __init__(value, nama=None, nilai=None, nilai2=None, hasil=None, campuran=None):
        value.nama = nama
        value.nilai = nilai
        value.nilai_akhir = nilai2
        value.hasil = hasil
        value.campuran = campuran
    

        
    def tugas_1(value):
        value.nilai = [78,85,90,67,88,92,73]
        print(f"Nilai tertinggi: {max(value.nilai) }")
        print(f"Nilai terendah: {min(value.nilai) }")
        print(f"Nilai rata-rata: {sum(value.nilai) / len(value.nilai) }")
       
        value.hasil = 0
        for i in value.nilai:
            value.hasil += i
        print(f"Rata-rata nilai: {value.hasil/len(value.nilai)}")
        
        
        value.nilai.append(900)
        print(f"Nilai setelah ditambah: {value.nilai}")
        value.nilai.remove(900)
        print(f"Nilai setelah dihapus: {value.nilai}")
        
        for i in (range(len(value.nilai))):
            if value.nilai[i] == 73:
                del value.nilai[i]
                break
        print(f"Nilai setelah dihapus: {value.nilai}")
        
    def tugas_2(value):
        value.nilai2 =[]
        jumlah = int(input("masukan panjang: "))
        for i in range(jumlah):
            data= input("masukan nilai: ")
            if data.isdigit():
                data = int(data)
                value.nilai2.append(data)
        print(f"Nilai : {value.nilai2}")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

if __name__ == "__main__":
    cetak = ARRAY()
    cetak.tugas_1()

