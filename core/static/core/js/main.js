$(document).ready(function() {

    geoFindMe();

    $('#search-form').keydown(function(event) {
        if (event.keyCode == 13) {
            //this.form.submit();
            this.submit();
            //return false;
         }
    });

    $(".primary-btns").button().click(function(){

        var btnValue = $(this).attr("value");
        console.log(btnValue);
        serializeData = { btnValue1: btnValue, ItemName: 'test' };

        $.ajax({
            type: "GET",
            url: "/core/searchrevolver/",
            async: false,
            data: serializeData,
            success: function(response) {
                $("#ajax-response").html(response);

            }
        });
        $(this).addClass('primary-btn-hover');
    });

    datepicker();
    timepicker();

});

function buttonRevolver(){




}


function datepicker(){

    $("#datepicker").flatpickr({

        minDate: "today",
        dateFormat: "m-d-Y",
        wrap: true,
        onChange: function(selectedDates, dateStr, instance) {
        //...
        },
        onOpen: [
            function(selectedDates, dateStr, instance){



        },
            function(selectedDates, dateStr, instance){

        }
        ],
        onClose: function(selectedDates, dateStr, instance){

            var date = this.selectedDates;
            console.log(date);
            serializeData = { ListID: '1', ItemName: 'test' };

            $.ajax({
                url: "/core/searchrefined/",
                type: "get",
                data: serializeData,
                success: function(response) {
                    $("#ajax-response").empty();
                    $("#ajax-response").html(response);
                }

            });

        }

    });


}

function timepicker(){

    $("#timepicker").flatpickr({

        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
        time_24hr: true/*
        onChange: function(selectedDates, dateStr, instance) {
        //...
        },
        onOpen: [
            function(selectedDates, dateStr, instance){



        },
            function(selectedDates, dateStr, instance){

        }
        ],
        onClose: function(selectedDates, dateStr, instance){

            var date = this.selectedDates;
            console.log(date);
            serializeData = { ListID: '1', ItemName: 'test' };

            $.ajax({
                url: "/core/searchrefined/",
                type: "get",
                data: serializeData,
                success: function(response) {
                    $("#ajax-response").empty();
                    $("#ajax-response").html(response);
                }

            });

        }*/

    });


}

function geoFindMe() {

    var output = document.getElementById("map");

    if (!navigator.geolocation){
        alert("<p>Geolocation is not supported by your browser</p>");
        return;
    }

    function success(position) {
        var latitude  = position.coords.latitude;
        var longitude = position.coords.longitude;

        //output.innerHTML = '<p>Latitude is ' + latitude + '° <br>Longitude is ' + longitude + '°</p>';

        var img = new Image();
        img.src = "https://maps.googleapis.com/maps/api/staticmap?center=" + latitude + "," + longitude + "&zoom=13&size=300x300&sensor=false";

        output.appendChild(img);
        $("#map").children('img').addClass('map');
    }

    function error() {
        output.innerHTML = "Unable to retrieve your location";
    }

    //output.innerHTML = "<p>Locating…</p>";

    navigator.geolocation.getCurrentPosition(success, error);

}