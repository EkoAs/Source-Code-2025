# cara cepat dari sebelumnya dengan menggunakan fungsi dan __init__()
class Hero:  # ini adalah template
    def __init__(self, namaInput, healthInput, damageInput):
        self.nama = namaInput
        self.health = healthInput
        self.damage = damageInput
        return None  # __init__ adalah fungsi yang akan di eksekusi ketika objek di buat
        # self adalah objek itu sendiri, ini adalah cara untuk mengakses atribut dari objek itu sendiri
        # atau self itu bisa dikategorikan sebagai hero
        
# ini adalah objek dari kelas Hero
hero1 = Hero("ucup",1000,34)
hero2 = Hero("dafa",100,304)
hero3 = Hero("zul",100,90)
#  init akan di eksekusi setelah objek di buat




print(f'''INI ADALAH CLASS HERO DARI GAME DOTA 2'\n
      hero1 = {hero1.__dict__}\n
      hero2 = {hero2.__dict__}\n
      hero3 = {hero3.__dict__}\n
      ''')

