function fn_login(){
    window.open('main-template.html','_self');
}
$('#btn_limpiar').click(function(e){ 
    fn_limpiar();
    $('#messagesLogin').empty();
});

$('#btn_ingresar').click(function(){
    var rut = $('#txt-username').val();
    var pass =$('#txt-password').val();
    val = true;

    $('#messagesLogin').empty();

    if(rut == ""){
        val=false;
        $('#messagesLogin').append('<li> Debe ingresar un rut </li>');
    }
    if(rut.length <9){
        val=false;
        $('#messagesLogin').append('<li> El rut debe contener al menos 9 caracteres </li>');
    }
    if(pass == ""){
        val=false;
        $('#messagesLogin').append('<li> Debe introducir una contraseña </li>');
    }

    if(pass.length<6){
        val=false;
        $('#messagesLogin').append('<li> La contraseña debe tener al menos 6 caracteres</li>')
    }


    else{
        fn_login();
        alert('¡INICIO DE SESIÓN CORRECTO!');
    }
})

function fn_limpiar(){
    $('#txt-username').val("");
    $('#txt-password').val("");
}