class StringWordChecker:
    def __init__(self, sentence, start_word, end_word):
        self.sentence = sentence.strip() 
        self.start_word = start_word.strip()  
        self.end_word = end_word.strip()  
        self.words = self.sentence.split()  
    
    def is_start_with_word(self):
        if not self.words:  
            return False
        return self.words[0] == self.start_word
    
    def is_end_with_word(self):
        if not self.words: 
            return False
        return self.words[-1] == self.end_word
    
    def get_word_count(self):
        return len(self.words)


def get_user_input(prompt):
    while True:
        text = input(prompt).strip()  
        if text:
            return text
        else:
            print("Input tidak boleh kosong. Coba lagi.")


if __name__ == "__main__":
    sentence = get_user_input("input kalimat: ")
    start_word = get_user_input("kata awal: ")
    end_word = get_user_input("kata akhir: ")
    checker = StringWordChecker(sentence, start_word, end_word)

    print(f'kalimat = {checker.sentence}')
    print(f'kata awal = {checker.start_word}')
    print(f'kata akhir = {checker.end_word}')
    print(f'diawali kata "{checker.start_word}"? {str(checker.is_start_with_word()).lower()}')
    print(f'diakhiri kata "{checker.end_word}"? {str(checker.is_end_with_word()).lower()}')
    print(f"Jumlah kata: {checker.get_word_count()}")
