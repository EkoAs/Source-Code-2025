# Operasi Logika atau boolean 
# Operator Logika atau boolean
# not, or, and, xor
print('=========== NOT') # kebalikan dari True => false, begitu juga sebaliknya
a = True
print('Nilai a =', a)
hasil = not a
print('not a =', hasil)

print('=========== OR') # jika salah satu benar maka hasilnya true
a = True 
b = False
hasil = a or b
print(a, 'or', b, '=', hasil)
hasil = b or a
print(b, 'or', a, '=', hasil)
hasil = a or a
print(a, 'or', a, '=', hasil)
hasil = b or b
print(b, 'or', b, '=', hasil)

print('=========== AND') # jika salah satu false maka akan false
a = True 
b = False
hasil = a and b
print(a, 'and', b, '=', hasil)
hasil = b and a
print(b, 'and', a, '=', hasil)
hasil = a and a
print(a, 'and', a, '=', hasil)
hasil = b and b
print(b, 'and', b, '=', hasil)

print('=========== XOR') # aka true jika salah satu true, sisanya false 
a = True 
b = False
hasil = a ^ b
print(a, '^', b, '=', hasil)
hasil = b ^ a
print(b, '^', a, '=', hasil)
hasil = a ^ a
print(a, '^', a, '=', hasil)
hasil = b ^ b
print(b, '^', b, '=', hasil)