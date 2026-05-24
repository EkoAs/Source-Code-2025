<?php
// Ambil data yang dikirim dari checkout.php via POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header("Location: index.php");
    exit;
}

$nama_barang = $_POST['nama_barang'];
$id_barang = $_POST['id_barang'];
$metode = $_POST['metode'];
$total = $_POST['total'];

// Data tambahan untuk struk
$waktu = date("d/m/Y H:i:s");
$kode = ($metode !== 'cod') ? strtoupper(substr(md5(time()), 0, 10)) : "BAYAR DI TEMPAT";

// Simulasi perhitungan detail untuk struk (biar angkanya pas)
$pajak = $total * (11/111); // Hitung mundur pajak dari total
$ongkir = 15000;
$subtotal = $total - $pajak - $ongkir;
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Struk Pembayaran - Asif Clothing</title>
    <style>
        body {
            background: #dfe6e9;
            font-family: 'Courier New', Courier, monospace;
            padding: 40px;
            display: flex;
            justify-content: center;
        }

        .struk-box {
            width: 100%;
            max-width: 500px;
            background: white;
            border: 1px solid #eee;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        .header { text-align: center; border-bottom: 2px dashed #000; padding-bottom: 20px; }
        .header h1 { margin: 0; font-size: 1.5rem; }

        .info-transaksi { margin: 20px 0; font-size: 0.9rem; }
        
        .tabel-barang { width: 100%; border-collapse: collapse; margin: 20px 0; }
        .tabel-barang td { padding: 5px 0; }

        .total-section { border-top: 2px dashed #000; padding-top: 15px; }
        .row { display: flex; justify-content: space-between; margin-bottom: 5px; }

        .kode-bayar {
            background: #f1f2f6;
            text-align: center;
            padding: 15px;
            margin: 20px 0;
            border: 1px solid #ccc;
        }

        .btn-print {
            display: block;
            width: 95%;
            padding: 12px;
            background: #2d3436;
            color: white;
            text-align: center;
            text-decoration: none;
            margin-top: 20px;
            border-radius: 5px;
            font-weight: bold;
        }

        @media print {
            .btn-print { display: none; }
            body { background: white; padding: 0; }
        }
    </style>
</head>
<body>

<div class="struk-box">
    <div class="header">
        <h1>ASIF CLOTHING STORE</h1>
        <p>Jl. Fashionable No. 1, Jakarta</p>
        <p><?php echo $waktu; ?></p>
    </div>

    <div class="info-transaksi">
        <p>Metode: <?php echo strtoupper($metode); ?></p>
        <p>Status: PROSES</p>
    </div>

    <table class="tabel-barang">
        <tr>
            <td><?php echo $nama_barang; ?></td>
            <td style="text-align: right;">Rp <?php echo number_format($subtotal, 0, ',', '.'); ?></td>
        </tr>
    </table>

    <div class="total-section">
        <div class="row">
            <span>Subtotal:</span>
            <span>Rp <?php echo number_format($subtotal, 0, ',', '.'); ?></span>
        </div>
        <div class="row">
            <span>Ongkir:</span>
            <span>Rp <?php echo number_format($ongkir, 0, ',', '.'); ?></span>
        </div>
        <div class="row">
            <span>Pajak (11%):</span>
            <span>Rp <?php echo number_format($pajak, 0, ',', '.'); ?></span>
        </div>
        <div class="row" style="font-weight: bold; font-size: 1.2rem; margin-top: 10px;">
            <span>TOTAL:</span>
            <span>Rp <?php echo number_format($total, 0, ',', '.'); ?></span>
        </div>
    </div>

    <?php if ($metode !== 'cod'): ?>
    <div class="kode-bayar">
        <small>Silakan transfer ke nomor Virtual Account berikut:</small>
        <h2 id="kode"><?php echo $kode; ?></h2>
        <button onclick="copyCode()" style="cursor:pointer; font-size: 0.7rem;">Salin Kode</button>
    </div>
    <?php else: ?>
    <div class="kode-bayar">
        <strong>PEMBAYARAN COD</strong><br>
        <small>Siapkan uang tunai saat kurir tiba.</small>
    </div>
    <?php endif; ?>

    <a href="index.php" class="btn-print">KEMBALI KE BERANDA</a>
    <p style="text-align: center; font-size: 0.7rem; color: #999; margin-top: 20px;">Terima kasih telah berbelanja emuach</p>
</div>

<script>
    function copyCode() {
        const code = document.getElementById('kode').innerText;
        navigator.clipboard.writeText(code);
        alert("Kode disalin ke clipboard!");
    }
</script>

</body>
</html>