function user_input() {
    // Panggil fungsi hitung
    hitung();
}

function hitung() {
    
    const nama = document.getElementById("nama").value;
    const nilaiUts = parseFloat(document.getElementById("nilaiUts").value);
    const nilaiUas = parseFloat(document.getElementById("nilaiUas").value);
    const nilaiMandiri = parseFloat(document.getElementById("nilaiMandiri").value);

    
    if (!nama) {
        document.getElementById("hasil").textContent = "Harap masukkan nama.";
        return;
    }
    if (isNaN(nilaiUts) || isNaN(nilaiUas) || isNaN(nilaiMandiri)) {
        document.getElementById("hasil").textContent = "Harap masukkan nilai yang valid.";
        return;
    }

    
    const nilaiAwal = {
        uts: nilaiUts,
        uas: nilaiUas,
        mandiri: nilaiMandiri,
    };

    
    // const nilaiAkhir = (nilaiUts * 0.15) + (nilaiUas * 0.45) + (nilaiMandiri * 0.20);
    const nilaiU = (nilaiUts * 0.15);
    const nilaiUA = (nilaiUas * 0.45);
    const nilaiM = (nilaiMandiri * 0.40);
    const nilaiAkhir = nilaiU + nilaiUA + nilaiM;
    
    
    document.getElementById("hasil").innerHTML = `
        <p>Nama: ${nama}</p>
        <p>Nilai Murni yang didapat:</p>
        <ul>
            <li>Nilai Murni UTS: ${nilaiU.toFixed(2)}</li>
            <li>Nilai Murni UAS: ${nilaiUA.toFixed(2)}</li>
            <li>Nilai Murni Mandiri: ${nilaiM.toFixed(2)}</li>
        </ul>
        <p>Nilai Akhir yg diperoleh: ${nilaiAkhir.toFixed(2)}</p>
    `;
}