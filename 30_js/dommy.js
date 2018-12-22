// team_gg2: Susan Lin and Joyce Liao
// SoftDev1 pd8
// K#30: Sequential Progression III: Season of the Witch
// 2018-12-21


var changeHeading = function(e) {
    var h = document.getElementById("h")
    if (e.type == 'mouseover') {
        h.innerHTML = this.innerHTML;
    }
    else {
        h.innerHTML = "Hello World";
    }
};

var removeItem = function(e) {
    this.remove();
};

var lis = document.getElementsByTagName("li");

for(var i=0; i < lis.length; i++) {
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout', changeHeading);
    lis[i].addEventListener('click', removeItem);
};

var addItem = function(e) {
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    item.addEventListener('click', removeItem);
    list.appendChild( item );
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);


var fib = function(n) {
  //storing results of subproblems
  var result = [0, 1];
  for (var i = 2; i <= n; i++) {
    result.push(result[i-2] + result[i-1]);
  }

  return result[n];
};

var addFib = function(e){
    // console.log("button clicked");
    var fib_list = document.getElementById("fiblist");
    // console.log(fib_list);
    var fib_ele = document.createElement("li");
    var next_fib = fib(num_fib);
    num_fib += 1;
    // console.log(num_fib);
    fib_ele.innerHTML = next_fib;
    fib_list.appendChild(fib_ele);
};

var fibb = document.getElementById("fb");
fibb.addEventListener("click", addFib);
var num_fib = 1;
