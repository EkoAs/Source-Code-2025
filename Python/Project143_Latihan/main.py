class CekHurufAngka:
    def __init__(self, text):
        self.text = text.strip() 
    
    def validate_alphanumeric(self):
        return self.text.isalnum()
    
    def get_length(self):
        return len(self.text)

def get_user_input():
    while True:
        text = input("input: ").strip()  
        if text: 
            return text
        else:
            print("Input tidak boleh kosong. Coba lagi.")
if __name__ == "__main__":
    user_text = get_user_input()
    validator = CekHurufAngka(user_text)
    is_valid = validator.validate_alphanumeric()
    print(f"teks hanya isi huruf dan angka: {is_valid}")
    print(f"Panjang teks: {validator.get_length()}")
