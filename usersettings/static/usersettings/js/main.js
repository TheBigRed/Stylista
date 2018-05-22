$(document).ready(function() {

    $('.list-group li').click(function(e) {
        e.preventDefault()

        //$that = $(this);

        $('.list-group').find('li').removeClass('active');
        $(this).addClass('active');
        $('#setting-form').addClass('d-none')
    });

    loadInputValues();


});


//Iterate over all input fields in form and put placeholder value as input value
function loadInputValues() {

    $('#setting-form *').filter(':input').each(function(){
        var ph = $(this).attr('placeholder');
        $(this).val(ph);
    });
}
