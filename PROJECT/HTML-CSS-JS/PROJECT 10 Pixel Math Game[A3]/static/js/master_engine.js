const MasterEngine = {
    score: 0,
    timerInterval: null,
    timeLeft: 10,
    currentKey: 0,

    // --- ==================FUNGSI MENU========= ---
    goToMode: function(modeName) {
        const name = document.getElementById('player-name').value;
        if(!name) {
            
            const input = document.getElementById('player-name');
            input.style.borderColor = "white";
            input.placeholder = "ISI NAMA!";
            setTimeout(() => input.style.borderColor = "", 500);
            return;
        }
        localStorage.setItem('pixel_player', name);
        window.location.href = '/play/' + modeName;
    },

    // --- ============================FUNGSI GAME================= ---
    startGame: function() {
        this.score = 0;
        this.fetchSoal();
    },

    fetchSoal: async function() {
        if(this.timerInterval) clearInterval(this.timerInterval);

        const mode = document.getElementById('game-mode').value;

        const response = await fetch('/api/get_soal', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ mode: mode })
        });
        const data = await response.json();

        document.getElementById('question-text').innerText = data.soal;
        this.currentKey = data.kunci;

        this.timeLeft = data.waktu || 10; 
        this.startTimer();

        const grid = document.getElementById('options-grid');
        grid.innerHTML = '';
        
        data.opsi.forEach(opt => {
            const btn = document.createElement('button');
            btn.className = 'btn-pixel';
            btn.innerText = opt;
            btn.onclick = () => this.checkAnswer(opt);
            grid.appendChild(btn);
        });
    },

    checkAnswer: function(userAnswer) {
        if(userAnswer == this.currentKey) {
            this.score += 10;
            document.getElementById('score').innerText = this.score;
            this.fetchSoal();
        } else {
            this.gameOver();
        }
    },

    startTimer: function() {
        if(this.timerInterval) clearInterval(this.timerInterval);
        document.getElementById('timer').innerText = this.timeLeft;

        this.timerInterval = setInterval(() => {
            this.timeLeft--;
            document.getElementById('timer').innerText = this.timeLeft;
            
            if(this.timeLeft <= 0) {
                this.gameOver();
            }
        }, 1000);
    },

    // --- ==================UPDATEGAME OVER TANPA ALERT=============== ---
    gameOver: function() {
        clearInterval(this.timerInterval);
        const playerName = localStorage.getItem('pixel_player') || "Unknown";
        
        // 1. Simpan Score ke Backend=========================
        fetch('/api/save_score', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ nama: playerName, score: this.score })
        });

        // 2. Tampilkan Modal Game Over ===============================
        const modal = document.getElementById('game-over-modal');
        
        // Isi data ke modal===================================
        document.getElementById('final-player').innerText = playerName;
        document.getElementById('final-score').innerText = this.score;
        
        // Munculkan modal (ubah display dari none ke flek)================
        modal.style.display = 'flex';
    }
};