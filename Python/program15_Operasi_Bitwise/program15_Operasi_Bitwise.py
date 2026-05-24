
# Operasi Bitwise
a = 5
b = 2   
# operasi or ( | )
print('========== OR =========')
c = a | b
print(a, '==>', format(a, '08b')) 
print(b, '==>', format(b, '08b'))
print('------------------------ ( | )')
print(c, '==>', format(c, '08b'))

# operasi and ( & )
print('========== and =========')
c = a & b
print(a, '==>', format(a, '08b')) 
print(b, '==>', format(b, '08b'))
print('------------------------ ( & )')
print(c, '==>', format(c, '08b'))

# operasi xor ( ^ )
print('========== xor =========')
c = a ^ b
print(a, '==>', format(a, '08b'))
print(b, '==>', format(b, '08b'))
print('------------------------ ( ^ )')
print(c, '==>', format(c, '08b'))

# operasi not ( ~ )
print('========== not =========')
c = ~ a
print(a, '==>', format(a, '08b'))
print('------------------------ ( ~ )')
print(c, '==>', format(c, '08b'))
print(' dalam bentuk binary')
print(c, '==>', format(c & 0XFF, '08b')) # hasilnya minus 6

# untuk menghilangkan minus dari hasil no ( ~ )
print('========== not (hilangkan minus) =========')
c = 0b00000101
e = 0b11111111
f = a ^ e
print(f, '==>', format(f, '08b'))


# shifting (menggeser angka satu dalam binary)
print('========== shifting =========')
print('==========Menggeser ke kiri <<')
print(b, '==>', format(b,'08b'))
c = b << 1
print(c, '==>', format(c, '08b'))

print('==========Menggeser ke kanan >>')
print(b, '==>', format(b,'08b'))
c = b >> 1
print(c, '==>', format(c, '08b'))

#  