<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Neuro Tech | Transaction Receipt</title>
    <link rel="stylesheet" href="assets/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&family=Orbitron:wght@700&display=swap" rel="stylesheet">
    <style>
        body { background: #000; padding: 20px; }
        .cyber-receipt {
            background: #111;
            border: 2px solid var(--electric-yellow);
            max-width: 600px;
            margin: 0 auto;
            padding: 40px;
            position: relative;
            font-family: 'Courier Prime', monospace;
            color: #ddd;
        }
        .cyber-receipt::before {
            content: "NEURO_TECH_OFFICIAL_INVOICE";
            position: absolute;
            top: -12px;
            left: 20px;
            background: var(--electric-yellow);
            color: #000;
            font-size: 0.7rem;
            padding: 2px 10px;
            font-family: 'Orbitron';
        }
        .header-receipt {
            border-bottom: 1px dashed #444;
            padding-bottom: 20px;
            margin-bottom: 20px;
            text-align: center;
        }
        .item-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            font-size: 0.9rem;
        }
        .total-box {
            border-top: 2px solid var(--electric-yellow);
            margin-top: 30px;
            padding-top: 20px;
        }
        .barcode {
            margin-top: 40px;
            text-align: center;
            opacity: 0.7;
            filter: invert(1);
        }
        @media print {
            .btn-print { display: none; }
        }
    </style>
</head>
<body>

    <div class="cyber-receipt">
        <div class="header-receipt">
            <h1 style="font-family: 'Orbitron'; color: var(--electric-yellow); margin: 0;">NEURO TECH</h1>
            <p>SUPPLY & ASSEMBLY SYSTEM</p>
            <p style="font-size: 0.8rem;">ID: TXN-<?php echo rand(1000, 9999); ?> / DATE: <?php echo date('d-m-Y'); ?></p>
        </div>

        <div id="items-list">
            <div class="item-row">
                <span>[CPU] INTEL CORE I7-14700K</span>
                <span>RP 6.800.000</span>
            </div>
            <div class="item-row">
                <span>[VGA] MSI RTX 4070 SUPER</span>
                <span>RP 11.200.000</span>
            </div>
            </div>

        <div class="total-box">
            <div class="item-row" style="font-weight: bold; color: var(--electric-yellow); font-size: 1.2rem;">
                <span>TOTAL TRANSACTION</span>
                <span>RP 18.000.000</span>
            </div>
        </div>

        <div style="margin-top: 30px; padding: 15px; border: 1px solid #333; font-size: 0.8rem;">
            <p style="margin: 0; color: var(--electric-yellow);">PERFORMANCE ESTIMATION:</p>
            <p style="margin: 5px 0;">GTA V Ultra: 120+ FPS | Stable Temperature</p>
        </div>

        <div class="barcode">
            <img src="https://bwipjs-api.metafloor.com/?bcid=code128&text=NEURO-TECH-<?php echo time(); ?>&scale=2&rotate=N&includetext" alt="Barcode">
            <p style="font-size: 0.6rem; margin-top: 5px;">VERIFIED BY NEURO_ENGINE_V1.0</p>
        </div>
    </div>

    <div style="text-align: center; margin-top: 20px;">
        <button class="btn-yellow btn-print" onclick="window.print()">PRINT INVOICE</button>
        <a href="index.php" class="btn-yellow btn-print" style="text-decoration: none; background: #333; color: #fff; margin-left: 10px;">BACK TO SHOP</a>
    </div>

</body>
</html>