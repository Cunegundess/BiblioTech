$(document).ready(function() {
    function atualizarTabela() {
        $.ajax({
            url: 'http://127.0.0.1:8000/api/cursos/', // Substitua pela URL correta da sua API
            method: 'GET',
            dataType: 'json',
            success: function(data) {
                var tabela = $('#tabela-cursos tbody');
                tabela.empty(); // Limpa a tabela

                data.forEach(function(curso) {
                    tabela.append(`
                        <tr>
                            <td>${curso.nome}</td>
                            <td>${curso.setor}</td>
                            <td>${curso.semestres}</td>
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
    setInterval(atualizarTabela, 5000); // 5000 milissegundos = 5 segundos

    function fecharModal() {
        $('.btn-close').click(); 
    }

    $('#cursoForm').on('submit', function(e){
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/api/cursos/', // Aqui está a URL de ação do formulário
            data: $(this).serialize(),
            success: function(data){
                // Aqui você pode adicionar código para lidar com a resposta bem-sucedida
                console.log(data);
                atualizarTabela(); // Atualiza a tabela com os novos dados
                fecharModal(); // Fecha o modal após o sucesso da requisição
            },
            error: function(data){
                // Aqui você pode adicionar código para lidar com erros
                console.log(data);
            }
        });
    });
});
