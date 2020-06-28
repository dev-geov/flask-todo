$(document).ready(function(){
    $('.edit').click( function(){
        var id = $(this).attr('id');
        console.log(id);
        $('.ui.modal.'+id).modal('show')
    })
});