var a = 1;
var b = '50', c;
c = a + b;
console.log(a,b,c);
//var a = 1,
//b = "50",
//c = a + b;

{let d = 0;}
function test1(){var d = 0;}
// d is not defined
{var d = 0;}
// defined
function test1(){console.log(d)};
test1(); // can use

var d = 7;
for (var d = 0; d < 10; d++) {
    console.log(d);
}

e = 1;
var e; // 提升，在声明前可定义，let不可以
e++;
e;
e--;
e;

const f = 114514;
f; // 不可重新赋值，类似let
const g = {key1:"", key2:1919810};
g;
g.key1 = '114514';
g;
//g = {} //还是不行

console.log(typeof 6);
console.log(typeof null);
console.log(typeof undefined);
console.log(undefined == null);
console.log(undefined === null);

function test1(a,b){
    return a + b
}
console.log(test1(1,1));

var h = {h_1:'hello', 
    h_2:"world", 
    h_3:function(){
        return this.h_1 + this.h_2
    }
};
h;
console.log(h.h_3());
console.log(h['h_1']);

console.log('aaaaa'.length);
console.log('abcabc'.indexOf('c'));
console.log('abcabc'.lastIndexOf('c'));
console.log('abcabc'.lastIndexOf('d'));
console.log('abcabc'.slice(2,4));
console.log('abcabc'.slice(-4));
console.log('hello e'.replace('e','a'));
console.log('hello e'.replace(/e/g,'a'));
console.log('hellO'.toUpperCase());console.log('WorLD'.toLowerCase());
console.log('      hello     '.trim());
console.log('hell word'.charAt(0));console.log('hell word'.charCodeAt(0));console.log('hell word'[0]);
console.log('a b c'.split(' '));
console.log("The rain in SPAIN stays mainly in the plain".match(/ain/g));
console.log('hello world'.includes('ll'));console.log('hello world'.startsWith('he'));console.log('hello world'.endsWith('ld'));

var i = `is ${(a + 10)}`;

(10).toString();
(9.52863).toFixed(2);
Number(true); Number("10"); Number("  10"); Number(new Date());
parseInt("10.33"); parseInt("10 20 30"); parseInt("10 years"); parseFloat("10.33");
Number.isInteger(114514);

var j;
j = ['a','b','c'];
j[0] = 'd';
j.length;
j.sort();
j.push('e');
j[j.length] = 'f'
j[10] = 'g'
Array.isArray(j);
console.log(j.toString());
console.log(j.join('-'));
j.push('a'); j.pop();
console.log(j.push('a')); console.log(j.pop());
j.shift(); j.unshift('a');
delete j[1];
j.splice(8,2,'h','i','j');
j.splice(2,1);
j = ['a','b','c']; j = j.concat(['d','e'],['f','g']);
console.log(j.slice(3,6));
j.reverse();
j = [10,5,300]; j.sort(function(a,b){return a - b});
j.sort(function(a, b){return 0.5 - Math.random()});
console.log(Math.max(1,2,3,4,5));

j.forEach(test1);
function test1(value, index, array){
    console.log(value + ' ' + index)
};
j = j.map(function(value){return value / 2;});
j = j.filter(function(value){return value > 3;});
console.log(j.every(function(value){return value > 10;}));
console.log(j.some(function(value){return value > 10;}));
j = [1,2,3,4,5,4,3,2,1]; console.log(j.indexOf(3)); console.log(j.lastIndexOf(3));
console.log(j.find(function(value){return value > 2;})); console.log(j.findIndex(function(value){return value > 2;}));

console.log(new Date()); console.log(new Date(2024,1,2, 11,19,0)); console.log(new Date(114514));
console.log((new Date()).toDateString()); console.log(new Date("2024")); console.log(new Date("2024-02-02T12:00:00"));
console.log(new Date("2/1/2024"));
console.log((new Date()).getDate()); console.log((new Date()).getDay());
// getMilliseconds() getMinutes() getMonth() getSeconds() getTime() getFullYear() getHours()
console.log((new Date()).setFullYear(2077));

Math.PI;
Math.round(6.8); Math.round(2.3);
Math.pow(8, 2); Math.sqrt(64);
Math.abs(-1) // 绝对值
Math.ceil(6.4); Math.floor(2.7); // 向上/下取整
Math.sin(30 * Math.PI / 180); Math.sin(30 * Math.PI / 180); Math.tan(30 * Math.PI / 180);
Math.min(0, 450, 35, 10, -8, -300, -78); Math.max(0, 450, 35, 10, -8, -300, -78);
Math.SQRT2 // 根号2
Math.random();
Math.floor(Math.random() * 10); // 0~9

Boolean(0); Boolean(''); //false
Boolean(114514); Boolean('1919810'); Boolean('false'); //true
true && false // and
true || false // or
!false // not

if (1 + 1 == 2) {
    console.log('fuck')
} else if (1 + 1 == 3) {
    console.log('you')
} else {
    console.log('too')
}
switch (new Date().getDay()) {
    default:
        console.log('懒');
        break;
    case 0:
    case 6:
        console.log('weekend');
        break;
    case 1:
        console.log('Mon.');
        break;
    case 5:
        console.log('Fri.');
} 

for (i = 0; i < 5; i++) { // 开始前执行;条件;完成一次循环后执行 // for (;i < len;) 条件可省，但可能搞崩浏览器
    console.log(i)
}
var i;
for (i in [0,1,2]) {console.log(i);};
for (let i of 'object') {console.log(i)};

var i = 0;
while (i < 10) {
    i++;
};
i // 10
do {
    console.log('do-while');
} while (false);

list:{
    console.log('not break');
    break list;
    console.log('break');
}

String(123);String(true);false.toString();
Number("3.14");Number(true);
+ '5'

"hello WORLD".search(/world/i);
"hello world".replace(/hello/i,"hell");
/e/.test("The best things in life are free!");
/e/.exec("The best things in life are free!");

try {
    throw "error message";
} catch(err) {
    console.log(err)
} finally {
    console.log('100%run')
}

test2()
function test2(){
    k = 100;
};
console.log(k);
console.log(window.k);

console.log(l);
var l = 10;  // var l 可以

k = this;
console.log(k); // [object window]
function test1(){return this};
console.log(test1()); // [object window]
k = {a:'114',b:514,c:function(){return this;}};
console.log(k.c()); // k

k = (v) => 'hello' + v;
console.log(k(' world'));
// 此时的this：函数拥有者

class cl1{
    constructor(cl2,cl3){ // def __init__(...):
        this.cl2 = cl2
        this.cl3 = cl3
    }
    cl4(){
        return this.cl2 + this.cl3
    }
};
k = new cl1('114','514');
console.log(k.cl4());

k = '{ "employees" : [' +
'{ "firstName":"Bill" , "lastName":"Gates" },' +
'{ "firstName":"Steve" , "lastName":"Jobs" },' +
'{ "firstName":"Alan" , "lastName":"Turing" } ]}';
k = JSON.parse(k);
console.log(k);

//debugger;

console.log(k = 114514);
10 == '10';
10 === '10'; // switch是这个
0.1 + 0.2;
k = 
"hello";
k = "he\
llo";

var k = {
    aa: 114,
    get bb(){
        return this.aa;
    },
    set cc(v){
        this.aa = v;
    }
};
k.cc = 514;
console.log(k.bb);
//
var k = {dd:0};
Object.defineProperty(k,'set',{
    get:function(){
        return this.dd
    }
});
console.log(k.set)

function m(aa,bb,cc){
    this.aa = aa;
    this.bb = bb;
    this.cc = cc;
};
var k = new m(11,45,14);
k.dd = 19;
k.ee = function(){return 19};
console.log(k.aa);console.log(k.dd);console.log(k.ee);

l = new Set(['a','b','c']);
l.add('d');
console.log(l);

l = new Map([
    ['a',1],
    ['b',2],
    ['c',3]
]);
l.set('d',4);
l.set('a',5);
console.log(l.get('a'));
console.log(l.size);
l.delete('b');
console.log(l);
l.clear();

l = new Map([['a',1],['b',2],['c',3]]);
console.log(l.has('a'));

l = ['a','b','c'];
Object.defineProperty(l,2,{value:'d'});
console.log(l);

(function(){
    console.log('helo wold');
}) (); //(function(){console.log('helo wold');})(); //console.log('helo wold');

function test1(b) {
    console.log(this.a + b);
};
test1.call({a:'114514'},'1919810');
test1.apply({a:'114514'},['1919810']);
Math.max.apply(null, [1,2,3]);

var test2 = (
    function () {
        var counter = 0;
        return function () {
            return counter += 1;
        }
    }
)();
test2();
test2();
console.log(test2());

// 类的继承
//class cl1{constructor(cl2,cl3){this.cl2 = cl2;this.cl3 = cl3;}cl4(){return this.cl2 + this.cl3;}};
class cl5 extends cl1 {
    constructor(cl2,cl3,cl6){
        super(cl2,cl3);
        this.cl6 = cl6;
    }
    cl7(){
        return this.cl2 + this.cl3 + this.cl6
    }
}
console.log((new cl5('11','45','14')).cl7())

class cl8{
    constructor(cl9){
        this.cl9 = cl9;
    }
    static cl10(x){
        return x.cl9
    }
};
console.log(cl8.cl10(new cl8('fuck')));

//async
function test3(){
    console.log('u');
};
setTimeout(test3,10);
setTimeout( function(){ test3(); } ,10);
//
var test3;
setInterval(test3, 1000); // loop 1000ms=1time
function test3() {
  let d = new Date();
  document.getElementById("timenow").innerHTML=
  d.getHours() + ":" +
  d.getMinutes() + ":" +
  d.getSeconds();
}
//
var j;
j = new Promise(
    function(ifnormal,iferror){
        if (true){
            ifnormal('succeed');
        } else {
            iferror('error');
        }
    }
);
j.then(
    function(v){console.log(v);}, // succeed
    function(v){console.log(v);} // error
);
//
async function test5(){
    throw 'shit'
    return 'Genshin Launch!'
};
test5().then(
    function(v){console.log(v);},
    function(v){console.log(v);}
);
//
async function test6(){
    let test6_1 = new Promise(function(res,rej){
        setTimeout(function(){res('done')},3000);
    });
    console.log(await test6_1);
};
test6();









