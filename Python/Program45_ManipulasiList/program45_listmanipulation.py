# Belajar manipulasi list
data = [" Ucup", " Otong", " Deden", " Ujang", " Asep"]
# mengambil data dari list 
data1 = data[0]
print(f"data ke 0 adalah {data1}")
# mengambil jumlah data dalam list
jumlahData = len(data)
print(f"Jumlah data dalam list {jumlahData}")

# manipulasi data
# menambah item pada list sesuai posisi
dataNew = data.insert(0, "mikael")
print(f"data setelah ditambah: {data}")

# menambah langsuung di akhir 
dataNew = data.append("Dani")
print(f"data setelah ditambah di akhir: {data}")



# merubah data ke ke satu jadi "Dani"
data[0] = "Dani"
print(f"data setelah diubah: {data}")

# menghapus data dari list
data.remove("Dani")  # menghapus data "Dani"
print(f"setelalh menghapus data Dani {data}")

# menghapus data paling akhir
data.pop()
print(f"setelah menghapus  data paling akhir {data}")

# menggabungkan list atau menambah list dengan list
data2 = ["Hans", "Dapa", "Zulbahri"]
dataupdate = data.extend(data2) # kok hasilnya none? 
print(f"data setelah digabungkan {data}")

# mengurutkan data
data.sort(reverse=True)  # mengurutkan data secara ascending # dari Z ke a
print(f"data setelah diurutkan {data}")


