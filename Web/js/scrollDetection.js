// Fichier de detection du scroll et de lancement des actions

function Anim(name) {
    if (name == 'Intro') {
        for (element of document.getElementsByClassName('ParagrapheIntro')) {
            element.classList.add('Paragraphe__animation');
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

    else if (name == 'Amelioration') {
        for (element of document.getElementsByClassName('ParagrapheAm')) {
            element.classList.add('Paragraphe__animation');
        }
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

var Amelioration
NewScrollReveal(Amelioration, 'Amelioration');




function EquipementOver(equipement) {
    if (equipement == 'Bouclier'){
        document.getElementById('TextGrenade').style.display = 'none';
        document.getElementById('TextPotion').style.display = 'none';

        var el = document.getElementById('TextBouclier');
        el.classList.add('Info__animation');
        el.style.display = 'inline';
        
    }

    else if (equipement == 'Grenade') {
        document.getElementById('TextBouclier').style.display = 'none';
        document.getElementById('TextPotion').style.display = 'none';

        var el = document.getElementById('TextGrenade')
        el.style.display = 'inline';
        el.classList.add('Info__animation');


    }

    else if (equipement == 'Potion') {
        document.getElementById('TextBouclier').style.display = 'none';
        document.getElementById('TextGrenade').style.display = 'none';

        var el = document.getElementById('TextPotion')
        el.style.display = 'inline';
        el.classList.add('Info__animation');

    }
    
}

function EquipementLeave() {
    document.getElementById('TextBouclier').style.display = 'none';
    document.getElementById('TextGrenade').style.display = 'none';
    document.getElementById('TextPotion').style.display = 'none';
}