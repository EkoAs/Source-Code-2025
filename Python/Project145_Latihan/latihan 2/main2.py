class Fungsi:
    def __init__(self,num1 = 0,num2=0,num3=0,kalimat=None,kalimat2=None):
        self.num1= num1
        self.num2= num2
        self.num3 = num3
        self.kalimat = kalimat
        self.kalimat2 = kalimat2
        
    def calls(self):
        print(f"{self.num1}, {self.num2}, {self.num3}, {self.kalimat}, {self.kalimat2}")
    
    def user_input(self):
        self.num1 = int(input("Masukkan angka pertama: "))
        self.num2 = int(input("Masukkan angka kedua: "))
        print(f"Angka yang dimasukkan: {self.num1} dan {self.num2}")
        Fungsi.luas(self)
        return self.num1, self.num2
    
    def luas(self):
        print(f"{self.num1} x {self.num2} = ", end="")
        return self.num1 * self.num2
    
    def nilai(self):
        nama = input("masukan nama: ")
        user= int(input("Masukkan nilai Anda: "))
        if user >= 85:
            self.num3 = user
            self.kalimat2 = "A"
        elif user >= 70 and user <=84:
            self.num3 = user
            self.kalimat2 = "B"
        elif user >= 55 and user <=69:
            self.num3 = user
            self.kalimat2 = "C"
        elif user >= 40 and user <=54:
            self.num3 = user
            self.kalimat2 = "D"
        else:
            self.num3 = user
            self.kalimat2 = "A++"
        
        self.kalimat = nama
        Fungsi.cetak(self)
        
    def cetak(self):
        print(f"Nama : {self.kalimat}")
        print(f"nilai : {self.num3}")
        print(f"Grade: {self.kalimat2}")
        
    def belanja(self):
        total_belanja = int(input("Masukan jumlah: "))
        total_belanja = float(total_belanja)
        if total_belanja > 500000:
            diskon = 0.20
            total_belanja *= diskon
            self.num1 = total_belanja
        elif total_belanja >= 210000 and total_belanja <= 500000:
            diskon = 0.15
            total_belanja *= diskon
            self.num1 = total_belanja
        elif total_belanja >= 210000 and total_belanja <= 500000:
            diskon = 0.10
            total_belanja *= diskon
            self.num1 = total_belanja
            
        
        print(f"total belanja anda adalah {self.num1}")
            
        
        
            
            
        
    
    
# objek = Fungsi(10,20,30,"Halo","Dunia")
# objek.calls()
objek2 = Fungsi()
objek2.belanja()


