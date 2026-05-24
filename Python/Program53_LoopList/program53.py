# loop dari list
# For loop
data = [1, 2, 3, 4, 5, 7, 6]
for angka in (data):
    print(f"Angka = {angka}")
    
# for range 
print("\n")
panjang = len(data)
for i in range(panjang):
    print(f"Angka = {i}")
    
# while
print("\n")
i = 0 
while i < panjang:
    print(f"Angka = {i}")
    i += 1
print("\n")


# List comprehension / cara cepat
print(f"List comprehension")
[print(f"Angka = {i}") for i in data]


print("\n")
# menggunalan enumerate
for index,data in enumerate(data):
    print(f"angka = {data}")
    print(f"angka = {index}")