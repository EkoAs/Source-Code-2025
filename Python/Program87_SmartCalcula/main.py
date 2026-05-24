# smart calculator

print(f"Modern Calculator. Use '2x2' to works")

userInput = input("Masukan Angka : ")
if len(userInput) == 3:
    num1 = int(userInput[0])
    num2 = int(userInput[2])
    operator = str(userInput[1])

    class math:
        @staticmethod
        def tambah(num1, num2):
            return num1 + num2
        @staticmethod
        def kurang(num1, num2):
            return num1 - num2
        @staticmethod
        def kali(num1, num2):
            return num1 * num2
        @staticmethod
        def bagi(num1, num2):
            if num1 != 0 or num2 != 0:
                return num1 / num2
            else:
                return "Hasil error karena ada 0"
        @staticmethod
        def modulus(num1, num2):
            return num1 % num2
        @staticmethod
        def pangkat(num1, num2):
            return num1 ** num2        
            
    if operator.lower() == '+':
        result = math.tambah(num1, num2)
    elif operator.lower() == '-':
        result = math.kurang(num1,num2)
    elif operator.lower() == 'x':
        result = math.kali(num1,num2)        
    elif operator.lower() == '/':
        result = math.bagi(num1,num2)        
    elif operator.lower() == '%':
        result = math.modulus(num1,num2)        
    elif operator.lower() == 'xx':
        result = math.pangkat(num1,num2)      
    else:
        print(f"Masukan operator +,-,x,/,%,xx")
        
    print(f"Hasil = {result}")
else: 
    print(f"Jumlah tidak sesuai")       


        
        
        
        
        
        
        