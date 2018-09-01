
getFileNameAndImg();

function getFileNameAndImg() {

    $('.input-upload').click(function() {

        console.log("Label clicked");

        $('.input-upload').change(function() {

            var filepath = $('.input-upload').val();
            var n = filepath.lastIndexOf("\\");
            var filename = filepath.substring(n + 1);
            console.log("FILE NAME: " + filename)
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
