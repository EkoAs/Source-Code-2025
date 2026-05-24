# Format string
nama = "ucup"
format = f"nama saya adalah {nama}"
print(format)

# bilangan desimal 
x = 2005.54321
format = f"bilangan desimal adalah {x:.2f}" # 2 digit dibelakang koma
print(format)

# menampilkan leading zero
x = 2005
format = f"bilangan leading zero adalah {x:05d}" # 5 digit  
print(format) 

#menghilangkan angka belakang
x = 2005.54321
format = f"bilangan leading zero adalah {x:.3f}" # 3 digit dibelakang koma
print(format)

# memformat persen
x = 0.045
format = f"bilangan persen adalah {x:.2%}" # 2 digit dibelakang koma
print(format)

# bilangan bulat
x = 20
format = f"bilangan bulat adalah {x:d}" # 2 digit dibelakang koma
print(format)

# menampilkan plus minus
x = -10
format = f"bilangan plus minus adalah {x:+d}" 
print(format)                    

x = +10
format = f"bilangan plus minus adalah {x:+d}" 
print(format)                    

# format lainnya
x = 10
format = f"bilamgan binary {bin(x)}" # binary
print(format)
x = 10 
format = f"bilamgan octal {oct(x)}" # octal
print(format)
x = 10
format = f"bilamgan hex {hex(x)}" # hex
print(format)
