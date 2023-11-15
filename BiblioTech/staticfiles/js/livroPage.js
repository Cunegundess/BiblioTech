$(document).ready(function() {
    const url = 'http://127.0.0.1:8000/api/livros/'

    function formatarISBN(isbn) {
        // Remover espaços em branco e hifens existentes
        const numeroLimpo = isbn.replace(/[ -]/g, '');
    
        // Determinar o comprimento do ISBN
        const comprimentoISBN = numeroLimpo.length;
    
        // Verificar se é ISBN-10 ou ISBN-13
        if (comprimentoISBN === 10) {
            // Formatar ISBN-10: XXX-X-XXXXX-XX
            return `${numeroLimpo.slice(0, 3)}-${numeroLimpo.slice(3, 4)}-${numeroLimpo.slice(4, 9)}-${numeroLimpo.slice(9, 10)}`;
        } else if (comprimentoISBN === 13) {
            // Formatar ISBN-13: XXX-X-XXXXX-XXXX-X
            return `${numeroLimpo.slice(0, 3)}-${numeroLimpo.slice(3, 4)}-${numeroLimpo.slice(4, 9)}-${numeroLimpo.slice(9, 13)}-${numeroLimpo.slice(13)}`;
        } else {
            // Se o comprimento não for 10 nem 13, retornar o número ISBN original
            return isbn;
        }
    }

    function atualizarTabela() {
        $.ajax({
            url: url, // Substitua pela URL correta da sua API
            method: 'GET',
            dataType: 'json',
            success: function(data) {
                var tabela = $('#tabela-livros tbody');
                tabela.empty(); // Limpa a tabela

                data.results.forEach(function(livro) {
                    tabela.append(`
                        <tr>
                            <td>${livro.titulo}</td>
                            <td>${livro.autor.nome}</td>
                            <td>${formatarISBN(livro.isbn)}</td>
                            <td>
                                <a class="btn btn-sm bg-primary text-light" href="http://127.0.0.1:8000/home/livros/${livro.id}">
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

    $('#livroForm').on('submit', function(e){
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
