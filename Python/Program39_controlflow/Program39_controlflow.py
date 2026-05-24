# control flow statements
# pass, continue, break, return
# pass mecegah kode error saat blok kode kosong
# contoh penggunaan pass, atau ingin dilanjutkan nanti

number = 0
#while number < 10:
    #number += 1
    #print(f"nomor sekarang {number}")
    #if number == 5:
  #      print("hello 5")
   #     pass  # pass tidak melakukan apa-apa, hanya untuk mengisi blok kode
 #       print("lanjutkan ke nomor berikutnya")
#print("selesai")
# continue digunakan untuk melewati iterasi saat kondisi tertentu terpenuhi
    
while number < 10:
    number += 1
    if number == 5:
        print("hello 5")
        continue  # melewati iterasi saat number == 5
        print(f"Akan dilewati nomor {number}")
    print(f"nomor sekarang {number}")
    

    
    

