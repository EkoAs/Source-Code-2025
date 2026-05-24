
// menggungakan foor loop
// (deklarasi; kondisi; increment/decrement) mirid C++
function loopingFor(){
    for(let i =0;i<10;++i){
        console.log(`loop ${i}`);
    }
}

// while loop 
function whileLoop(){
    var count= 0
    while(repreat <= 10){
        var jawaban = confirm('lagi?');
        count++;
        if(!jawaban) break;
    }
}
// lakukan sekali dulu,baruk cek kondiisi dia akhir
function doWhileLoop(){
    var counter = 0;
    do{
        counter++;
        var jawaban = confirm('lagi?');
    } while(jawaban);
}


function hitung_Genap(){
    var num = 0
    for(let i=1;i<=20;++i){
        if(i % 2 == 0){
            num += i;
        } else{
            continue;
        }
        console.log(`Angka ke ${i}`)
    }
    console.log(`Jumlah bilangan genap dari 1 sampai 20 adalah ${num}`);
}

function bilanganPrima() {
    for (let num = 2; num <= 20; num++) {
        let isPrime = true;
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            console.log(`Bilangan prima: ${num}`);
        }
    }
}
// function prima(){
//     var num = 0
//     for(let i=2;i<=20;++i){
//         if(i % 2 != 0){
//             num += i;
//         } else{
//             continue;
//         }
//         console.log(`angka ke ${i}`)
//     }
   
// }
hitung_Genap();    
bilanganPrima();