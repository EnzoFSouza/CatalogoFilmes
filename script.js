const API_URL = 'http://127.0.0.1:8000/filmes';

// Função para buscar filmes (GET)
async function carregarFilmes() {
    const response = await fetch(API_URL);
    const filmes = await response.json();
    const tableBody = document.getElementById('filmesTableBody');
    tableBody.innerHTML = '';

    filmes.forEach(filme => {
        tableBody.innerHTML += `
            <tr>
                <td>${filme.id}</td>
                <td>${filme.titulo}</td>
                <td>${filme.genero}</td>
                <td>${filme.nota}</td>
                <td>${filme.classificacao}</td>
                <td>${filme.onde_assistir}</td>
                <td>
                    <button onclick="deletarFilme(${filme.id})" class="btn-delete">Excluir</button>
                </td>
            </tr>
        `;
    });
}

// Função para criar filme (POST)
document.getElementById('filmeForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const novoFilme = {
        titulo: document.getElementById('titulo').value,
        genero: document.getElementById('genero').value,
        nota: parseInt(document.getElementById('nota').value),
        classificacao: document.getElementById('classificacao').value,
        onde_assistir: document.getElementById('ondeAssistir').value
    };

    await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(novoFilme)
    });

    e.target.reset();
    carregarFilmes();
});

// Função para deletar (DELETE)
async function deletarFilme(id) {
    if (confirm('Deseja excluir este filme?')) {
        await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
        carregarFilmes();
    }
}

carregarFilmes();