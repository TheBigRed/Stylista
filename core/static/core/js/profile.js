$(document).ready(function() {

    $('#lightgallery').lightGallery({

        mode: 'lg-fade',
        cssEasing : 'cubic-bezier(0.25, 0, 0.25, 1)'

    });

    $("[id^=modalopen]").click(function(){

        var serviceName = $(this).parents().eq(1).children().eq(0).children().eq(0).text();
        var serviceDescription = $(this).parents().eq(1).children().eq(0).children().eq(1).text();
        var time = $(this).parents().eq(0).children().eq(0).text();
        var price = $(this).parents().eq(0).children().eq(1).text();
        console.log(serviceName);
        $('#jservice').append(serviceName);
        $('#jdesc').append(serviceDescription);
        $('#jtime').append(time);
        $('#jprice').append(price);

        // it is superfluous to have to manually call the modal.
        // $('#addBookDialog').modal('show');
    });

    $('#confirm-btn').click(function(){

        form_submit();

    });

});

function form_submit() {

    $('#form-contract').submit();

}

