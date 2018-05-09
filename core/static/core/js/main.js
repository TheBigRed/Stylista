$(document).ready(function() {

    $('#search-input').keydown(function(event) {
        if (event.keyCode == 13) {
            alert("hey");
            this.form.submit();
            return false;
         }
    });

    $("#datepicker").flatpickr({});

});