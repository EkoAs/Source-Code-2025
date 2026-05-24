<?php
$nama = "Eko Asif Bahri";
$nim = "251351028";
$jurusan = "informatika";
$alamat = "Indonesia";

function nama() {
    global $nama;
    global $nim;
    global $jurusan; 
    global $alamat;
    echo "Nama saya ".$nama."\nNIM saya ".$nim."\nSaya dari jurusan ".$jurusan."\nAlamat saya di ".$alamat;
}

nama();    



?>