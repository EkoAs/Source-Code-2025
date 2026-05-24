<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Neuro Tech | Smart PC Builder</title>
    <link rel="stylesheet" href="assets/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap" rel="stylesheet">
</head>
<body>

    <nav class="navbar">
        <div class="nav-logo">NEURO TECH</div>
        <div class="nav-links">
            <a href="index.php">Katalog</a>
            <a href="smart_build.php" style="color: var(--electric-yellow);">Smart Build</a>
        </div>
    </nav>

    <div style="max-width: 1000px; margin: 40px auto; padding: 20px;">
        <section id="budget-input" style="text-align: center; background: #1a1a1a; padding: 40px; border-radius: 15px; border: 1px dashed var(--electric-yellow);">
            <h2 style="font-family: 'Orbitron';">Berapa Budget Rakitan Kamu?</h2>
            <p style="color: #888;">Sistem cerdas kami akan memilihkan komponen terbaik & diskon random.</p>
            
            <div style="margin-top: 30px;">
                <input type="number" id="budget-value" placeholder="Contoh: 7000000" 
                       style="padding: 15px; width: 300px; border-radius: 5px; border: none; font-size: 1.2rem;">
                <button class="btn-yellow" onclick="generateBuild()" style="padding: 15px 30px; font-size: 1.1rem;">Mulai Rakit</button>
            </div>
        </section>

        <div id="status-message" style="text-align: center; margin-top: 20px;"></div>

        <section id="build-result" style="display: none; margin-top: 50px;">
            <div style="display: flex; gap: 30px; align-items: flex-start;">
                
                <div style="flex: 2;">
                    <h3 style="color: var(--electric-yellow); font-family: 'Orbitron';">Rekomendasi Komponen</h3>
                    <div id="build-list" style="display: flex; flex-direction: column; gap: 10px;"></div>
                </div>

                <div style="flex: 1; background: #1a1a1a; padding: 20px; border-radius: 10px; border-left: 5px solid var(--electric-yellow);">
                    <h3 style="font-family: 'Orbitron'; font-size: 1rem;">Analisis Neuro Engine</h3>
                    <hr border="0" style="border-top: 1px solid #333; margin: 15px 0;">
                    <div class="fps-info">
                        <p style="margin: 0; font-size: 0.9rem; color: #888;">Estimasi Performa GTA V:</p>
                        <h2 id="fps-value" style="color: var(--electric-yellow); margin: 5px 0;">-- FPS</h2>
                    </div>
                    <p id="performance-summary" style="font-style: italic; font-size: 0.9rem; color: #aaa;"></p>
                    <div style="margin-top: 20px;">
                        <p style="font-size: 0.8rem;">Total Harga:</p>
                        <h2 id="total-price" style="color: var(--electric-yellow);">Rp 0</h2>
                    </div>
                    <button class="btn-yellow" style="width: 100%; margin-top: 20px;">Cetak Struk Pembelian</button>
                </div>

            </div>
        </section>
    </div>

    <script>
        async function generateBuild() {
            const budget = document.getElementById('budget-value').value;
            const statusMsg = document.getElementById('status-message');
            const resultSection = document.getElementById('build-result');

            if(!budget || budget <= 0) return alert("Masukkan budget yang valid!");

            statusMsg.innerHTML = "<p style='color: var(--electric-yellow);'>Neuro Engine sedang menghitung...</p>";
            resultSection.style.display = 'none';

            try {
                const response = await fetch('http://127.0.0.1:5000/api/recommend', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ budget: parseFloat(budget) })
                });

                const data = await response.json();

                if(data.status === 'success') {
                    statusMsg.innerHTML = "";
                    resultSection.style.display = 'block';
                    
                    // Render List
                    const listContainer = document.getElementById('build-list');
                    listContainer.innerHTML = '';
                    data.items.forEach(item => {
                        listContainer.innerHTML += `
                            <div style="background: #222; padding: 15px; border-radius: 5px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <span style="color: var(--electric-yellow); font-size: 0.8rem;">[${item.kategori}]</span><br>
                                    <strong>${item.nama}</strong>
                                </div>
                                <div style="text-align: right;">
                                    ${item.is_discount ? `<small style="text-decoration: line-through; color: #666;">Rp ${item.harga.toLocaleString()}</small><br>` : ''}
                                    <span style="color: var(--electric-yellow);">Rp ${item.harga_display.toLocaleString()}</span>
                                </div>
                            </div>
                        `;
                    });

                    // Update Summary
                    document.getElementById('fps-value').innerText = data.performance.gtav_fps;
                    document.getElementById('performance-summary').innerText = data.performance.summary;
                    document.getElementById('total-price').innerText = "Rp " + data.total.toLocaleString();
                } else {
                    statusMsg.innerHTML = `<p style="color: #ff4444; font-weight: bold;">⚠️ ${data.message}</p>`;
                }
            } catch (error) {
                statusMsg.innerHTML = "<p style='color: red;'>Error: Engine Python tidak merespon.</p>";
            }
        }
    </script>
</body>
</html>