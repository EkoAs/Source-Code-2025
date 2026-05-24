# latihan inheritance
# multiple inheritance

class Type:
    def type(self,type):
        self.type = type
    def info(self):
        print(f"{self.type}")
class Team:
    def  team(self,team):
        self.team = team
    def info(self):
        print(f"{self.team}")
class Hero(Type,Team):
    def __init__(self,name):
        self.name=name
    def called(self):
        print(f"Nama: {self.name}")
        print("Type:", end=" ")
        Type.info(self)
        print("Team:", end=" ")
        Team.info(self)
ucup = Hero("ucup")
ucup.team("raja")
ucup.type("red")
# print(ucup.team)
# print(ucup.type)

Hero.called(ucup)