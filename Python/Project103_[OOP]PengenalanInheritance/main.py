# pengenalan inheritance
class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
# sub class
class Hero_intelligent(Hero):
    pass

class Hero_spedd(Hero):
    pass
        
lina = Hero("Lina", 100)
ucup = Hero_intelligent('ucup', 100) # sekarang ucup punya nama yang diturunkan dari Hero class

print(ucup.__dict__)
