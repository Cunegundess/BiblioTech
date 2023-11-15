$(document).ready(function() {
    console.log("Script carregado")
    
    $('#loginForm').submit(function(e) {
        e.preventDefault(); // Impede o comportamento padrão do formulário
    
        // Obtenha os valores do formulário
        var username = $('#id_username').val();
        var password = $('#id_password').val();
    
        // Envie as credenciais para o endpoint de login no Django
        $.ajax({
          url: 'http://127.0.0.1:8000/api/token/', // Substitua pela URL correta do endpoint de login que gera o token JWT
          type: 'POST',
          data: {
            username: username,
            password: password
          },
          success: function(response) {
            // Armazene o token JWT no localStorage após um login bem-sucedido
            var token = response.access; // Supondo que a resposta contenha um campo 'access' com o token JWT
            localStorage.setItem('jwtToken', token);
    
            // Redirecione ou realize outras ações após o login bem-sucedido
            console.log('Login bem-sucedido! Token JWT:', token);
          },
          error: function(error) {
            console.error('Erro ao tentar fazer login:', error);
          }
        });
    });
});