function carregarPaginacao(url, paginaAtual) {
    var paginaContainer = $('#pagination-container');

    $.ajax({
        url: url,
        method: 'GET',
        dataType: 'json', // Alterado para JSON, assumindo que o backend retorna JSON
        data: { page: paginaAtual },
        success: function(data) {
            atualizarTabela(data);
        }
    });
}

$('#pagination-container').on('click', '.page-link', function(e) {
    e.preventDefault();
    var url = $(this).attr('href'); // Obtém a URL da página clicada
    carregarPaginacao(url);
});