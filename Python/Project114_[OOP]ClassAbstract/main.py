from abc import ABC,abstractmethod

# mendeklarasikan
class Kendaraan(ABC):
    @abstractmethod
    def bergerak(self):
        pass # tanpa objek apapun
    
    
# wajib pakai sub class kalo objeknya mau di panggil
# ini adalah class pewaris
class Mobil(Kendaraan):
    def bergerak(self):
        print(f"Mobil bergerak dengan empat roda")

class Kereta(Kendaraan):
    def bergerak(self):
        print(f"Kereta bergerak dengan empat baja")

# cara pemanggilan 
mobil = Mobil()
mobil.bergerak()

kereta = Kereta()
kereta.bergerak()