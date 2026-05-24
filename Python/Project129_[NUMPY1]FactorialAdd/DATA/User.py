
from . import Progres
from .Progres import Math
from .MatrixRumus import Matrixs,MatrixInvers,MatrixsTranspose
from .TrinogomertyR import Trigonometry, TrigonometryBasic, TrinogomeOpsi
from .FaktorialRumus import Factorial

def dataNew():
    keluhan = input("Masukan Keluhan Anda: ")
    try:
        with open("data.txt", 'r+', encding='utf-8') as file:
            file.write(keluhan)
    except:
        print(f"Update Gagal")

def kalkulator_biasa():
    print("\n",'-'*114)
    print(f"{('Masukan Operator +,-,*,/,**,%:'):^114}")
        
    operator = str(input("masukan operator: "))
    numx = input("masukan angka pertama: ")
    numy = input("masukan angka kedua: ")
    try:
        if numx.isdigit() or numx.count('.') == 1 or numy.isdigit() or numy.count('.') == 1:
            num1 = float(numx)
            num2 = float(numy) 
        else:
            print(f"kesalahan input. pastikan data harus angka dan operator harus sesuai!")
            return False
    except ValueError:
        print(f"kesalahan input. pastikan data harus angka dan operator harus sesuai!")
        return False
       
    match operator:
        case "+": print("Hasil:", Math.add(num1, num2))
        case "-": print("Hasil:", Math.min(num1, num2))
        case "/": print("Hasil:", Math.bagi(num1, num2))
        case "*": print("Hasil:", Math.kali(num1, num2))
        case "**": print("Hasil:", Math.pangkat(num1, num2))
        case "%": print("Hasil:", Math.modulus(num1, num2))
        case _: print("Operator Tidak sesuai, [+,-,*,**,/,%]")

def kalkulator_Trinogo():
    # Tampilkan menu sub-operator trigonometri 1-12
    print("\n",'='*50)
    print('''
        1. Sisi c
        2. Sisi b
        3. Sisi a
        4. c dari a dan sin(alpha)
        5. c dari b dan cos(alpha)
        6. a dari c dan sin(alpha)
        7. a dari b dan tan(alpha)
        8. b dari c dan cos(alpha)
        9. b dari a dan tan(alpha)
        10. alpha dari a dan c
        11. alpha dari b dan c
        12. alpha dari a dan b
        ''')
    print('='*50, "\n")
    operator = input("Masukkan opsi (1-12): ")
    match operator:
        case "1": TrinogomeOpsi.sisiC()
        case "2": TrinogomeOpsi.sisiB()
        case "3": TrinogomeOpsi.sisiA()
        case "4": TrinogomeOpsi.cDaria()
        case "5": TrinogomeOpsi.cDariBdanCosAlpha()
        case "6": TrinogomeOpsi.aDariCdanSinAlpha()
        case "7": TrinogomeOpsi.aDariBdanTanAlpha()
        case "8": TrinogomeOpsi.bDariCdanCosAlpha()
        case "9": TrinogomeOpsi.bDariAdanTanAlpha()
        case "10": TrinogomeOpsi.alphaDariAC()
        case "11": TrinogomeOpsi.alphaDariBC()
        case "12": TrinogomeOpsi.alphaDariAB()
        case _: print("Operator tidak dikenali!")

            
   
                
                    
def matrix_Math():
    print('='*50, "\n")
    print('''
        1. Matrix Pangkat (2x2,3x3,4x4, costum)
        2. Matrix Operator (+,-,*,/,//,**,%)
        3. Matrix Determinan/Invers
        4. Matrix Transpose
        
          ''')
    print("Pilihan Matrix (1-4):")
    print('='*50, "\n")
    operator = input("Masukkan opsi (1-4): ")
    print('='*50, "\n")
    match operator:
        case "1": Matrixs.matrix_pangkat_costum()
        case "2": Matrixs.matrix_operator()
        case "3": MatrixInvers.matrix_invers()
        case "4": MatrixsTranspose.matrix_transpose()
        # case "4": matrix_determinan()
        # case "6": matrix_transpose()
        case _: print("Opsi tidak dikenali!")
        
def factorial_Opsi():
    Factorial.factorialMath()