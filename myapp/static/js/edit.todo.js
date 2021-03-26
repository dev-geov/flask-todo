$(document).ready(function(){

    $('.item.add').click( function(){
        console.log('add')
        $('.ui.modal.add').modal('show')
    })

    $('.edit').click( function(){
        id = $(this).attr('id')
        console.log(id)
        $('.ui.modal.'+id).modal('show')
    })
    
});