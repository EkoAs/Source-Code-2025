# contoh membuat exception sendiri
# contoh 1
from numbers import Number
def tambah(a,b): # biar a b cuma nagka doang
    if not isinstance(a, Number) or not isinstance(b, Number): # akan ngasih tau dia number atau bukan
        raise f"input pertama harus angka" #buat naikin exceptionnya
    return a + b

print(tambah(1,4))


# contoh 2
# menangkap berdasarkan tipe exteptionnya
angka = 0
try:
    hasil = 10/angka
    
except Exception as error_message:
    print(error_message)
    # atau
# except ZeroDivisionError as error_message:
#     print(error_message) # lebih detail
    