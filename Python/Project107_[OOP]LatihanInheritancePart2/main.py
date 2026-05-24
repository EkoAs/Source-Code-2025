from data import Hero, BestHero, IntellegentHero
from data.daftarHero import inputUS

# Contoh pembuatan hero manual (bisa dihapus jika tidak perlu)
# lina = Hero("lina")
# ucup = BestHero("ucup")
# rayn = IntellegentHero("rayn")

# rayn.info()
# lina.exp = 300
# lina.info()

while True:
    hero1, hero2 = inputUS()
    print("\nHero 1:", hero1.info())
    print("Hero 2:", hero2.info())

    # Pertarungan
    while hero1.health > 0 and hero2.health > 0:
        hero1.serang(hero2)
        if hero2.health <= 0:
            print(f"{hero2.name} Kalah!")
            break
        hero2.serang(hero1)
        if hero1.health <= 0:
            print(f"{hero1.name} Kalah!")
            break

    print(f"\n{'='*10} Info Akhir Kedua Hero {'='*10}")
    print(hero1.info())
    print(hero2.info())

    play_again = input("Ingin bermain lagi? (y/n): ")
    if play_again.lower() != 'y':
        break

