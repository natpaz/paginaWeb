$("#btn-cargar").click(function (event) {
    event.preventDefault();
/* declaramos la variable url*/
    var url = "https://dog.ceo/api/breeds/image/random";

/* utilizamos fetch para acceder a los recursos del servidor*/
        fetch(url)
        .then(response => response.json())
        .then(data => 
            {
/* declaramos la variable para mostrar la imagen*/
                var $foto_user = $("<p><img class='img-thumbnail' src='"+data.message+"'>");



                /* limpiamos el contedor antes de desplegar */
                $("#info").empty();
                $('#info')

                    .append($foto_user);



            })
        .catch(error => console.error(error));



});
