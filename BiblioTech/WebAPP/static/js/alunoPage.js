$(document).ready(function() {
    const url = 'http://127.0.0.1:8000/api/alunos/'
    
    function atualizarTabela() {
        $.ajax({
            url: url, // Substitua pela URL correta da sua API
            method: 'GET',
            dataType: 'json',
            success: function(data) {
                var tabela = $('#tabela-alunos tbody');
                tabela.empty(); // Limpa a tabela

                data.results.forEach(function(aluno) {
                    tabela.append(`
                        <tr>
                            <td>${aluno.nome}</td>
                            <td>${aluno.ra}</td>
                            <td>${aluno.curso.nome}</td>
                            <td>
                                <a class="btn btn-sm bg-primary text-light" href="http://127.0.0.1:8000/home/alunos/${aluno.id}">
                                    <i class="bi bi-pencil-square me-1"></i>
                                    Editar
                                </a>
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

    $('#alunoForm').on('submit', function(e){
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/api/alunos/', // Aqui está a URL de ação do formulário
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
