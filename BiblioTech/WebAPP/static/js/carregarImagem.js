$(document).ready(function() {
    var img = new Image();
    img.src = "{% static 'img/books6.jpg' %}";
    
    img.onload = function() {
        // Quando a imagem estiver completamente carregada, atualize o plano de fundo
        $('header').css('background-image', 'url(' + img.src + ')');
    }
});
