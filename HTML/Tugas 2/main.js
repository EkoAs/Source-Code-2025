function cekHarga() {
    const harga = parseFloat(document.getElementById("harga").value);
    if (isNaN(harga)) {
        document.getElementById("hasil").textContent = "Harap masukkan angka yang valid.";
        return;
    }

    
    let kategori;
    if (harga < 500) {
        kategori = "Barang tidak ada.";
    } else if (harga < 4000) {
        kategori = "Murah.";
    } else if (harga <= 7500) {
        kategori = "Sedang.";
    } else if (harga <= 10000) {
        kategori = "Mahal.";
    } else {
        kategori = "Barang tidak ada.";
    }
    document.getElementById("hasil").textContent = `Kategori harga: ccccccccc${kategori}`;
}