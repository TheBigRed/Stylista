$(document).ready(function() {

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