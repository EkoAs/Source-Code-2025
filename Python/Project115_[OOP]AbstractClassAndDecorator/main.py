# hubungan deckorator dgn abstrak class

from abc import ABC,abstractmethod
class Button(ABC):
    def __init__(self,setLink): # tidak abstrack method
        self.link = setLink # yg asalnya atribut jadi method karena pakai property
        
    @abstractmethod
    def click(self):
        pass
    @property
    @abstractmethod
    def link(self):
        pass
class Push(Button):
    def click(self):
        print("push button click {}".format(self.link)) # self link adalah y di bawahnya  
    
    # meng implementasikan link di sub class
    @Button.link.setter
    def link(self,input):
        self.__link = input
    
    @link.getter # tidak perlu pakai button karena di atasnya sudah ada butto nlink
    def link(self):
        return self.__link
tombol1 = Push("www.go.id")
tombol1.click()
