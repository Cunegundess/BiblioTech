$(document).ready(function(){

    function formatarData(data) {
        return moment(data).format('DD/MM/YYYY');
    }


    $('#search-form').submit(function(event){
        event.preventDefault();
        var query = $('#search-input').val();

        // Verifica se a consulta está vazia
        if (!query.trim()) {
            alert('Por favor, insira um termo de pesquisa.');
            return; // Impede o envio do formulário se a consulta estiver vazia
        }

        $.ajax({
            url: 'http://localhost:8000/api/pesquisa/', // Substitua pela URL da sua view de pesquisa na API
            type: 'GET',
            data: { consulta: query },
            contentType: 'application/json', // Adiciona o cabeçalho Content-Type
            success: function(response){
                if ($.isEmptyObject(response)) {
                    alert('Nenhum resultado encontrado.');
                } else {
                    // Redireciona para a página de resultados após uma query bem-sucedida
                    window.location.href = 'http://localhost:8000/home/resultados_pesquisa/?data=' + encodeURIComponent(JSON.stringify(response));
                }
            },
            error: function(error){
                alert('Erro na requisição: ' + error.responseText); // Alerta com a mensagem de erro
                console.log(error);
            }
        });
    });
});
