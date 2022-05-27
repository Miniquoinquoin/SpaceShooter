// Fichier de detection du scroll et de lancement des actions

function Anim(name) {
    if (name == 'Intro') {
        for (element of document.getElementsByClassName('ParagrapheIntro')) {
            element.classList.add('Intro__animation');
        } 
    }

    else if (name == 'Mode') {
        var compt = 0;
        for (element of document.getElementsByClassName('Separation__bar')) {
            compt++;
            element.classList.add('Separation__bar__animation__' + compt.toString());
        } 
        document.getElementById('Campagne').classList.add('Campagne__animation');
        document.getElementById('Infini').classList.add('Infini__animation');

    }
    
}

// Check si l'element passé en param est affiché sur l'écran
function checkVisible(elm) {
    var rect = elm.getBoundingClientRect();
    var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
    return !(rect.bottom < 0 || rect.top - viewHeight >= -200);
}

//Regarde si une div est affichée toutes les 250ms puis désactive l'interval



function NewScrollReveal(variable ,name) {
    variable = setInterval(function () {
        if (checkVisible(document.getElementById(name))) {
            Anim(name);
            clearInterval(variable); // Désactive le SetInterval
        }
    }, 250);
}


var Intro
NewScrollReveal(Intro, 'Intro');

var Mode
NewScrollReveal(Mode, 'Mode');