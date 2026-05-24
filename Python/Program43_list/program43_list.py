# list 

# Int list 
dataInt = [1, 2, 3, 4, 5]
print(dataInt)

# String list
dataStr = ["satu", "dua", "tiga", "empat", "lima"]
print(dataStr)

# boolean list
dataBool = [True, False, True, False, True]
print(dataBool)

# list campuran
dataMix = [1, "dua", 3.0, True, "lima"]
print(dataMix)

# buat list
data = range(1, 11, 2)  # membuat list dari 1 sampai 10 range(start, stop, step)
print(f"{list(data)}")


# memisahkan list
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data1, data2, data3 = data[:3], data[3:6], data[6:]
print(f"data1: {data1}")
print(f"data2: {data2}")
print(f"data3: {data3}")

# gabungkan list
dataGabung = data1 + data2 + data2
print(f"dataGabung: {dataGabung}")
# menghapus list
del dataGabung[0]  # menghapus data pertama
print(f"dataGabung setelah dihapus: {dataGabung}")