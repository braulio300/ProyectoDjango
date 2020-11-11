$(function ()
{
    //Validar escribir numeros o letras.
    let numeros = '1234567890';
    let letras  = 'qwertyuiopasdfghjklñzxcvbnm' +
                'QWERTYUIOPASDFGHJKLÑZXCVBNM' +
                'ÁÉÍÓÚáéíóú-@_ .';
    let dv = '1234567890Kk';

    //Restringir escribir números.
    $('.txtNombre').keypress(function (e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
                return false;
    });

    //Validación de datos de registro
    $('.btnAceptar').click(function()
    {
        //la variable texto, validara uno por uno.
        let texto= "";

        texto = $('.txtNombre').val();   //.val() captura lo que se ingresó en la caja de texto.
        if(texto == '')                  // Nombre
        {
            alert('No especificó el Nombre de usuario');
            $('.txtNombre').focus();
            return;
        }

        texto = $('.txtCorreo').val();   //.val() captura lo que se ingresó en la caja de texto.
        if(texto == '')                  // Correo
        {
            alert('No especificó el Correo');
            $('.txtCorreo').focus();
            return;
        }

        texto = $('.txtClave').val();   //.val() captura lo que se ingresó en la caja de texto.
        if(texto == '')                  // Clave
        {
            alert('No especificó la contraseña');
            $('.txtClave').focus();
            return;
        }

        //Validar Correo
        let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,4})+$/
        if(!emailRegex.test($('.txtCorreo').val()))
        {
            alert('Formato del correo no es válido.');
            return;
        }


    })

})