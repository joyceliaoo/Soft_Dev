// team JL - Jack Lu, Joyce Liao
// SoftDev1 pd8
// K29 -- Sequential Progression
// 2018-12-20

var fib = function (n){
    if (n < 2){
        return n;
    }
    else
        return fib(n-1) + fib(n-2);
}

var gcd = function(a ,b) {
    if ( a < b )
        var c = a;
    else
        var c = b;
    for (var i = c; i >= 1; i--) {
        if (a % i == 0 && b % i == 0)
            return i;
    }
    return 1;
}

var students = [
    "J", "A", "D", "E"
];

var randomStudent = function(){
    var i = Math.floor(Math.random() * students.length);

    return students[i];
}

var fibbut = document.getElementById("fib");
var gcdbut = document.getElementById("gcd");
var ranbut = document.getElementById("random");
// console.log(ranbut);

var get_fib_7 = function() {
    data = fib(7);
    console.log(data);
}

var get_gcd_2490 = function() {
    data = gcd(24,90);
    console.log(data);
}

var get_ran = function() {
    data = randomStudent();
    console.log(data);
}

fibbut.addEventListener('click', get_fib_7);
gcdbut.addEventListener('click', get_gcd_2490);
ranbut.addEventListener('click', get_ran);
