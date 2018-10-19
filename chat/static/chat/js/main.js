
sendMessage();

function sendMessage() {

    $('#btn-send-msg').click(function (e) {

        var msg = $('#txtarea').val();

        if(msg){

            alert(msg);

        }

    });

}