$(document).ready(function() {
    function atualizarTabela() {
        $.ajax({
            url: 'http://localhost:8000/api/autores/', // Substitua pela URL correta da sua API
            method: 'GET',
            dataType: 'json',
            success: function(data) {
                var tabela = $('#tabela-autores tbody');
                tabela.empty(); // Limpa a tabela

                data.forEach(function(autor) {
                    tabela.append(`
                        <tr>
                            <td>${autor.nome}</td>
                            <td>${autor.nacionalidade}</td>
                            <td>${autor.data_nascimento}</td>
                            <td>
                                <button type="button" class="btn btn-sm bg-primary text-light">
                                    <i class="bi bi-pencil-square me-1"></i>
                                    Editar
                                </button>
                            </td>
                        </tr>
                    `);
                });
            }
        });
    }

    // Chama a função para atualizar a tabela quando a página carrega
    atualizarTabela();

    // Atualiza a tabela a cada X segundos (por exemplo, a cada 5 segundos)
    setInterval(atualizarTabela, 1000); // 5000 milissegundos = 5 segundos
});
