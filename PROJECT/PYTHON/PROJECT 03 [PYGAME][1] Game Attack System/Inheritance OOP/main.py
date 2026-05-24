from hero import Hero,BestHero,IntellegentHero
lina = Hero("lina")
ucup = BestHero("ucup")
rayn = IntellegentHero("rayn")

rayn.info()
lina.exp = 300
        
lina.info()
        
# Ketika exp dinaikkan, biasanya ada mekanisme untuk menaikkan level.
# Misal, setiap 100 exp = naik 1 level. Armor, attack, dan atribut lain bisa berubah sesuai level.
# Contoh sederhana:
lina.exp += 200  # Tambah exp
lina.info()      # Cek apakah level dan atribut berubah

ucup.exp = 500
ucup.info()