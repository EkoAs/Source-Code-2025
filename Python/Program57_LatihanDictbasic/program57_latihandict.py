# Latihan dict basic dan penggunaan list
emptyList = []
userInput = str(input("Masukan Daftar :"))
userInputKey = str(input("Masukan kata Kunci :"))
data = {
    userInputKey:userInput
}
dataUser = data[userInputKey]
fullData = list(dataUser)
print(f"Full data{fullData}")
while True:
       print(fullData)
       if len(fullData) == 1:
           break
       fullData = fullData[:-1]