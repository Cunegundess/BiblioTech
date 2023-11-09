$(document).ready(function() {
    const url = 'http://127.0.0.1:8000/api/editoras/'
    function atualizarTabela() {
        $.ajax({
            url: url, // Substitua pela URL correta da sua API
            method: 'GET',
            dataType: 'json',
            success: function(data) {
                var tabela = $('#tabela-editoras tbody');
                tabela.empty(); // Limpa a tabela

                data.results.forEach(function(editora) {
                    tabela.append(`
                        <tr>
                            <td>${editora.nome}</td>
                            <td>${editora.endereco}</td>
                            <td>${editora.telefone}</td>
                            <td>
                                <button id="editButton" type="button" class="btn btn-sm bg-primary text-light" data-bs-toggle="modal" data-bs-target="#formEditora">
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

    $('#editoraForm').on('submit', function(e){
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

    $('#tabela-editoras').on('click', '#editButton', function() {
        var linha = $(this).closest('tr'); 
        var nome = linha.find('td:eq(0)').text(); 
        var endereco = linha.find('td:eq(1)').text(); 
        var telefone = linha.find('td:eq(2)').text(); 

        // Preenche o formulário de edição
        $('#id_nome').val(nome);
        $('#id_endereco').val(endereco);
        $('#id_telefone').val(telefone);

        // Muda o título do modal
        $('#editoraFormLabel').text('Editar Editora');

        // Adiciona o campo de CSRF ao formulário
        $('#editoraForm').append('{% csrf_token %}');

        // Adiciona um botão de exclusão ao formulário
        $('#editoraForm .modal-footer').append('<button type="button" class="btn btn-danger" id="deleteButton">Excluir</button>');

        // Define a URL de ação do formulário para a edição
        $('#editoraForm').attr('action', url); // Substitua pela URL correta
    });

    $('#editoraForm').on('click', '#deleteButton', function() {
        atualizarTabela();
        var editoraId = $('#id_id').val(); // Supondo que você tenha um campo de ID no formulário
        $.ajax({
            type: 'DELETE',
            url: `http://127.0.0.1:8000/api/editoras/${editoraId}/`, // Substitua pela URL correta
            dataType: 'json',
            success: function(data) {
                console.log(data.mensagem);
                atualizarTabela();
                fecharModal();
            },
            error: function(xhr, textStatus, errorThrown) {
                console.error(xhr.responseText);
            }
        });
    });
});
