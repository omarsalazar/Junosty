$.noConflict();
jQuery(document).ready(function(){

    (function( jQuery ){
       jQuery.fn.get_csrf = function() {
           var end, start;
           start = document.cookie.indexOf('csrftoken=');
           end = document.cookie.indexOf(";", start);
           if (-1 === end) {
             end = document.cookie.length;
           }
           csrftoken = document.cookie.substring(start, end).replace('csrftoken=', '');
           return csrftoken;
       };
    })( jQuery );

    (function( jQuery ){
       jQuery.fn.editar_hora = function(aidi) {
           console.log('holis');
           c_token = jQuery().get_csrf();
           jQuery.ajax({
               method: 'POST',
               url: '/materia/detalle/20/',
               headers: {
                   'x-csrftoken': c_token
               },
               data: {
                   aidi: aidi,
                   action: 'editar_hora',
                   hora: jQuery('#hora-'+aidi).val(),
                   fin: jQuery('#fin-'+aidi).val(),
                   dia: jQuery('#dia-'+aidi).val()
               },
               success: function (data, status, jqXRH) {
                   alert(status);
                   location.reload();
               },
               error: function(jqXRH, status, throwStatus) {
                   alert(status);
                   location.reload();
               }
           });
       };
    })( jQuery );

    (function( jQuery ){
       jQuery.fn.eliminar_hora = function(aidi) {
           c_token = jQuery().get_csrf();
           jQuery.ajax({
               method: 'POST',
               url: '/materia/detalle/20/',
               headers: {
                   'x-csrftoken': c_token
               },
               data: {
                   aidi: aidi,
                   action: 'eliminar_hora',
                   hora: jQuery('#hora-'+aidi).val(),
                   fin: jQuery('#fin-'+aidi).val(),
                   dia: jQuery('#dia-'+aidi).val()
               },
               success: function (data, status, jqXRH) {
                   alert(status);
                   location.reload();
               },
               error: function(jqXRH, status, throwStatus) {
                   alert(status);
                   location.reload();
               }
           });
       };
    })( jQuery );

});

function valid(){
    contra1 = document.form1.contrasena.value;
    contra2 = document.form1.contrasenados.value;
    usuario = document.form1.usuario.value;
    apellidos = document.form1.apellidos.value;
    var espacios = false;
    var cont = 0;

    while (!espacios && (cont < usuario.length) || !espacios && (cont < apellidos.length) ) {
        if (usuario.charAt(cont) == " " || apellidos.charAt(cont) == " ")
        espacios = true;
        cont++;
    }

    if (espacios) {
        alert("No debe haber campos de texto vacio a excepción de la contraseña en caso de no querer cambiarla");
        return false;
    }

    if(contra1 != contra2){
        alert("Las contraseñas no coinciden");
        return false;
    }


}

function validregistro(){
    contra = document.formr.contrasena.value;
    contrar = document.formr.contrasenados.value;
    if(contra != contrar){
        alert("Las contraseñas no coinciden");
        return false;
    }
}
