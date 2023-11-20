$(document).ready(function() {
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
