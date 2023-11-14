$(document).ready(function() {
    // Obtendo o token do atributo de dados do corpo
    const token = $('body').data('token');
    sessionStorage.setItem('token', token);

    // Resto do seu código aqui...
});