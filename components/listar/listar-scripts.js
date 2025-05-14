const HOST = "http://localhost:8080"
/** Exemplo prático de chamada em API  */
async function listar() {
    let response = await fetch(HOST + "/backend/listar")
    let livros = await response.json()

    let table = document.getElementById("listarLivros")
    if (table != null) {
        let tbody = table.getElementsByTagName('tbody')[0]
        // listarLivros.innerHTML = ""

        livros.forEach(livro => {
            let tr = document.createElement("tr")

            let tdTitulo = document.createElement("td")
            tdTitulo.innerText = livro.titulo
            tr.appendChild(tdTitulo)
            /**
             * Termine de preencher a tabela de livros
             */

            let tdAcao = document.createElement("td")
            let btnEditar = document.createElement("a")
            btnEditar.innerText = "Editar"
            btnEditar.href = HOST + "/editar?id="+livro.id
            tdAcao.appendChild(btnEditar)

            tr.appendChild(tdAcao)

            tbody.appendChild(tr)
        });
    }
}

listar()