$(function(){
    $('.btnBuscar').click(function()
    {
        $.post("/contactAjaxResponse",
                { txtId : $('.txtId').val() },   
                function(data)
                {
                    if(data == undefined)
                        alert('El id no fue encontrado');
                    else
                    {
                        $('.txtId').val(data['id']);
                        $('.txtRut').val(data['rut']);
                        $('.txtNombre').val(data['nombre']);
                        $('.txtApellido').val(data['apellido']);
                        $('.txtCorre').val(data['corre']);
                    }

                } 
        )
        .fail(function()
        {
            alert('Error en la comunicación, manden chelas');

        })
        return false;
    });


});