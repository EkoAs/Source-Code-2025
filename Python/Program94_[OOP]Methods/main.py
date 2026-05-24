# Methods
'''
macam macam method
1. Method tanpa argumen
2. Method dengan argumen
3. Method dengan return
4. Method dengan argumen dan return
'''
class Hero:
    num = 0
    def __init__(self, namaInput, healthInput, damageInput):
        self.nama = namaInput
        self.health = healthInput
        self.damage = damageInput
        Hero.num += 1
        print(f"hero ke {Hero.num} adalah {self.nama}")
        
        # tanpa argumen
    def siapa(self):
        print(f"Nama hero saya adalah {self.nama}")
            
            
    # dengan argumen 
    def upHealth(self, up):
        self.health += up
        print(f"Health {self.nama} sekarang adalah {self.health}")
            
    # dengan return
    def getDamage(self):
        return self.damage

# Membuat instance dari Hero
hero1 = Hero("Ucup", 100, 3)
hero2 = Hero("zul", 30, 45)
# Memanggil metode tanpa argumen
hero1.siapa()  # Output: Nama hero saya adalah Ucup
# Memanggil metode dengan argumen
hero1.upHealth(50)  # Output: Health Ucup sekarang adalah 150
hero2.upHealth(20)  # Output: Health zul sekarang adalah 50
# Memanggil metode dengan return
damage = hero2.getDamage()  # Menyimpan nilai damage ke dalam variabel
print(f"Damage {hero2.nama} adalah {damage}")  # Output: Damage Dafa adalah 5

print(f"hero {hero1.__dict__}\n dan hero {hero2.__dict__}")