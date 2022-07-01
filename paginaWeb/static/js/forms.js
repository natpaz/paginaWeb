$(document).ready(function(){

// Acá creamos las validaciones del formulario.
    $('#validar').validate({
        rules: {
        nombre:{
            required:true,
            minlength: 5
        },
        correo:{
            required:true,
            correo: true
        },
        asunto:{
            required:true
        },
        mensaje:{
            required:true
        },
        },
        messages: {
            nombre:{
                required:"Debes ingresar tu nombre",
                minlength:"Tu nombre debe ser de no menos de 5"
        },
            correo:{
                required:"Debes ingresar un correo",
                email:"Por favor ingresa un correo válido"
        },
            asunto:{
            required:"Debes escribir el asunto"
        },
            mensaje:{
            required:"Escriba el mensaje"
        },
        },
    });

});