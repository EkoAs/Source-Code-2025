# Copy and pop dictionary
teman_teman = {
    'tong':'otong',
    'dit':'adit',
    'cup':'ucup'
}
# copy list biasa
dataCopy = teman_teman
print(f"data teman2 = {teman_teman}")
print(f"data copy = {dataCopy}\n")

data2 = teman_teman.copy()
data2['sep'] = 'asep'# melihat perbedaan setelah di ubah
print(f"data teman2 = {teman_teman}")
print(f"data copy = {data2}\n")

# pop dictionary / mengambil berdasarkan key
dataUcup = data2.pop('cup')
print(f"data teman2 = {data2}")
print(f"data copy = {dataUcup}\n")

# pop item / mengambil data paling akhir 
dataEnd = data2.popitem()
print(f"data teman2 = {data2}")
print(f"data copy = {dataEnd}\n")
