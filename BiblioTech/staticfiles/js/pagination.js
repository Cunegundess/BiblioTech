function carregarPaginacao(url, paginaAtual) {
    var paginaContainer = $('#pagination-container');

    $.ajax({
        url: url,
        method: 'GET',
        dataType: 'json',
        data: { page: paginaAtual },
        success: function(data) {
            atualizarTabela(data); // Certifique-se de que a função atualizarTabela esteja definida e funcional
        }
    });
}

$('#pagination-container').on('click', '.page-link', function(e) {
    e.preventDefault();
    var url = $(this).attr('href'); // Obtém a URL da página clicada
    var paginaAtual = url.split('=')[1]; // Obtém o número da página a partir da URL
    carregarPaginacao(url, paginaAtual); // Passa a URL e o número da página para a função
});
