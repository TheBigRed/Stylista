$(document).ready(function() {

    $('.list-group li').click(function(e) {
        e.preventDefault()

        $that = $(this);

        $('.list-group').find('li').removeClass('active');
        $that.addClass('active');
    });

});