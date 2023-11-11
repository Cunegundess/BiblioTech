function excluirLivro(event, url) {
    event.preventDefault();
    if (confirm('Tem certeza de que deseja excluir este Livro?')) {
        fetch(url, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value,
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            alert(data.mensagem);
            // Redirecionar ou fazer outras ações necessárias após excluir
            window.location.href = data.redirect || 'http://127.0.0.1:8000/home/livros/';
        })
        .catch(error => {
            console.error('Erro ao excluir Livro:', error);
            // Tratar erros, se necessário
        });
    }
}

function salvarLivro(event, url) {
    event.preventDefault();
    if (confirm('As alterações estão corretas?')) {
        // Obtenha os dados do formulário e converta para JSON
        const formData = new FormData(document.getElementById('editarLivroForm'));
        const jsonData = {};
        formData.forEach((value, key) => {
            jsonData[key] = value;
        });

        fetch(url, {
            method: "PUT",
            headers: {
                "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value,
                "Content-Type": "application/json"
            },
            body: JSON.stringify(jsonData)
        })
        .then(response => response.json())
        .then(data => {
            alert(data.mensagem);
            // Redirecionar ou fazer outras ações necessárias após salvar
            window.location.href = data.redirect || 'http://127.0.0.1:8000/home/livros/';
        })
        .catch(error => {
            alert('Erro ao alterar os dados:', error);
            console.error('Erro ao alterar os dados:', error);
            // Tratar erros, se necessário
        });
    }
}