const HOST = "http://localhost:8080"
/** Exemplo prático de chamada em API  */
async function listar() {
    let response = await fetch(HOST + "/backend/listar")
    let livros = await response.json()
    // let listaTarefas = document.getElementById("listaTarefas")
    listaLivros.innerHTML = ""

    livros.forEach(livro => {
        console.log(livro)
    });
}

listar()