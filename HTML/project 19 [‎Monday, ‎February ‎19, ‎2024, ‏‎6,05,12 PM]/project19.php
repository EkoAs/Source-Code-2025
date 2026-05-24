<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to = "ekoasif8@gmail.com"; 
    $from = $_POST['email'];
    $message = $_POST['message'];
    $subject = "Pesan dari Form Kontak";

    $headers = "From: $from\r\n";
    $headers .= "Reply-To: $from\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    if (mail($to, $subject, $message, $headers)) {
        echo "Pesan telah terkirim. Terima kasih!";
    } else {
        echo "Maaf, pesan gagal terkirim.";
    }
}
?>