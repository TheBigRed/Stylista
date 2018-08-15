$(document).ready(function() {

    var cw = window.rating2.clientWidth; // save original 100% pixel width & only gets width once
    var starElem = document.getElementsByClassName("star-rating");
    console.log(cw);

    for(var i=0; i<starElem.length; i++) {

        var datVal = starElem[i].getAttribute('data-value');
        rating(datVal, cw, starElem[i]);

    }


    helpfulAjaxCall();
    removeHR();

});


function rating(datVal, cw, starElem) {

    starElem.style.width = Math.round(cw * (datVal / 5)) + 'px';

}

//Remove last HR Element from review container
function removeHR(){

    var select = document.getElementsByTagName("HR");
    console.log("hr num: " + select.length);
    select[select.length-1].parentNode.removeChild(select[select.length-1]);

}

//Ajax call to upvote or down vote help button with CSRF token validation
function helpfulAjaxCall(){

    $(".help-button").button().click(function(){

        //var btnValue = $('help-button').text();
        var btnValue = $(this).text();
        serializeData = { vote: btnValue };
        csrftoken = getCookie('csrftoken');

        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $.ajax({
            type: "POST",
            url: "/reviews/upvote/",
            async: false,
            data: serializeData,
            success: function(response) {


            }
        });

    });


    function getCookie(name) {

        var cookieValue = null;

        if (document.cookie && document.cookie !== '') {

            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {

                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }

        }

        return cookieValue;

    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

}