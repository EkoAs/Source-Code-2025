<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Neuro Tech | Final Validation</title>
    <link rel="stylesheet" href="assets/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap" rel="stylesheet">
</head>
<body>

    <nav class="navbar">
        <div class="nav-logo">NEURO TECH</div>
        <div class="nav-links">
            <a href="index.php">Kembali ke Katalog</a>
        </div>
    </nav>

    <div style="max-width: 800px; margin: 50px auto; padding: 20px;">
        <div style="background: #1a1a1a; border: 1px solid var(--electric-yellow); border-radius: 10px; padding: 30px; box-shadow: var(--neon-glow);">
            <h2 style="font-family: 'Orbitron'; color: var(--electric-yellow); text-align: center;">FINAL VALIDATION</h2>
            <p style="text-align: center; color: #888;">Pastikan semua komponen sudah sesuai sebelum sinkronisasi database.</p>
            
            <hr border="0" style="border-top: 1px solid #333; margin: 25px 0;">

            <div id="checkout-list">
                </div>

            <div style="margin-top: 30px; padding: 20px; background: #0d0d0d; border-radius: 5px;">
                <div style="display: flex; justify-content: space-between; font-family: 'Orbitron';">
                    <span>TOTAL ESTIMASI:</span>
                    <span id="grand-total" style="color: var(--electric-yellow); font-size: 1.5rem;">Rp 0</span>
                </div>
            </div>

            <div style="margin-top: 30px; display: flex; gap: 15px;">
                <button class="btn-yellow" onclick="processPayment()" style="flex: 2; padding: 20px;">KONFIRMASI PEMBAYARAN</button>
                <button class="btn-yellow" onclick="window.history.back()" style="flex: 1; background: #333; color: #fff; border: 1px solid #444;">BATAL</button>
            </div>
        </div>
    </div>

    <script>
        // Simulasi data dari LocalStorage atau Session
        // (Biasanya data dikirim dari index.php atau smart_build.php)
        const cartData = JSON.parse(localStorage.getItem('neuro_cart')) || [];

        function renderCheckout() {
            const container = document.getElementById('checkout-list');
            let total = 0;
            
            if(cartData.length === 0) {
                container.innerHTML = "<p style='text-align:center;'>Keranjang kosong.</p>";
                return;
            }

            container.innerHTML = cartData.map(item => {
                total += item.harga_display || item.harga;
                return `
                    <div style="display: flex; justify-content: space-between; margin-bottom: 15px; border-bottom: 1px solid #222; padding-bottom: 10px;">
                        <div>
                            <span style="color: var(--electric-yellow); font-size: 0.8rem;">${item.kategori}</span>
                            <div style="font-weight: bold;">${item.nama}</div>
                        </div>
                        <div style="text-align: right;">
                            Rp ${(item.harga_display || item.harga).toLocaleString()}
                        </div>
                    </div>
                `;
            }).join('');

            document.getElementById('grand-total').innerText = "Rp " + total.toLocaleString();
        }

        async function processPayment() {
            if(cartData.length === 0) return alert("Pilih barang dulu!");

            // Kirim data ke Python (app.py) untuk potong stok
            try {
                const response = await fetch('http://127.0.0.1:5000/api/checkout', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ cart: cartData })
                });

                const result = await response.json();

                if(result.status === 'success') {
                    alert("SINKRONISASI BERHASIL: Stok telah diperbarui.");
                    // Pindah ke halaman struk
                    window.location.href = 'receipt.php';
                } else {
                    alert("ERROR: " + result.message);
                }
            } catch (error) {
                alert("Gagal terhubung ke Neuro Engine!");
            }
        }

        window.onload = renderCheckout;
    </script>
</body>
</html>