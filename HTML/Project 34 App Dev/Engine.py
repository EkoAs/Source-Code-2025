import random

class MathEngine:
    def __init__(self):
        self.operators = ['+', '-', '*', '/']

    def generate_question(self, mode):
        """
        Menghasilkan soal, jawaban, tipe input, dan batas waktu
        berdasarkan mode yang dipilih.
        """
        question = ""
        answer = 0
        options = []  # Untuk pilihan ganda
        input_type = "text" # text atau buttons
        time_limit = 10

        if mode == 'perkalian':
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            question = f"{a} x {b}"
            answer = a * b
            
            # Konfigurasi khusus Perkalian
            time_limit = 4
            input_type = "buttons"
            options = self._generate_options(answer)

        elif mode == 'pembagian':
            # Memastikan hasil pembagian adalah bilangan bulat
            b = random.randint(2, 10)
            answer = random.randint(2, 12) # Jawaban kita tentukan dulu
            a = b * answer # Maka A pasti bisa dibagi B
            question = f"{a} : {b}"
            
        elif mode == 'penambahan':
            a = random.randint(10, 99)
            b = random.randint(10, 99)
            question = f"{a} + {b}"
            answer = a + b

        elif mode == 'pengurangan':
            a = random.randint(20, 100)
            b = random.randint(1, a) # Agar hasil tidak negatif
            question = f"{a} - {b}"
            answer = a - b

        elif mode == 'campuran':
            # Contoh logika campuran: (A op B) op C
            # batasi angka
            ops = ['+', '-', '*'] 
            op1 = random.choice(ops)
            op2 = random.choice(ops)
            
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            
            # String expression untuk Python eval
            # template untuk operasinya
            expr = f"({a} {op1} {b}) {op2} {c}"
            
            # Tampilan user (x diganti simbol kali yang bagus)
            display_expr = expr.replace('*', 'x')
            
            answer = eval(expr)
            question = display_expr

        return {
            "question": question,
            "answer": int(answer), # Pastikan integer
            "input_type": input_type,
            "options": options,
            "time_limit": time_limit
        }

    def _generate_options(self, correct_ans):
        """Membuat opsi jawaban pengecoh untuk pilihan ganda"""
        options = {correct_ans}
        while len(options) < 4:
            # Buat pengecoh di sekitar jawaban benar (+- 5 atau 10)
            decoy = correct_ans + random.randint(-10, 10)
            if decoy > 0 and decoy != correct_ans:
                options.add(decoy)
        
        opts_list = list(options)
        random.shuffle(opts_list)
        return opts_list