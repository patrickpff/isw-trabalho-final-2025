import cgi
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json

class serverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        print("Tratamento do GET")
        print(self.path)
        # Carregar os arquivos da pasta STATIC, se existir
        if self.path.startswith('/static/') or self.path.startswith('/components/'):
            filepath = self.path.lstrip('/')
            if os.path.exists(filepath):
                self.send_response(200)
                if filepath.endswith('.css'):
                    # Se tiver arquivo .css, envia no header o content-type 
                    # para informar o navegador que existem arquivos 
                    # css para serem carregados
                    self.send_header("Content-Type", "text/css")
                    self.end_headers()

                    with open(filepath, 'rb') as file:
                        self.wfile.write(file.read())
                    return
                elif filepath.endswith('.js'):
                    # Se tiver arquivo .js, envia no header o content-type 
                    # para informar o navegador que existem arquivos 
                    # js para serem carregados
                    self.send_header("Content-Type", "application/javascript")
                    self.end_headers()

                    with open(filepath, 'rb') as file:
                        self.wfile.write(file.read())
                    return
                elif filepath.endswith('.html'):
                    # Se tiver arquivo .html, envia no header o content-type 
                    # para informar o navegador que existem arquivos 
                    # html para serem carregados
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                    self.end_headers()

                    with open(filepath, 'rb') as file:
                        self.wfile.write(file.read())
                    return
                # self.end_headers()

                # with open(filepath, 'rb') as file:
                #     self.wfile.write(file.read())
                
                # return
            else :
                self.send_response(400)
                self.end_headers()
                self.wfile.write("Arquivo não encontrado".encode('utf-8'))
                return
        
        directory = os.path.dirname(os.path.abspath(__file__))
        # Adicione suas rotas a partir daqui!
        if self.path.startswith('/sobre'):
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            data = directory + "/components/sobre/sobre.html"
            
            with open(data, 'r', encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                self.wfile.write(conteudo.encode('utf-8'))
                
            return
        
        if self.path.startswith('/cadastrar'):
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            data = directory + "/components/cadastrar/cadastrar.html"
            
            with open(data, 'r', encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                self.wfile.write(conteudo.encode('utf-8'))
                
            return
        
        if self.path.startswith('/listar'):
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            data = directory + "/components/listar/listar-view.html"
            
            with open(data, 'r', encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                self.wfile.write(conteudo.encode('utf-8'))
            
            return
        
        if self.path.startswith('/editar'):
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            data = directory + "/components/cadastrar/editar.html"
            
            with open(data, 'r', encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                self.wfile.write(conteudo.encode('utf-8'))
                
            return

        if self.path.startswith('/backend/listar'):
            # caminho do arquivo
            try:
                file_path = os.path.join("data", "dados.json")
                
                # abre o arquivo como somente leitura (r) e encoding utf8
                with open(file_path, "r", encoding="utf-8") as file:
                    data = file.read()
                # envio de resposta

                self.send_response(200)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(data.encode("utf-8"))
            except FileNotFoundError:
                # Se o arquivo pessoas.json não for encontrado
                self.send_response(404)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                error_message = json.dumps({"error": "Arquivo não encontrado!"})
                self.wfile.write(error_message.encode("utf-8"))
            except Exception as e:
                # Se acontecer outro erro qualquer
                self.send_response(500)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                error_message = json.dumps({"error": str(e)})
                self.wfile.write(error_message.encode("utf-8"))
            
            return
        # Código de Status da chamada: 200 = sucesso
        self.send_response(200) 

         # Especifica o tipo de conteúdo e o conjunto de caracteres
        self.send_header("Content-type", "text/html; charset=utf-8")

        # Finaliza o cabeçalho
        self.end_headers()

        with open('index.html', 'r', encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            self.wfile.write(conteudo.encode('utf-8'))
    
    def do_POST(self):
        print("Tratamento do POST")

def main():
    print('Chama servidor')
    server = None

    try:
        port = 8080
        server = HTTPServer(('', port), serverHandler)
        print("Servidor rodando na porta: {}" . format(port))
        server.serve_forever()

    except KeyboardInterrupt:
        print("Servidor sendo finalizado...")
        server.socket.close()


main()