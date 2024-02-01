let bg = document.querySelector('.mouse-parallax-bg');
let bgWidth = bg.clientWidth;
let bgHeight = bg.clientHeight;

window.addEventListener('mousemove', function(e) {
    let x = e.clientX / window.innerWidth;
    let y = e.clientY / window.innerHeight;

    // Устанавливаем ограничения для трансформации, основываясь на размерах фона
    let maxTransX = bgWidth - window.innerWidth;
    let maxTransY = bgHeight - window.innerHeight;

    // Ограничиваем значения, чтобы они не выходили за пределы фона
    let transX = Math.max(-maxTransX, Math.min(0, -x * 50));
    let transY = Math.max(-maxTransY, Math.min(0, -y * 50));

    bg.style.transform = 'translate(' + transX + 'px, ' + transY + 'px)';
});1