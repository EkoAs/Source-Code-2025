# anonymous dan lambda function 
def pangkat(num):
    return num**2 
print(f"hasil fungsi biasa = {pangkat(2)}")
# lambda function
#  output = lambda argumen:ekpession
pangkat = lambda angka:angka**2 
print(f"Hasil lambda = {pangkat(2)}")

# dengan dua atau lebih input
input2 = lambda num, pow:num**pow
print(f"dua input = {input2(2, 2)}")

input2 = lambda num,pow,mins:(num**pow)-mins
print(f"tiga input = {input2(2,2,2)}")

# sortir list str sesuai jumlah
data = ['asep', 'dudung', 'otong', 'cup', 'rian']
data.sort(key=lambda dat:len(dat))
print(f"data sortir = {data}")

# sortir angka tertentu/ kurang dari lima
data = [1,2,3,4,5,6,7,8,9,10]
datasort = list(filter(lambda x:x<5,data))
print(f"data angka kurang dari lima = {datasort}")

# sortir angka ganjil,genap
data = [1,2,3,4,5,6,7,8,9,10]
ganjil = list(filter(lambda x:x % 2 != 0,data))
print(f"data angka ganjil = {ganjil}")

genap = list(filter(lambda x:x % 2 == 0,data))
print(f"data angka genap = {genap}")

kelipatan3 = list(filter(lambda x:x % 3 == 0,data))
print(f"data angka kelipatan3 = {kelipatan3}")

#  anonymous function 
# dengan currying
def pangkat(n):
    return lambda angka:angka**n
pangkat2 = pangkat(2)  # hasilnya 2 = 2 jadi => 4 
print(f"pangkat dari pangkat = {pangkat2(2)}")

# pangkat bebas
def pangkat(n):
    return lambda angka:angka**n
# pangkat2 = pangkat()  # hasilnya 2 = 2 jadi => 4 
print(f"pangkat dari pangkat bebas = {pangkat(2)(2)}")





