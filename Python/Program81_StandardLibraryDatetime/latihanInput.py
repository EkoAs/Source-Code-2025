import datetime
from datetime import timedelta
now = datetime.datetime.now()
day = int(input("Masukan hari ke :"))
mon = int(input("Masukan bulan ke :"))
year = int(input("Masukan tahun ke :"))
if mon < 1:
    mon = 1
elif mon > 12:
    mon = 12
    
valid_date = datetime.datetime(year, mon, day)
print(f"Tanggal yang dimasukkan: {valid_date.strftime('%d-%m-%Y')}")



