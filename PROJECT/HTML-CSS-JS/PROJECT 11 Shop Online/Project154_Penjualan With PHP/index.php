<?php
// 1. Ambil data dari API Python (Pastikan Flask python app.py sedang RUNNING)
$url = "http://127.0.0.1:5000/api/produk";
$search = isset($_GET['search']) ? $_GET['search'] : '';

// Jika ada pencarian, kirim parameter ke API
if (!empty($search)) {
    $url .= "?search=" . urlencode($search);
}

$response = @file_get_contents($url);
$produk = json_decode($response, true);
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tech Clothing - Koleksi Pakaian</title>
    <style>
        :root {
            --shiny-white: #f8f9fa;
            --metallic-silver: #e2e8f0;
            --dark-accent: #2d3436;
            --gold-shimmer: #d4af37;
        }

        body {
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #ffffff 0%, #dcdde1 100%);
            color: var(--dark-accent);
            min-height: 100vh;
        }

        nav {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(10px);
            padding: 15px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 15px rgba(0,0,0,0.1);
            border-bottom: 1px solid rgba(255,255,255,0.3);
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            letter-spacing: 2px;
            color: var(--dark-accent);
            text-transform: uppercase;
        }

        .search-container {
            flex-grow: 0.5;
            display: flex;
        }

        .search-container input {
            width: 100%;
            padding: 10px 15px;
            border: 1px solid var(--metallic-silver);
            border-radius: 20px 0 0 20px;
            outline: none;
        }

        .btn-search {
            padding: 10px 20px;
            background: var(--dark-accent);
            color: white;
            border: none;
            border-radius: 0 20px 20px 0;
            cursor: pointer;
        }

        .container { padding: 40px 5%; }

        .grid-produk {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 25px;
        }

        .card {
            background: rgba(255, 255, 255, 0.7);
            border-radius: 15px;
            overflow: hidden;
            transition: all 0.4s ease;
            border: 1px solid rgba(255,255,255,0.5);
            position: relative;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        }

        .card:hover { transform: translateY(-10px); background: rgba(255, 255, 255, 1); }

        .badge-diskon {
            position: absolute;
            top: 10px;
            right: 10px;
            background: #ff4757;
            color: white;
            padding: 5px 10px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: bold;
            z-index: 1;
        }

        .product-image-container {
            width: 100%;
            height: 250px;
            overflow: hidden;
            background: #f1f2f6;
        }

        .product-image-container img { width: 100%; height: 100%; object-fit: cover; }

        .info { padding: 20px; }

        .nama-barang { font-size: 1.1rem; font-weight: 600; margin-bottom: 8px; height: 45px; overflow: hidden; }

        .harga-asli { text-decoration: line-through; color: #a4b0be; font-size: 0.9rem; }

        .harga-final { color: #2f3542; font-size: 1.2rem; font-weight: bold; }

        .meta { display: flex; justify-content: space-between; margin-top: 15px; font-size: 0.85rem; color: #747d8c; }

        .btn-aksi {
            width: 100%; margin-top: 10px; padding: 12px; border: none; border-radius: 10px;
            background: var(--dark-accent); color: white; font-weight: bold; cursor: pointer; transition: 0.3s;
        }

        .rating { color: #f1c40f; }
    </style>
</head>
<body>

    <nav>
        <div class="logo">TECHS CLOTHING</div>
        <form class="search-container" action="index.php" method="GET">
            <input type="text" name="search" placeholder="Cari pakaian impianmu..." value="<?php echo htmlspecialchars($search); ?>">
            <button type="submit" class="btn-search">Cari</button>
        </form>
        <div class="cart-icon">🛒 Keranjang</div>
    </nav>

    <div class="container">
        <div class="grid-produk">
            <?php if (!empty($produk)): ?>
                <?php foreach ($produk as $p): ?>
                <div class="card">
                    <?php if ($p['diskon'] > 0): ?>
                        <div class="badge-diskon">Disc <?php echo $p['diskon']; ?>%</div>
                    <?php endif; ?>
                    
                    <div class="product-image-container">
                        <img src="<?php echo $p['img']; ?>" alt="<?php echo $p['nama']; ?>">
                    </div>

                    <div class="info">
                        <div class="nama-barang"><?php echo $p['nama']; ?></div>
                        
                        <?php if ($p['diskon'] > 0): 
                            $harga_diskon = $p['harga'] - ($p['harga'] * $p['diskon'] / 100);
                        ?>
                            <div class="harga-asli">Rp <?php echo number_format($p['harga'], 0, ',', '.'); ?></div>
                            <div class="harga-final">Rp <?php echo number_format($harga_diskon, 0, ',', '.'); ?></div>
                        <?php else: ?>
                            <div class="harga-final">Rp <?php echo number_format($p['harga'], 0, ',', '.'); ?></div>
                        <?php endif; ?>

                        <div class="meta">
                            <span class="rating">★ <?php echo $p['rating']; ?></span>
                            <span>Terjual <?php echo $p['terjual']; ?>+</span>
                        </div>

                        <p style="font-size: 0.8rem; color: #ff4757; margin-top: 10px;">Sisa Stok: <?php echo $p['stok']; ?></p>

                        <button class="btn-aksi" onclick="alert('Berhasil ditambah ke keranjang!')">+ Keranjang</button>
                        <a href="checkout.php?id=<?php echo $p['id']; ?>" style="text-decoration: none;">
                            <button class="btn-aksi" style="background: transparent; border: 1px solid black; color: black;">
                                Beli Sekarang
                            </button>
                        </a>
                    </div>
                </div>
                <?php endforeach; ?>
            <?php else: ?>
                <div style="grid-column: 1/-1; text-align: center; padding: 50px;">
                    <h3>Barang tidak ditemukan atau Server Python mati.</h3>
                </div>
            <?php endif; ?>
        </div>
    </div>

</body>
</html>