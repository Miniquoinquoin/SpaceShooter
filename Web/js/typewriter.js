import Typewriter from '../module/typeWriter/core';

var titre = document.getElementById("typewriter");

const typewriter = new Typewriter(titre, {
    loop: false,
    cursor: '',
});

typewriter.pauseFor(12000)
    .typeString('Space <br>Shooter')
    .start();