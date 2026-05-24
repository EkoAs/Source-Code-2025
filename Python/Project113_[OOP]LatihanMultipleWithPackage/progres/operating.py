import math

class Math:
    def add(num1:float,num2:float):
        return num1+num2
    def min(num1:float,num2:float):
        return num1-num2
    def bagi(num1:float,num2:float):
        return num1/num2
    def kali(num1:float,num2:float):
        return num1*num2
    def pangkat(num1:float,num2:float):
        return num1**num2
    def modulus(num1:float,num2:float):
        return num1%num2
    
class Trigonometry:
    pi = math.pi
    @staticmethod
    def to_degrees(radians):
        return math.degrees(radians)
    @staticmethod
    def to_radians(degrees):
        return math.radians(degrees)
class TrigonometryBasic(Trigonometry):
    @staticmethod
    def sisi_c(a, b):
        return math.sqrt(a**2 + b**2)
    @staticmethod
    def sisi_a(c, b):
        return math.sqrt(c**2 - b**2)
    @staticmethod
    def sisi_b(c, a):
        return math.sqrt(c**2 - a**2)
    @staticmethod
    def c_dari_a_dan_sin_alpha(a, alpha_rad):
        return a / math.sin(alpha_rad)
    @staticmethod
    def c_dari_b_dan_cos_alpha(b, alpha_rad):
        return b / math.cos(alpha_rad)
    @staticmethod
    def a_dari_c_dan_sin_alpha(c, alpha_rad):
        return c * math.sin(alpha_rad)
    @staticmethod
    def a_dari_b_dan_tan_alpha(b, alpha_rad):
        return b * math.tan(alpha_rad)
    @staticmethod
    def b_dari_c_dan_cos_alpha(c, alpha_rad):
        return c * math.cos(alpha_rad)
    @staticmethod
    def b_dari_a_dan_tan_alpha(a, alpha_rad):
        return a / math.tan(alpha_rad)
    @staticmethod
    def alpha_dari_a_c(a, c):
        return math.asin(a / c)

    @staticmethod
    def alpha_dari_b_c(b, c):
        return math.acos(b / c)

    @staticmethod
    def alpha_dari_a_b(a, b):
        return math.atan(a / b) 
    
class BangunRuang():
    def bangunruang():
        volumeBalok = lambda panjang, lebar, tinggi:panjang*lebar*tinggi
        kelilingBalok = lambda panjang, lebar:(panjang+lebar)*2
        luasBalok = lambda panjang, lebar:panjang*lebar
        return volumeBalok, kelilingBalok, luasBalok
            
    
    
    
    
    