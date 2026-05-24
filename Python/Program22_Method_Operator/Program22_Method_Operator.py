# operator method
# # mengubah huruf pertama menjadi kapital

uppertxt = "halo"
hasil = uppertxt.upper()
print('Normal :\t', uppertxt)
print('upper :\t', hasil)

#pengecekan dengan is method
hasil = uppertxt.isupper()
print('isupper :\t', str(hasil))

hasil2 = uppertxt.isdecimal()
print('isdecimal :\t', str(hasil2))

hasil3 = uppertxt.isalpha()
print('isalpha :\t', str(hasil3))

hasil4 = uppertxt.isspace()
print('isspace:\t', str(hasil4))

# alokasi karakter
user = "tengah".center(10)
print(user)

user = "kiri".ljust(10)
print(user)

user = "kanan".rjust(10, '=')
print(user)

# penggabungang komponen 
x = ["Halo", "Dunia", "aim"]
join = ' '.join(x)
print(join)

# split
y = "HaloooDuniaooaimoo".split('oo')

print(y)


