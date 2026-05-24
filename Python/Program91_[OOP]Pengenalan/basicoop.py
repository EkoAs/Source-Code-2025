# penenalan oop 
# kelas dan objek
# kelas adalah blueprint, cetakan, template
# objek adalah instance dari kelas,
 
'''INI ADALAH CLASS HERO DARI GAME DOTA 2'''
class Hero: # ini adalah template
    pass
hero1 = Hero(); # ini adalah objek dari kelas Hero
hero2 = Hero();

hero1.nama = "Axe" # ini adalah atribut dari objek hero1
hero1.health = 200
hero2.nama = "Ucup"
hero2.health = 10000
# cek atribut dari bobjek hero 1
print(hero1.__dict__)
print(hero2.__dict__)
# cek apakah objek atau bukan
print(hero1)

# mengambil salah satu saja
print(f"Nama hero ke satu adalah = {hero1.nama}") # ini adalah cara mengambil atribut dari objek
print(f"darah hero ke 2 adalah = {hero2.health}")