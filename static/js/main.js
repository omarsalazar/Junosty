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
               },
               error: function(jqXRH, status, throwStatus) {
                   alert(status);
               }
           });
       };
    })( jQuery );

});
