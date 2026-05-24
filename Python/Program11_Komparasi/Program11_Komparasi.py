
a = 4
b = 3
print('=========== Lebih Dari >')
hasil = a > b
print(a, '>', b, '=', hasil)
hasil = a > 5
print(a, '>', 5, '=', hasil)
hasil = a > 4
print(a, '>', 4, '=', hasil)

print('========== Kurang Dari <')
hasil = a < b
print(a, '<', b, '=', hasil)
hasil = a < 5
print(a, '<', 5, '=', hasil)
hasil = a < 4
print(a, '<', 4, '=', hasil)

print('========== Lebih dari sama dengan >=')
hasil = a >= b
print(a, '>=', b, '=', hasil)
hasil = a >= 5
print(a, '>=', 5, '=', hasil)
hasil = a >= 4
print(a, '>=', 4, '=', hasil)

print('========== Kurang dari sama dengan <=')
hasil = a <= b
print(a, '<=', b, '=', hasil)
hasil = a <= 5
print(a, '<=', 5, '=', hasil)
hasil = a <= 4
print(a, '<=', 4, '=', hasil)

print('========== sama dengan ==')
hasil = a == b
print(a, '==', b, '=', hasil)
hasil = a == 5
print(a, '==', 5, '=', hasil)
hasil = a == 4
print(a, '==', 4, '=', hasil)

print('==========  Tidak sama dengan !=')
hasil = a != b
print(a, '!=', b, '=', hasil)
hasil = a != 5
print(a, '!=', 5, '=', hasil)
hasil = a != 4
print(a, '!=', 4, '=', hasil)

print('========== object identity is')
x = 5
y = 5
print('Identity x', hex(id(x)))
print('Identity y', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

print('========== object identity is not') # kebalikan dari is
x = 5
y = 6
print('Identity x', hex(id(x)))
print('Identity y', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)

print('==========  Logika AND')
a = True
b = False
print('a =', a)
print('b =', b)
print('a and b =', a and b)
print('a or b =', a or b)
print('not a =', not a)
print('not b =', not b)