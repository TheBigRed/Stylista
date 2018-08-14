$(document).ready(function() {

    var cw = window.rating1.clientWidth; // save original 100% pixel width
    var starElem = document.getElementsByClassName("star-rating");
    //var datVal = document.getElementById('rating1').getAttribute('data-value');

    for(var i=0; i<starElem.length; i++) {

        var datVal = starElem[i].getAttribute('data-value');
        rating(datVal, cw, starElem[i]);
        console.log("Current star rating " + i + " : " + datVal);

    }

    //removeHR();

});


function rating(stars, cw, starElem) {

    starElem.style.width = Math.round(cw * (stars / 5)) + 'px';

}

function removeHR(){

    var select = document.getElementsByTagName("HR");
    console.log("hr num: " + select.length);
    select[select.length-1].parentNode.removeChild(select[select.length-1]);

}