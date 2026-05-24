from data.input import chose
while True:
    chose()
    lanjut = input("\nLanjut? (y/n): ").lower()
    if lanjut != 'y':
        break