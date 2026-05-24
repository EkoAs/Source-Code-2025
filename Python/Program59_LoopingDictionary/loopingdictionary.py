# Looping Dictionary
temanTeman = {
    'cup':'Ucup',
    'tong':'Otong',
    'dung':'dudung',
    'sep':'aseep'
}
# mengambil key saja
# loopping first try
print(f"mencetak key saja")
for teman in temanTeman:
    print(f"{teman}")
   
# mengambil isinya saja 
print(f"mencetak value saja\n")
keys = temanTeman.keys()
for key in temanTeman.keys():
    print(f"{temanTeman.get(key)}")
    
values = temanTeman.values()
for value in temanTeman.values():
    print(f"{value}")
    
# meng akses dua duanya
items = temanTeman.items()
for key, value in temanTeman.items():
    print(f"key = {value} item = {value}")
    
# Membuat dictionary baru dengan key dan value yang dibalik
temanTerbalik = {value: key for key, value in temanTeman.items()}
print(temanTerbalik)
