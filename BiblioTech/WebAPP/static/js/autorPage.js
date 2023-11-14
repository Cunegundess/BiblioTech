$(document).ready(function() {
    const url = 'http://127.0.0.1:8000/api/autores/'

    function formatarData(data) {
        return moment(data).format('DD/MM/YYYY');
    }


    function atualizarTabela() {
        $.ajax({
            url: url, 
            method: 'GET',
            dataType: 'json',
            success: function(data) {
                var tabela = $('#tabela-autores tbody');
                tabela.empty(); 
                
                data.results.forEach(function(autor) {
                    tabela.append(`
                        <tr>
                            <td>${autor.nome}</td>
                            <td>${autor.nacionalidade}</td>
                            <td>${formatarData(autor.data_nascimento)}</td>
                            <td>
                                <a class="btn btn-sm bg-primary text-light" href="http://127.0.0.1:8000/home/autores/${autor.id}">
                                    <i class="bi bi-pencil-square me-1"></i>
                                    Editar
                                </a>
                            </td>
                        </tr>
                    `);
                });
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
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

    $('#autorForm').on('submit', function(e){
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: url, // Aqui está a URL de ação do formulário
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
