import random

# ==============================================================================
#                               CLASS MATH ENGINE
# ==============================================================================
#  Ini adalah "Dapur" tempat meracik soal.
#  Semua logika angka, operator campuran, dan pilihan ganda ada di sini.
# ==============================================================================

class MathEngine:
    def __init__(self):
        self.operators = ['+', '-', '*']

    # ==========================================================================
    #  FUNGSI UTAMA: GENERATE QUESTION
    #  Menerima 'mode' dari Flask, mengembalikan Paket Soal (JSON)
    # ==========================================================================
    def generate_question(self, mode):
        question = ""
        answer = 0
        options = []      # Kosong jika bukan pilihan ganda
        input_type = "text" # Default isian biasa
        time_limit = 10   # Default waktu

        # ----------------------------------------------------------------------
        #  MODE 1: PERKALIAN (SPEED MODE - PILIHAN GANDA)
        # ----------------------------------------------------------------------
        if mode == 'perkalian':
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            question = f"{a} x {b}"
            answer = a * b
            
            # Konfigurasi Khusus Perkalian
            time_limit = 2         # waktu khusus perkalian, hehehe
            input_type = "buttons"   # Pilihan Ganda
            options = self._generate_options(answer) # Buat pengecoh

        # ----------------------------------------------------------------------
        #  MODE 2: CAMPURAN (RANDOM TEMPLATE)
        # ----------------------------------------------------------------------
        elif mode == 'campuran':
            # Pilih operator dan anka acak
            op1 = random.choice(self.operators)
            op2 = random.choice(self.operators)
            
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)

            # Pola Soal (Template)
            pola_soal = [
                f"({a} {op1} {b}) {op2} {c}",
                f"{a} {op1} ({b} {op2} {c})",
                f"{a} {op1} {b}"
            ]
            
            expr = random.choice(pola_soal)
            
            # Hitung jawaban (Python menghitung otomatis)
            answer = eval(expr)
            
            # Format tampilan (ganti * jadi x)
            question = expr.replace('*', 'x')
            time_limit = 5 # Waktu khusus campuran (gausan kelamaan, udh gede gabisa mtk)

        # ----------------------------------------------------------------------
        #  MODE 3: PENGURANGAN
        # ----------------------------------------------------------------------
        elif mode == 'pengurangan':
            a = random.randint(20, 100)
            b = random.randint(1, a) # Biar tidak minus
            question = f"{a} - {b}"
            answer = a - b
            time_limit = 8

        # ----------------------------------------------------------------------
        #  MODE 4: PENAMBAHAN
        # ----------------------------------------------------------------------
        elif mode == 'penambahan':
            a = random.randint(10, 50)
            b = random.randint(10, 50)
            question = f"{a} + {b}"
            answer = a + b
            time_limit = 8

        return {
            "question": question,
            "answer": int(answer),
            "input_type": input_type,
            "options": options,
            "time_limit": time_limit
        }

    # ==========================================================================
    #  FUNGSI BANTUAN: MEMBUAT OPSI PENGECOH
    #  khusuk mode Perkalian
   
    def _generate_options(self, correct_ans):
        opts = {correct_ans} # Pakai set biar unik
        while len(opts) < 4:
            decoy = correct_ans + random.randint(-10, 10)
            if decoy > 0 and decoy != correct_ans:
                opts.add(decoy)
        
        hasil = list(opts)
        random.shuffle(hasil)
        return hasil