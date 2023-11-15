$(document).ready(function() {
    const url = 'http://127.0.0.1:8000/api/emprestimos/'
    // const token = "44992d5cf025fc6881b123025edf4a0778435697"
    const token = sessionStorage.getItem('jwtToken');

    function formatarData(data) {
        const partesData = data.split('/');
        const dataISO = `${partesData[2]}-${partesData[1]}-${partesData[0]}`;
    
        return moment(dataISO, 'YYYY-MM-DD').format('DD/MM/YYYY');
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
                                <td>${emprestimo.aluno}</td>
                                <td>${emprestimo.livro}</td>
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

    // function converterDataParaFormatoDjango(data) {
    //     const partesData = data.split('/');
    //     const dataFormatoDjango = `${partesData[2]}-${partesData[1].padStart(2, '0')}-${partesData[0].padStart(2, '0')}`;
    //     return dataFormatoDjango;
    // }

    $('#emprestimoForm').on('submit', function(e){
        e.preventDefault();
    
        var formData = {
            nome: $('#id_nome').val(),
            livro: $('#id_livro').val(),
            aluno: $('#id_aluno').val(),
            data_emprestimo: $('#id_data_emprestimo').val(),
            data_devolucao: $('#id_data_devolucao').val()
            // ... adicione outros campos conforme necessário
        };
    

        function getCSRFToken() {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith('csrftoken=')) {
                    return cookie.substring('csrftoken='.length, cookie.length);
                }
            }
            return null;  // Retorna null se o token CSRF não for encontrado
        }

        var csrftoken = getCSRFToken(); 

        $.ajax({
            type: 'POST',
            url: url, // Aqui está a URL de ação do formulário
            headers: {
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            },
            data: JSON.stringify(formData),
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
