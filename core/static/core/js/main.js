$(document).ready(function() {

    $('#search-input').keydown(function(event) {
        if (event.keyCode == 13) {
            alert("hey");
            this.form.submit();
            return false;
         }
    });

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
                    $("#ajax-response").html(response);
                }

            });

        }

    });

});