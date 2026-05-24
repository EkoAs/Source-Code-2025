''' Fungsi dengan argumen (input)'''
# # template fungsi
# def nama fungsi (argumen)
#     badan fungsi

'''Fungsi argumen'''
def hello(nama):
    '''fungsi menerima input dengan variable nama'''
    print(f"Halo yang terhormat {nama}")
    
hello("Ucup")
hello("Otong")
hello("Dudung")
print('\n')

def tambah(num1, num2):
    hasil = num1 + num2
    print(f"Hasil dari {num1} + {num2} = {hasil}")
tambah(2,9)
tambah(0,1)
tambah(9,1)
print('\n')
def list(anggota):
    numz = 0
    copyList = anggota.copy()
    for peserta in copyList:
        numz += 1
        print(f"anggota ke {numz} adalah {peserta}")
grup = ['Ucup', 'Rian', 'Dudung']
list(grup)
