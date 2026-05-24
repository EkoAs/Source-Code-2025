<?php
  // $nilai = 81;
  // if($nilai >= 90 && $nilai <= 100){
  //   echo "Nilai anda A++";
  // }else if($nilai >= 80 && $nilai <= 89){
  //   echo "Nilai andaaa B++";
  // }else if($nilai >= 70 && $nilai <= 79){
  //   echo "Nilai andaaa c++";
  // }else if($nilai >=60 && $nilai <= 69){
  //   echo "Nilai andaaa d++";
  // }else{
  //   echo "Lulus coyyy!!";
  // }

//   $kartu = true;
//   $diskon = 0;
//   $belanja = 400;
  
//   if($kartu){
//     if($belanja > 100){
//       $diskon = 15;
//     }else if($belanja > 500){
//       $diskon = 50;
//     }else{
//       echo "Anda gak dapat diskonnn";
//     }
//   }else{
//       $diskon = 5;
//     }

// echo "Uang anda $belanja\n";  
// $total_bayar = $belanja - $diskon;

// echo "Diskon: Rp $diskon%\n";
// echo "Total bayar: Rp $total_bayar\n";

$hari = 3;

switch ($hari) {
    case 1:
        $nama_day = "Senin";
        break;
    case 2:
        $nama_day = "Selasa";
        break;
    case 3:
        $nama_day = "Rabu";
        break;
    case 4:
        $nama_day = "Kamis";
        break;
    case 5:
        $nama_day = "Jumat";
        break;
    case 6:
        $nama_day = "Saptu";
        break;
    case 7:
        $nama_day = "Minggu";
        break;
    case 8:
        $nama_day = "Senin lagi";
        break;
    default:
        $nama_day = "Invalid";
        break;
}

echo "hari ke-$hari adalah $nama_day\n";
?>
<?php



?>

