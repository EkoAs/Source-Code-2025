// =============================================================================
//                             KONFIGURASI GLOBAL
// =============================================================================
const game = {
    score: 0,
    currentMode: '',
    currentAnswer: null,
    timerInterval: null,
    timeLeft: 0,
    totalTime: 0,

    // =========================================================================
    //                             MULAI PERMAINAN
    // =========================================================================
    start: function(mode) {
        this.currentMode = mode;
        this.score = 0;
        
        // Update UI
        document.getElementById('score').innerText = "0";
        document.getElementById('menu-screen').style.display = 'none';
        document.getElementById('game-over-screen').style.display = 'none';
        
        const gameScreen = document.getElementById('game-screen');
        gameScreen.classList.remove('hidden'); // Hapus class hidden CSS
        gameScreen.style.display = 'block';

        // Panggil Soal Pertama
        this.nextQuestion();
    },

    // =========================================================================
    //                             AMBIL SOAL (FETCH)
    // =========================================================================
    nextQuestion: async function() {
        try {
            // Request ke Python
            const response = await fetch('/get_question', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ mode: this.currentMode })
            });
            const data = await response.json();

            // Simpan Kunci Jawaban
            this.currentAnswer = data.answer;

            // Tampilkan Soal
            document.getElementById('question-text').innerText = data.question;

            // Setup Input (Tombol atau Text)
            this.renderInput(data);

            // Mulai Timer
            this.startTimer(data.time_limit);

        } catch (error) {
            console.error("Error ambil soal:", error);
        }
    },

    // =========================================================================
    //                             RENDER TAMPILAN INPUT
    // =========================================================================
    renderInput: function(data) {
        const inputArea = document.getElementById('input-area');
        inputArea.innerHTML = ''; // Bersihkan area

        if (data.input_type === 'buttons') {
            // ----- MODE PILIHAN GANDA -----
            const grid = document.createElement('div');
            grid.className = 'options-grid';
            
            data.options.forEach(opt => {
                const btn = document.createElement('button');
                btn.className = 'btn-luxury'; // Pakai style mewah tadi
                btn.innerText = opt;
                btn.onclick = () => this.checkAnswer(opt);
                grid.appendChild(btn);
            });
            inputArea.appendChild(grid);

        } else {
            // ----- MODE ISIAN TEXT -----
            const input = document.createElement('input');
            input.type = 'number';
            input.placeholder = '?';
            input.id = 'user-input';
            input.autocomplete = 'off';
            
            // Cek jawaban saat tekan Enter
            input.onkeydown = (e) => {
                if (e.key === 'Enter') this.checkAnswer(parseInt(input.value));
            };
            
            inputArea.appendChild(input);
            setTimeout(() => input.focus(), 100); // Auto focus
        }
    },

    // =========================================================================
    //                             SISTEM TIMER
    // =========================================================================
    startTimer: function(seconds) {
        if (this.timerInterval) clearInterval(this.timerInterval);
        
        this.totalTime = seconds;
        this.timeLeft = seconds;
        
        const timerBar = document.getElementById('timer-bar');
        timerBar.style.width = '100%';
        timerBar.style.transition = 'none'; // Reset animasi
        
        // Trik kecil biar animasi jalan mulus dari 100%
        setTimeout(() => {
            timerBar.style.transition = `width ${seconds}s linear`;
            timerBar.style.width = '0%';
        }, 50);

        this.timerInterval = setInterval(() => {
            this.timeLeft -= 0.1;
            if (this.timeLeft <= 0) {
                this.gameOver();
            }
        }, 100);
    },

    // =========================================================================
    //                             CEK JAWABAN
    // =========================================================================
    checkAnswer: function(userVal) {
        if (userVal === this.currentAnswer) {
            // JAWABAN BENAR
            this.score += 10;
            document.getElementById('score').innerText = this.score;
            
            // Stop timer lama, lanjut soal baru
            clearInterval(this.timerInterval);
            this.nextQuestion();
        } else {
            // JAWABAN SALAH
            this.gameOver();
        }
    },

    // =========================================================================
    //                             GAME OVER
    // =========================================================================
    gameOver: function() {
        clearInterval(this.timerInterval);
        document.getElementById('game-screen').style.display = 'none';
        document.getElementById('game-over-screen').style.display = 'block';
        document.getElementById('game-over-screen').classList.remove('hidden');
        document.getElementById('final-score').innerText = this.score;
    }
};