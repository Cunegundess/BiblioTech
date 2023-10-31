$(document).ready(function(){
    $('#AutorForm').on('submit', function(e){
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: "{% url 'API:autores'%}", // Aqui está a URL de ação do formulário
            data: $(this).serialize(),
            success: function(data){
                // Aqui você pode adicionar código para lidar com a resposta bem-sucedida
                console.log(data);
            },
            error: function(data){
                // Aqui você pode adicionar código para lidar com erros
                console.log(data);
            }
        });
    });
});
