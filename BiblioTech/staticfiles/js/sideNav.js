document.addEventListener('DOMContentLoaded', function() {
    var links = document.querySelectorAll('#menu a');
    for (var i = 0; i < links.length; i++) {
        if (links[i].href === window.location.href) {
            links[i].classList.add('active');
        }
    }
});