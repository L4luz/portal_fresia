$('#btn_enviar').click(function(e){
    var nombre = $('#txt-nombre').val();
    var email = $('#txt-email').val();
    var comentarios = $('#txt-comentarios').val();
    val = true; 

    $('#messagesEnviar').empty();

    if (nombre == ""){
        val = false;
        $('#messagesEnviar').append('<li> Debe ingresar nombre </li>');
    }

    if (email == ""){
        val = false;
        $('#messagesEnviar').append('<li> Debe ingresar un correo electronico </li>');
    }

    if (comentarios == ""){
        val = false;
        $('#messagesEnviar').append('<li> Debe ingresar comentarios </li>');
    }
    

})

$('#btn_limpiar').click(function(e){
    $('#txt-nombre').val("");
    $('#txt-email').val("");
    $('#txt-comentarios').val("");

})

