# class variable dan instance variable
class Hero:  # ini adalah template
    num = 0 # class variable, ini adalah variable yang dimiliki oleh kelas itu sendiri
    def __init__(self, namaInput, healthInput, damageInput):
        self.nama = namaInput # self ini adalah instance variable, ini adalah variable yang dimiliki oleh objek itu sendiri
        self.health = healthInput
        self.damage = damageInput
        Hero.num += 1 # ini akan menambah jumlah hero yang dibuat
        # self adalah objek itu sendiri, ini adalah cara untuk mengakses atribut dari objek itu sendiri
        print(f"hero ke {Hero.num} adalah {self.nama}")
hero1 = Hero("ucup", 1000, 34)
hero2 = Hero("dafa", 100, 304)
print(hero1.__dict__)  # ini akan menampilkan atribut dari kelas Hero
print(hero2.__dict__)  # ini akan menampilkan atribut dari kelas Hero
        