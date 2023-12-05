// Seletor jQuery para os campos do formulário
const nomeInput = $('#id_nome');
const emailInput = $('#id_email');
const senhaInput = $('#id_senha');
const contatoInput = $('#id_contato');
const raInput = $('#id_ra');

// Seletor jQuery para a div de mensagens de erro
const errorMessages = $('#error-messages');

// Eventos de entrada para validações em tempo real
nomeInput.on('input', function () {
    clearError();
    const nomeValue = nomeInput.val();
    if (nomeValue.length < 3) {
        showError('O nome deve ter pelo menos 3 caracteres.');
    }
});

emailInput.on('input', function () {
    clearError();
    const emailValue = emailInput.val();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(emailValue)) {
        showError('Digite um endereço de e-mail válido.');
    }
});

senhaInput.on('input', function () {
    // Sua lógica de validação para o campo senha
    // Exemplo: exibir uma mensagem de erro se a senha for muito curta
    if ($(this).val().length < 6) {
        showError('Senha deve ter pelo menos 6 caracteres');
    } else {
        clearError();
    }
});

$('#id_contato').inputmask('(99) 99999-9999', { placeholder: ' ' });
$('#id_telefone').inputmask('(99) 99999-9999', { placeholder: ' ' });
$('#id_data_emprestimo').inputmask('99/99/9999', { placeholder: ' ' });
$('#id_data_devolucao').inputmask('99/99/9999', { placeholder: ' ' });
$('#id_data_nascimento').inputmask('99/99/9999', { placeholder: ' ' });
// $('#id_isbn').inputmask('999-9-99999-9999-9', {
//     placeholder: ' ',
// });


raInput.on('input', function () {
    clearError();
    const raValue = raInput.val();
    // Adicione lógica de validação do RA conforme necessário
    // Exemplo: RA deve conter apenas números e ter um comprimento específico
    const raRegex = /^\d{8}$/;
    if (!raRegex.test(raValue)) {
        showError('Digite um RA válido (apenas números, 8 dígitos).');
    }
});

// Função para exibir mensagens de erro
function showError(message) {
    errorMessages.html(`<div class="alert alert-danger" role="alert">${message}</div>`);
}

// Função para limpar as mensagens de erro
function clearError() {
    errorMessages.html('');
}

// Evento de envio do formulário para realizar a última validação antes de enviar ao servidor
$('#alunoForm').submit(function (event) {
    // Realize sua última validação aqui, se necessário
    // Exemplo: impedir o envio se houver mensagens de erro exibidas
    if (errorMessages.html() !== '') {
        event.preventDefault();
        showError('Corrija os erros antes de enviar o formulário.');
    }
});