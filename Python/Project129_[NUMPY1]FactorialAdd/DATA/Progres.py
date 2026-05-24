import math
# import numpy as np
# from . import User
# from .User import kalkulator_biasa, kalkulator_Trinogo

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
    
    
class TrinogomeOpsi:
    def sisiC(): # 1
        result = None  # Tempat menyimpan hasil perhitungan
        a = float(input("Masukkan sisi a (tinggi): "))
        b = float(input("Masukkan sisi b (alas): "))
        result = TrigonometryBasic.sisi_c(a, b)  # c = sqrt(a^2 + b^2)
        print(f"Hasil sisi c = {result:.2f}")
        return result
    
    def sisiB(): # 2
        result = None  # Tempat menyimpan hasil perhitungan
        c = float(input("Masukkan sisi c (miring): "))
        a = float(input("Masukkan sisi a (tinggi): "))
        result = TrigonometryBasic.sisi_b(c, a)  # b = sqrt(c^2 - a^2)
        print(f"Hasil sisi b = {result:.2f}")
        
    def sisiA(): # 3
        result = None
        c = float(input("Masukkan sisi c (miring): "))
        b = float(input("Masukkan sisi b (alas): "))
        result = TrigonometryBasic.sisi_a(c, b)  # a = sqrt(c^2 - b^2)
        print(f"Hasil sisi a = {result:.2f}")
        
    def cDaria(): # 4
        a = float(input("Masukkan sisi a (tinggi): "))
        alpha_deg = float(input("Masukkan sudut alpha (dalam derajat): "))
        alpha_rad = Trigonometry.to_radians(alpha_deg)
        result = TrigonometryBasic.c_dari_a_dan_sin_alpha(a, alpha_rad)  # c = a / sin(alpha)
        print(f"Hasil sisi c = {result:.2f}")
    

    def cDariBdanCosAlpha(): # 5
        b = float(input("Masukkan sisi b (alas): "))
        alpha_deg = float(input("Masukkan sudut alpha (dalam derajat): "))
        alpha_rad = Trigonometry.to_radians(alpha_deg)
        result = TrigonometryBasic.c_dari_b_dan_cos_alpha(b, alpha_rad)
        print(f"Hasil sisi c = {result:.2f}")

    def aDariCdanSinAlpha():  # 6
        c = float(input("Masukkan sisi c (miring): "))
        alpha_deg = float(input("Masukkan sudut alpha (dalam derajat): "))
        alpha_rad = Trigonometry.to_radians(alpha_deg)
        result = TrigonometryBasic.a_dari_c_dan_sin_alpha(c, alpha_rad)
        print(f"Hasil sisi a = {result:.2f}")

    def aDariBdanTanAlpha():  # 7
        b = float(input("Masukkan sisi b (alas): "))
        alpha_deg = float(input("Masukkan sudut alpha (dalam derajat): "))
        alpha_rad = Trigonometry.to_radians(alpha_deg)
        result = TrigonometryBasic.a_dari_b_dan_tan_alpha(b, alpha_rad)
        print(f"Hasil sisi a = {result:.2f}")

    def bDariCdanCosAlpha():  # 8
        c = float(input("Masukkan sisi c (miring): "))
        alpha_deg = float(input("Masukkan sudut alpha (dalam derajat): "))
        alpha_rad = Trigonometry.to_radians(alpha_deg)
        result = TrigonometryBasic.b_dari_c_dan_cos_alpha(c, alpha_rad)
        print(f"Hasil sisi b = {result:.2f}")

    def bDariAdanTanAlpha():  # 9
        a = float(input("Masukkan sisi a (tinggi): "))
        alpha_deg = float(input("Masukkan sudut alpha (dalam derajat): "))
        alpha_rad = Trigonometry.to_radians(alpha_deg)
        result = TrigonometryBasic.b_dari_a_dan_tan_alpha(a, alpha_rad)
        print(f"Hasil sisi b = {result:.2f}")

    def alphaDariAC():  # 10
        a = float(input("Masukkan sisi a (tinggi): "))
        c = float(input("Masukkan sisi c (miring): "))
        result_rad = TrigonometryBasic.alpha_dari_a_c(a, c)
        result = Trigonometry.to_degrees(result_rad)
        print(f"Sudut alpha = {result:.2f}°")

    def alphaDariBC():  # 11
        b = float(input("Masukkan sisi b (alas): "))
        c = float(input("Masukkan sisi c (miring): "))
        result_rad = TrigonometryBasic.alpha_dari_b_c(b, c)
        result = Trigonometry.to_degrees(result_rad)
        print(f"Sudut alpha = {result:.2f}°")

    def alphaDariAB():  # 12
        a = float(input("Masukkan sisi a (tinggi): "))
        b = float(input("Masukkan sisi b (alas): "))
        result_rad = TrigonometryBasic.alpha_dari_a_b(a, b)
        result = Trigonometry.to_degrees(result_rad)
        print(f"Sudut alpha = {result:.2f}°")

# import numpy as np
# class Matrixs:
#     def matrix_pangkat_costum():
#         opsi_ordo = input("Masukan Ordo Matrix (2x2, 3x3, 4x4): ")
#         match opsi_ordo:
#             case "2x2":
#                 print("Masukan input E.X (1234) => (12) Baris pertama. (34) Baris kedua ")
#                 a = input("Masukan input: ")
#                 pangkat = input("Masukan pangkat matrix: ")
#                 if len(a) == 4 and a.isdigit() and pangkat.isdigit():
#                     data = [int(x) for x in a]          # Jadi [1, 1, 1, 1]
#                     matriks2 = np.array(data).reshape(2, 2)  # Jadi [[1 1], [1 1]]
#                     pangkat2 = int(pangkat)
#                     print(f"Hasil = \n{matriks2**pangkat2}")
#                 else:
#                     print("Input harus 4 digit untuk ordo 2x2")
                