class Pengecekan:
    def __init__(self, text):
        self.text = text.strip()  
    
    def is_all_upper(self):
        return self.text.isupper()
    
    def is_all_lower(self):
        return self.text.islower()
    
    def get_length(self):
        return len(self.text)


def get_user_input():
    while True:
        text = input("input: ").strip()  # strip() untuk hapus spasi ekstra
        if text:  # Cek apakah input tidak kosong
            return text
        else:
            print("Input tidak boleh kosong. Coba lagi.")


if __name__ == "__main__":
    user_text = get_user_input()
    checker = Pengecekan(user_text)
    all_upper = checker.is_all_upper()
    all_lower = checker.is_all_lower()
    print(f"1. Apakah semuanya huruf besar? {all_upper} ({'Benar' if all_upper else 'Salah'})")
    print(f"2. Apakah semuanya huruf kecil? {all_lower} ({'Benar' if all_lower else 'Salah'})")
    print(f"Panjang teks: {checker.get_length()}")
