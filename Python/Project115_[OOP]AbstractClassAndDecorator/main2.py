from abc import ABC,abstractmethod
class User(ABC):

    def __init__(self,pw):
        self.password = pw
        
    @property
    @abstractmethod
    def password(self):
        pass

    @password.setter
    @abstractmethod
    def password(self, value):
        pass

    @abstractmethod
    def login(self):
        pass
    
class Admin(User):
    def login(self):
        print(f"Login berhasil. Password: {self.password}")

    # Implementasi GETTER
    @property
    def password(self):
        return self.__pw

    # Implementasi SETTER
    @password.setter
    def password(self, value):
        self.__pw = f"hashed-{value}"  # contoh hashing/simbol keamanan
        
        
user1 = Admin("1234")
user1.login()