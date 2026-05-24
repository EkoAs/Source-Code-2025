# latihan loop segitiga
sisi = 10

print("untuk for")
# pakai for
# pakai dummy variable
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1



print("untuk while")
# 2. menggunakan while
count = 1
while True:
    print("*"*count)
    count += 1
    if count > sisi:
        break



# 3. Tugas buat belah ketupat6
spasi = int(sisi/2)
count = 1
while True:
    print(" "*spasi + "*"*count).center()
    count += 2
    spasi -= 1
    if count  < sisi:
          break
            
