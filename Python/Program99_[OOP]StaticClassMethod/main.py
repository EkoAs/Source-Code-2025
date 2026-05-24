# staticmethod and class method
class Hero:
    # private class vatiable
    __jumlah = 0
    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1
        
    # method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah
    # karan ada argumen self

    #  method ini gak berlaku untuk objek, tapi berlaku untuk class
    def get():
        return Hero.__jumlah
    
    # menggunakan statsic method
    # (decorator)
    @staticmethod # menandakan bahwa medhod ini static # nempel ke objek dan kelasnya
    def get():
        return Hero.__jumlah
    #  static tidak mengambil argumen
    
    @classmethod
    def get3(cls): # agar nempel ke kelas method
        return cls.__jumlah # mengubah nama class
    #  class mengabil argumen
sniper = Hero("sniper")
dam = Hero("raja")
print(sniper.get())
print(Hero.get3())