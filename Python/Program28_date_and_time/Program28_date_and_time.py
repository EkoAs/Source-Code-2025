# date and time 
import datetime as dt
# Get the current date and time
hariini =  dt.date.today()
print(f"Hari ini adalah {hariini} Hari ini {hariini:%A} tanggal {hariini:%d} bulan {hariini:%B} tahun {hariini:%Y}")

# Get the current time
waktu = dt.datetime.now().time()
print(f"Waktu sekarang adalah {waktu:%H:%M:%S}")

tanggal = int(input("Masukan Tanggal :"))
bulan = int(input("Masukan Bulan :"))
tahun = int(input("Masukan Tahun :"))

tanggal_lahir = dt.datetime(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah {tanggal_lahir:%A} tanggal {tanggal_lahir:%d} bulan {tanggal_lahir:%B} tahun {tanggal_lahir:%Y}")
# Calculate the difference between today and the user's birthday 
# menghitung umur dari tanggal input dan tanggal hari ini
umur = hariini - tanggal_lahir.date()
year = umur.days // 365
mounth = (umur.days % 365) // 30 # menghitung sisa bulan dari umur
print(f"Umur anda adalah {year} tahun")
print(f"Umur anda adalah {umur.days} hari")
print(f"Umur anda adalah {mounth} bulan") 