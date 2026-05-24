import datetime
# waktu saat ini 
nowTime = datetime.datetime.now()
print(f"Waktu saat ini : {nowTime} \n")

# waktu saat ini
waktu = datetime.datetime.today()
print(f"Waktu saat ini {waktu} \n")

# menghitung beberapa jam, hari ke depan
from datetime import timedelta
future_time = nowTime + timedelta(hours=4) #hours, days, minute, dll
print(f"Waktu 4 jam ke depan: {future_time}\n")

