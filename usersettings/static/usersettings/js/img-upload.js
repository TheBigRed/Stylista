
addFileNameToLabel();

function addFileNameToLabel() {

    $('.input-upload').click(function() {

        console.log("Label clicked");

        $('.input-upload').change(function() {

            var filename = $('.input-upload').val();
            $('#filename').text(filename);
            alert(filename);

        });

    });


}


