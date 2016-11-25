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
           c_token = $().get_csrf();
           jQuery.ajax({
               method: 'POST',
               url: '/materia/detalle/20/',
               headers: {
                   'x-csrftoken': hoho
               },
               data: {
                   idi: aidi,
                   status: 'editar'
               }
           });
       };
    })( jQuery );

    (function( jQuery ){
       jQuery.fn.eliminar_hora = function(aidi) {
           c_token = $().get_csrf();
           jQuery.ajax({
               method: 'POST',
               url: '/materia/detalle/20/',
               headers: {
                   'x-csrftoken': hoho
               },
               data: {
                   idi: aidi,
                   status: 'eliminar'
               }
           });
       };
    })( jQuery );

});
