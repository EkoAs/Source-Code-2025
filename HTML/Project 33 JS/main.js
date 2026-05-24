// 

function cek_Pass(){
    var password = prompt("Masukan angka");
    if(password == "111"){
        document.writeln("<h2>Selamat datang di halaman ini</h2>");
    }else{
        document.writeln("<h2>Password yang anda masukan salah</h2>");
    }

    }
cek_Pass(password);


// INPUT NILAI DAN GRADE
function nilai(){
    var nilai=prompt("Masukkan Nilai Anda :");
    var grade="";

    if(nilai >= 90){
    grade="A";
    } else if(nilai >= 80){
    grade="B+";
    } else if(nilai >= 70){
    grade="B";
    } else if(nilai >= 60){
    grade="C+";
    } else if(nilai >= 50) {
    grade="C";
    } else if(nilai >= 40){
    grade="D";
    } else if(nilai >= 30){
    grade="E";
    }
    else{
    grade="F";
    }
    document.writeln(`<p> Nilai Anda : ${grade} </p>`);
}

nilai();


function bagian_A(){
    var salesman = prompt("Masukan penjualan barang: ");
    var komisi = 0;
    if(salesman >= 200000 && salesman <= 300000){
        komisi = salesman * 0.1;
        komisi += 10000;
        document.writeln(`<p> Komisi Anda : ${komisi} dari pendapatan awal ${salesman} </p>`);
        
    }else if(salesman >= 300000 && salesman <= 500000){
        komisi = salesman * 0.15;
        komisi += 20000;
        document.writeln(`<p> Komisi Anda : ${komisi} </p>`);
    }else if(salesman >= 500000){
        komisi = salesman * 0.2;
        komisi += 30000;
        document.writeln(`<p> Komisi Anda : ${komisi} </p>`);
    }else{
        document.writeln("<p> Penjualan Anda kurang </p>");
    }
}