$(document).ready(function() {
    const url = 'http://127.0.0.1:8000/api/emprestimos/'
    // const token = "44992d5cf025fc6881b123025edf4a0778435697"
    const token = sessionStorage.getItem('jwtToken');

    function formatarData(data) {
        return moment(data).format('DD/MM/YYYY');
    }

    function atualizarTabela() {

        if (token) {
            var headers = {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            }
        
            $.ajax({
                url: url,  // Substitua pela URL correta da sua API
                method: 'GET',
                headers: headers,
                dataType: 'json',
                success: function(data) {
                    var tabela = $('#tabela-emprestimos tbody');
                    tabela.empty(); // Limpa a tabela

                    data.results.forEach(function(emprestimo) {
                        tabela.append(`
                            <tr>
                                <td>${emprestimo.nome}</td>
                                <td>${emprestimo.aluno.nome}</td>
                                <td>${emprestimo.livro.titulo}</td>
                                <td>${formatarData(emprestimo.data_emprestimo)}</td>
                                <td>
                                    <a class="btn btn-sm bg-primary text-light" href="http://127.0.0.1:8000/home/emprestimos/${emprestimo.id}">
                                        <i class="bi bi-pencil-square me-1"></i>
                                        Editar
                                    </a>
                                </td>
                            </tr>
                        `);
                    });
                },
                error: function(error) {
                    // Manipule os erros da requisição aqui
                    console.error('Erro na requisição:', error);
                }
            });

        } else {
            console.error('Token não encontrado')
        }
    }

    // Chama a função para atualizar a tabela quando a página carrega
    atualizarTabela();

    // Atualiza a tabela a cada X segundos (por exemplo, a cada 5 segundos)
    setInterval(atualizarTabela, 5000); // 5000 milissegundos = 5 segundos

    function fecharModal() {
        $('.btn-close').click(); 
    }

    $('#emprestimoForm').on('submit', function(e){
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: url, // Aqui está a URL de ação do formulário
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            },
            data: $(this).serialize(),
            success: function(data){
                // Aqui você pode adicionar código para lidar com a resposta bem-sucedida
                console.log(data);
                atualizarTabela(); // Atualiza a tabela com os novos dados
                fecharModal(); // Fecha o modal após o sucesso da requisição
            },
            error: function (xhr) {
                console.log('Código de Status:', xhr.status);
                console.log('Resposta:', xhr.responseText);
            },
            complete: function() {
                // Reabilita o botão de envio do formulário após a requisição
                $('#submit-button').attr('disabled', false);
            }
        });
    });
});
