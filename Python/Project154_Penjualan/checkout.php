<?php
// 1. Ambil ID dari URL (Contoh: checkout.php?id=1)
$product_id = isset($_GET['id']) ? $_GET['id'] : null;

if (!$product_id) {
    echo "Pilih produk terlebih dahulu!";
    exit;
}

// 2. Ambil detail produk dari API Python
$url = "http://127.0.0.1:5000/api/produk"; // URL API kita
$response = @file_get_contents($url);
$all_products = json_decode($response, true);

// Cari produk yang sesuai dengan ID
$item = null;
if ($all_products) {
    foreach ($all_products as $p) {
        if ($p['id'] == $product_id) {
            $item = $p;
            break;
        }
    }
}

if (!$item) {
    echo "Produk tidak ditemukan!";
    exit;
}

// 3. Logika Perhitungan (Matematika Bisnis)
$harga_awal = $item['harga'];
$diskon_rp = ($item['diskon'] / 100) * $harga_awal;
$subtotal = $harga_awal - $diskon_rp;

$ongkir = 15000; // Contoh ongkir flat
$pajak = 0.11 * $subtotal; // PPN 11%
$total_bayar = $subtotal + $ongkir + $pajak;

?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkout - Septian Clothing</title>
    <style>
        :root {
            --shiny-white: #fcfcfc;
            --dark-gray: #2d3436;
            --border-color: #dfe6e9;
        }

        body {
            font-family: 'Segoe UI', sans-serif;
            background: #f0f2f5;
            margin: 0;
            padding: 20px;
            color: var(--dark-gray);
        }

        .checkout-container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        }

        h2 { border-bottom: 2px solid #f1f2f6; padding-bottom: 10px; margin-top: 0; }

        .item-row {
            display: flex;
            justify-content: space-between;
            padding: 15px 0;
            border-bottom: 1px solid var(--border-color);
        }

        .summary-section {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }

        .flex-row { display: flex; justify-content: space-between; margin-bottom: 10px; }
        .total-bold { font-size: 1.4rem; font-weight: bold; color: #d63031; margin-top: 10px; }

        .payment-method {
            margin-top: 30px;
            padding: 20px;
            border: 2px solid var(--border-color);
            border-radius: 10px;
        }

        select, button {
            width: 100%;
            padding: 12px;
            margin-top: 10px;
            border-radius: 8px;
            font-size: 1rem;
            border: 1px solid #ccc;
        }

        .btn-bayar {
            background: var(--dark-gray);
            color: white;
            border: none;
            cursor: pointer;
            font-weight: bold;
            transition: 0.3s;
            margin-top: 20px;
        }

        .btn-bayar:hover { background: #000; transform: scale(1.02); }
    </style>
</head>
<body>

<div class="checkout-container">
    <a href="index.php" style="text-decoration: none; color: #636e72; font-size: 0.9rem;">← Kembali Belanja</a>
    <h2>Rincian Pesanan</h2>
    
    <div class="item-row">
        <div>
            <strong style="display:block;"><?php echo $item['nama']; ?></strong>
            <small style="color: #b2bec3;">Harga Satuan: Rp <?php echo number_format($item['harga'], 0, ',', '.'); ?></small>
        </div>
        <span>Rp <?php echo number_format($subtotal, 0, ',', '.'); ?></span>
    </div>

    <div class="summary-section">
        <div class="flex-row">
            <span>Subtotal (Setelah Diskon)</span>
            <span>Rp <?php echo number_format($subtotal, 0, ',', '.'); ?></span>
        </div>
        <div class="flex-row">
            <span>Ongkos Kirim</span>
            <span>Rp <?php echo number_format($ongkir, 0, ',', '.'); ?></span>
        </div>
        <div class="flex-row">
            <span>Pajak (PPN 11%)</span>
            <span>Rp <?php echo number_format($pajak, 0, ',', '.'); ?></span>
        </div>
        <hr style="border: 0; border-top: 1px solid #ccc;">
        <div class="flex-row total-bold">
            <span>Total Bayar</span>
            <span>Rp <?php echo number_format($total_bayar, 0, ',', '.'); ?></span>
        </div>
    </div>

    <form action="receipt.php" method="POST" class="payment-method">
        <input type="hidden" name="nama_barang" value="<?php echo $item['nama']; ?>">
        <input type="hidden" name="total" value="<?php echo $total_bayar; ?>">
        <input type="hidden" name="id_barang" value="<?php echo $item['id']; ?>">

        <label for="metode">Pilih Metode Pembayaran:</label>
        <select name="metode" id="metode" required onchange="toggleCode(this.value)">
            <option value="cod">COD (Bayar di Tempat)</option>
            <option value="transfer">Transfer Bank (Virtual Account)</option>
            <option value="e-wallet">E-Wallet (OVO/Dana/Gopay)</option>
        </select>

        <div id="info-pembayaran" style="margin-top: 15px; color: #636e72; font-size: 0.9rem; display: none;">
            * Kode pembayaran akan muncul di struk belanja setelah klik bayar.
        </div>

        <button type="submit" class="btn-bayar">PROSES PEMBAYARAN</button>
    </form>
</div>

<script>
    function toggleCode(val) {
        const info = document.getElementById('info-pembayaran');
        info.style.display = (val !== 'cod') ? 'block' : 'none';
    }
</script>

</body>
</html>