
class BerisDeret():
    def __init__(self):
        pass

    def barisan_Aritmatika(self):
        num1 = input("Masukan angka: ")
        if num1.isdigit() or num1.count('.') == 1:
            num1 = float(num1)
            
        else:
            print("Input tidak valid!")
            return False