// after loaded
$('document').ready(function(){console.log('hello world');});

$('button#demo1').click(
    function(){
        $('p#demo1').hide();
    }
);
/*
$("*")
$(this)

.class
#id
ele --- div
[href] --- a[target='_blank'] a[target!='_blank']
:type  --- :button就是type='button'
:even :odd

p:first
ul li:first-child
*/
$('button#demo1').dblclick(
    function(){
        alert('double click!');
    }
);
$('p#demo1').mousedown(
    function(){
        $('p#demo1').text('o((>ω< ))o');
    }
);
$('p#demo1').mouseup(
    function(){
        $('p#demo1').text('\(￣︶￣*\))');
    }
);
/*
$('p#demo1').mouseenter(
    function(){
        $('p#demo1').text('hello');
    }
);
$('p#demo1').mouseleave(
    function(){
        $('p#demo1').text('bye');
    }
);
等于
*/
$('p#demo1').hover(
    function(){
        $('p#demo1').text('hello');
    },
    function(){
        $('p#demo1').text('bye');
    }
);
$('button#demo1').focus(function(){$('button#demo1').css('background-color','red');});
$('button#demo1').blur(function(){$('button#demo1').css('background-color','white');});

$('button#demo2').click(
    function(){
        $('p#demo1').show(
            1000, 'swing',
            function(){
                console.log('done');
            }    
        );
    }
);

$('button#demo3').click(
    function(){
        $('div#demo3').animate({
            width: '200px',
            height: '-=10px',
        },'fast');
    }
);

$('button#demo4').click(
    function(){
        console.log($('a#demo4').text());
        console.log($('a#demo4').html());
        console.log($('a#demo4').attr('href'));
        console.log($('input#demo4').val());
    }
);
// .text(...) .html(...)
$('#demo5').click(
    function(){
        $('input#demo4').val(
            function(i,o){ // 被选元素列表中当前元素的下标, 旧值
                console.log(i + ' ' + o);
                return 'hello!';
            }
        );
        $('a#demo4').text('go to ');
        $('a#demo4').attr('href','https://example.com'); // .attr( { ... } )

        $('a#demo4').append('example.com');
        $('a#demo4').prepend("click => "); // 可多个
        // .after() .before() 元素外前后添加
    }
);

$('button#demo6-1').click(function(){  $('p#demo6-1').remove()  });
$('button#demo6').click(function(){  $('div#demo6').remove()  });

// .addClass() .removeClass() .toggleClass()
// .width() .height() // 包括内边距 .innerWidth() .innerHeight() // 再包括边框 .outerWidth() .outerHeight()

$('#demo7').load('ajaxtest.txt h2',function(responseTxt,statusTxt,xhr){console.log(responseTxt + '\n' + statusTxt + '\n' + xhr);});
// $(...).load()
$.get('ajaxtest.txt' , function(data,stutus){console.log(data + '\n' + stutus);});
// $.get( URL [, data ] [, callback ] [, dataType ] ) // $.post()同
