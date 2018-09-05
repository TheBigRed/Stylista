
listGroup();

function listGroup(){

    $('#formset-container').html($('#profile-form').html());

    $('.list-group li').click(function(e) {

        e.preventDefault()
        $('.list-group').find('li').removeClass('list-item-active');
        $(this).addClass('list-item-active');
        var id = $(this).attr('id');
        var html = $('#'+id+"-form").html();
        $('#formset-container').html(html);

    });

}