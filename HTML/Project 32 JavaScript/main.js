console.log("hello")

// alert("AKU RAJA KAU BUDAK")

var siteName = "javascript";
var url= "www.yandex.com";

function tambah() {
    var a = document.getElementById("div_kalimat");
    a.innerHTML += "<p>Hallo.......</p>";
}

function resets() {
    document.getElementById("div_kalimat").innerHTML = "";
}
let counter=0;
function variable(){
    var a = 100;
    var b = 200;
    var result = a + b;
    var benar = b > a;
    var salah = b < a;
    document.writeln('100 + 200 = ' + result + `<br/>`);


    var result2 = benar || salah;
    document.writeln(`${benar}} || ${salah} = ${result2}<br/>`);
    
    var result2 = benar && salah;
    document.writeln(`${benar} && ${salah} = ${result2}<br/>`);
    
    var result2 = !benar;
    document.writeln(`!${benar} = ${result2}<br/>`);

    // counter++;
    // document.getElementById("hasil").innerHTML=`Counter: ${counter}`;

}
