//Boton Limpiar
$('#btn_limpiar').click(function(e){ 
    fn_limpiar();
    $('#messagesRegistro').empty();
    fn_removeValido();
    fn_removeInvalido();
});
