
getFileNameAndImg();

function getFileNameAndImg() {

    $('.input-upload').click(function() {

        console.log("Label clicked");

        $('.input-upload').change(function() {

            var filename = $('.input-upload').val();
            getImg(this);
            $('#filename').text(filename);

        });

    });


}


function getImg(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('.storefront-img').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}
