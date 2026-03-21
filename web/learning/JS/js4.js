console.log(document.getElementById('demo1').innerHTML);
document.getElementsByTagName('h1')[0].style.color = 'darkblue';
document.getElementById('demopic').src = 'https://dummyimage.com/250x180/000/fff.png&text=JS!';

document.getElementsByClassName('demo1')[0].onclick = function(){console.log('clicked');};
document.querySelectorAll('p#demo1')[0].innerHTML = 'Hell Word'

console.log(document.body);
console.log(document.cookie);
console.log(document.domain);
console.log(document.title);
console.log(document.URL);

//document.write(Date());

function testdemo1(){
    alert('click')
}
document.getElementById('demo2').addEventListener('click',function(){console.log(':P');});
document.getElementById('demo2').addEventListener('click',testdemo1);
document.getElementById('demo2').addEventListener('mouseover',function(){console.log('(happy)');});
window.addEventListener('resize',function(){console.log('resize!');});
document.getElementById('demo2').removeEventListener('click',testdemo1);

var demo3_child_p = document.createElement('p').appendChild(document.createTextNode('This is a text'));
document.getElementById('demo3').append(demo3_child_p);
document.getElementById('demo4').remove();
document.getElementById('demo5').replaceChild(document.createElement('p').appendChild(document.createTextNode('This is new text')),document.getElementById('demo6'))

console.log(window.innerWidth + ' ' + window.innerHeight);
console.log(screen.width + ' ' + screen.height);
console.log(screen.availWidth + ' ' + screen.availHeight);
console.log(screen.colorDepth);

console.log(location.href);console.log(location.hostname);console.log(location.pathname);

//history.back();history.forward();
console.log(navigator.cookieEnabled);
console.log(navigator.userAgent);
console.log(navigator.language);console.log(navigator.platform);console.log(navigator.onLine);

//alert("alert");console.log(confirm('confirm'));console.log(prompt('prompt','test'));

var cookiesoon = '';
cookiesoon += 'time=' + Date() + ';';
cookiesoon += 'expires=' + (new Date(new Date().getTime() + 300000)) + ';';
cookiesoon += 'path=/'
document.cookie = cookiesoon;
console.log(document.cookie);

function demo7_f() {
    if (! document.getElementById("demo7").checkValidity()) {
      alert(document.getElementById("demo7").validationMessage);
    }
};

console.log('last: ' + localStorage.getItem('time'));
localStorage.setItem('time',new Date());
console.log('now : ' + localStorage.getItem('time'));
console.log('====================================')
console.log('last: ' + sessionStorage.getItem('time'));
sessionStorage.setItem('time',new Date());
console.log('now : ' + sessionStorage.getItem('time'));

navigator.geolocation.getCurrentPosition(
    function(l){
        alert(l.coords.latitude);
        alert(l.coords.longitude);
        console.log(l.coords.accuracy);
        console.log(l.coords.altitude);console.log(l.coords.altitudeAccuracy);
        console.log(l.coords.heading);console.log(l.coords.speed);
    },
    function(e){
        switch(e.code){
            case e.PERMISSION_DENIED:
                console.log('用户不允许定位');
                break;
            case e.POSITION_UNAVAILABLE:
                console.log('定位不可用');
                break;
            case e.TIMEOUT:
                console.log('定位超时');
                // 为什么chrome偏要调用googleapi，firefox就没问题
                // 神奇的兼容性问题+1
                break;
            case e.UNKNOWN_ERROR:
                console.log('未知错误');
                break;
        }
    }
);
// navigator.geolocation.watchPosition() 实时更新到并执行函数 .clearWatch()停下来