const HOST = "http://localhost:8080"
/** Exemplo prático de chamada em API  */
async function listar() {
    let response = await fetch(HOST + "/backend/listar")
    let livros = await response.json()

    let table = document.getElementById("listarLivros")
    let tbody = table.getElementsByTagName('tbody')[0]
    // listarLivros.innerHTML = ""

    livros.forEach(livro => {
        let tr = document.createElement("tr")

        let tdTitulo = document.createElement("td")
        tdTitulo.innerText = livro.titulo
        tr.appendChild(tdTitulo)

        let tdAutor = document.createElement("td")
        tdAutor.innerText = livro.autor
        tr.appendChild(tdAutor)

        let tdPaginas = document.createElement("td")
        tdPaginas.innerText = livro.paginas
        tr.appendChild(tdPaginas)

        let tdEditora = document.createElement("td")
        tdEditora.innerText = livro.editora
        tr.appendChild(tdEditora)

        let tdAno = document.createElement("td")
        tdAno.innerText = livro.ano
        tr.appendChild(tdAno)

        tbody.appendChild(tr)
        // console.log(livro)
    });
}

listar()