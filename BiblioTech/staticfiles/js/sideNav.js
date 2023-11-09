$(document).ready(function() {
    document.addEventListener('DOMContentLoaded', function() {
        var links = document.querySelectorAll('#menu a');
        for (var i = 0; i < links.length; i++) {
            if (links[i].href === window.location.href) {
                links[i].classList.add('active');
            }
        }
    });

    // Abre o dropdown
    $('.dropdown-toggle').on('click', function () {
        $(this).next('.dropdown-menu').toggleClass('show');
    });

    // Fecha o dropdown ao clicar fora dele
    $(document).on('click', function (e) {
        if (!$(e.target).closest('.dropdown').length) {
            $('.dropdown-menu').removeClass('show');
        }
    });

});
