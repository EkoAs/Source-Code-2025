<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neuro Tech | High-End PC Supply</title>
    <link rel="stylesheet" href="assets/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap" rel="stylesheet">
</head>
<body>

    <nav class="navbar">
        <div class="nav-logo">NEURO TECH</div>
        <div class="nav-links">
            <a href="index.php">Katalog</a>
            <a href="smart_build.php" style="color: var(--electric-yellow); border: 1px solid var(--electric-yellow); padding: 5px 15px; border-radius: 5px;">Build by Budget</a>
            <a href="cart.php">Keranjang (<span id="cart-count">0</span>)</a>
        </div>
    </nav>

    <header style="padding: 50px 2rem; text-align: center; background: radial-gradient(circle, #1a1a1a 0%, #0d0d0d 100%);">
        <h1 style="font-family: 'Orbitron', sans-serif; letter-spacing: 5px;">PREMIUM COMPONENTS</h1>
        <p style="color: #888;">Level up your rig with industrial grade hardware.</p>
    </header>

    <main style="padding: 2rem;">
        <div id="catalog-container" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 25px;">
            <p>Loading components...</p>
        </div>
    </main>

    <footer style="text-align: center; padding: 40px; border-top: 1px solid #222; margin-top: 50px; color: #555;">
        &copy; 2025 NEURO TECH SUPPLY. Powered by Dual-Engine Technology.
    </footer>

    <script>
        // Ambil data dari Python API (app.py)
        async function loadCatalog() {
            try {
                const response = await fetch('http://127.0.0.1:5000/api/components');
                const components = await response.json();
                
                const container = document.getElementById('catalog-container');
                container.innerHTML = '';

                components.forEach(item => {
                    container.innerHTML += `
                        <div class="component-card">
                            <img src="${item.gambar}" alt="${item.nama}" style="width: 100%; border-radius: 5px; margin-bottom: 15px;">
                            <div style="font-size: 0.8rem; color: var(--electric-yellow); margin-bottom: 5px;">${item.brand}</div>
                            <h3 style="margin: 0 0 10px 0; font-family: 'Rajdhani', sans-serif;">${item.nama}</h3>
                            <div class="price-tag">Rp ${item.harga.toLocaleString('id-ID')}</div>
                            <p style="font-size: 0.8rem; color: #888;">Stok: ${item.stok}</p>
                            <button class="btn-yellow" style="width: 100%; margin-top: 15px;" onclick="addToCart('${item.id}')">Add to Build</button>
                        </div>
                    `;
                });
            } catch (error) {
                console.error("Gagal load data:", error);
                document.getElementById('catalog-container').innerHTML = "<p>Gagal terhubung ke Engine. Pastikan app.py sudah jalan!</p>";
            }
        }

        function addToCart(id) {
            alert("Barang " + id + " ditambahkan ke keranjang!");
            // Logika keranjang bisa kita kembangkan nanti
        }

        window.onload = loadCatalog;
    </script>
</body>
</html>