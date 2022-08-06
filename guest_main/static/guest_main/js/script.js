var head = document.querySelector('header');
var achieves = document.querySelectorAll('.achievement');
var achieve = Array.from(achieves);
var header_menu_button = document.querySelector('.header_burger_open');
var header_menu = document.querySelector('.header_burger_menu')
var marker = true;
var btn = new Map();
var btns = document.querySelectorAll('.our_companions-buttons');
var slides_block = document.querySelector('.carousel-inner')
var slides = slides_block.querySelectorAll('.carousel-item');
var element = document.querySelector('.about_us-statistics');
for (i = 0; i < achieve.length; i++) {
    achieve[i].innerHTML = 0;
}
header_menu_button.onclick = function() {
    header_menu.classList.toggle('left');
}

var header_menu_height = window.innerHeight - head.clientHeight;

header_menu.style.top = head.clientHeight + 'px';
header_menu.style.height = header_menu_height + 'px';


function Statistic() {
    nums = []
    var maxnum = 0;
    for (i = 0; i < achieve.length; i++) {
        num = achieve[i].getAttribute('tag');
        nums[i] = num;
    }
    maxnum = Math.max(...nums);

    function Counter(element, int, lim) {
        if (int <= lim) {
            element.innerHTML = int;
            if (int > 999 && lim - int > 100) int = int + 50;
            else if (int > 99 && lim - int > 10) int = int + 10;
            else int++;
            setTimeout(Counter, 800 / lim, element, int, lim);
        }
    }
    for (i = 0; i < achieve.length; i++) {
        var j = 0;
        Counter(achieve[i], j, nums[i])
    }
}

var Visible = function(target) {
    // Все позиции элемента
    var targetPosition = {
            top: window.pageYOffset + target.getBoundingClientRect().top,
            left: window.pageXOffset + target.getBoundingClientRect().left,
            right: window.pageXOffset + target.getBoundingClientRect().right,
            bottom: window.pageYOffset + target.getBoundingClientRect().bottom
        },
        // Получаем позиции окна
        windowPosition = {
            top: window.pageYOffset,
            left: window.pageXOffset,
            right: window.pageXOffset + document.documentElement.clientWidth,
            bottom: window.pageYOffset + document.documentElement.clientHeight
        };

    if (windowPosition.top > 0) {
        head.style.position = 'fixed';
        head.style.top = 0;
    } else {
        head.style.position = null;
        head.style.top = null;
    }

    if (targetPosition.top < windowPosition.bottom && marker) { // Если позиция левой стороны элемента меньше позиции правой чайти окна, то элемент виден справа
        // Если элемент полностью видно, то запускаем следующий код
        Statistic()
        marker = false
    }
};

// Запускаем функцию при прокрутке страницы
window.addEventListener('scroll', function() {
    Visible(element);
});

// А также запустим функцию сразу. А то вдруг, элемент изначально видно
Visible(element);

// Слайдер

for (var i = 0; i < btns.length; i++) {
    this['btn'.concat(i + 1)] = btns[i];
    Checker(this['btn'.concat(i + 1)]);
}

function Checker(vals) {
    var val = '';
    window.onload = function() {
        var show = true;
        val = btn1.getAttribute('pk');
        Styles(btn1);
        for (let j = 0; j < slides.length; j++) {
            slides[j].classList.remove('active');
            slides_block.appendChild(slides[j]);
            if (slides[j].getAttribute('name') != val) {
                slides[j].remove();
            } else if (show == true) {
                slides[j].classList.add('active');
                show = false;
            }
        }
    }
    vals.onclick = function() {
        var show = true;
        val = vals.getAttribute('pk');
        Styles(vals);
        for (let j = 0; j < slides.length; j++) {
            slides[j].classList.remove('active');
            slides_block.appendChild(slides[j]);
            if (slides[j].getAttribute('name') != val) {
                slides[j].remove();
            } else if (show == true) {
                slides[j].classList.add('active');
                console.log(slides[j]);
                show = false;
            }
        }
    }
}

function Styles(val) {
    for (var i = 0; i < btns.length; i++) {
        btns[i].style.fontFamily = 'var(--main_font)';
    }
    val.style.fontFamily = 'var(--title_font)';
}