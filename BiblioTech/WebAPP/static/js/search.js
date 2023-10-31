// Código JavaScript para lidar com a pesquisa
$(document).ready(function() {
    $('#search-form').on('submit', function(e) {
        e.preventDefault();
        var consulta = $('#search-input').val(); // Obtém a consulta do input

        $.ajax({
            url: 'http://127.0.0.1:8000/api/pesquisa/', // Rota da sua API de pesquisa
            method: 'GET',
            data: { consulta: consulta },
            dataType: 'json',
            success: function(data) {
                // Aqui você pode processar os resultados da pesquisa
                console.log(data);
            },
            error: function(error) {
                console.error(error);
            }
        });
    });
});
