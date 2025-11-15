# Importa Flask para criar a aplicação web
from flask import Flask, render_template, request
# Importa funções de classificação e geração de resposta do módulo model
from model import classificar_email, gerar_resposta
# Importa biblioteca para leitura de arquivos PDF
import PyPDF2
# Importa módulo time para delays (comentado no código)
import time

# Inicializa a aplicação Flask
app = Flask(__name__)

# Define a rota principal da aplicação que aceita requisições GET e POST
@app.route("/", methods=["GET", "POST"])
def index():
    """
    Função principal que processa o formulário de classificação de emails.
    Tratamento de upload de arquivo (PDF/TXT) ou texto digitado.
    
    Returns:
        render_template: Renderiza o template HTML com categoria e resposta
    """
    # Inicializa variáveis de resultado como None
    categoria = resposta = None

    # Verifica se a requisição é do tipo POST (formulário enviado)
    if request.method == "POST":
        # Obtém o arquivo enviado pelo formulário (campo "email")
        arquivo = request.files.get("email")
        # Inicializa string vazia para armazenar o texto do email
        texto = ""

        # Verifica se um arquivo foi enviado e processa de acordo com o tipo
        if arquivo:
            # Se o arquivo é PDF, extrai texto de todas as páginas
            if arquivo.filename.endswith(".pdf"):
                # Cria leitor PDF a partir do arquivo enviado
                leitor = PyPDF2.PdfReader(arquivo)
                # Extrai texto de cada página e concatena
                texto = "".join([p.extract_text() for p in leitor.pages])
            # Se é arquivo de texto simples (TXT)
            else:
                # Lê o conteúdo do arquivo e decodifica de bytes para string
                texto = arquivo.read().decode("utf-8")
        # Se nenhum arquivo foi enviado, obtém o texto digitado na textarea
        else:
            texto = request.form.get("texto_email")
        
        # Debug: imprime o texto para verificação em console
        print(repr(texto))
        
        # Verifica se o texto não está vazio antes de classificar
        if texto != "":
            # Chama função para classificar o email como Produtivo/Improdutivo
            categoria = classificar_email(texto)
            # Gera resposta automática baseada na categoria
            resposta = gerar_resposta(categoria)
        
        # Delay opcional para simular processamento (comentado)
        # time.sleep(2)

    # Renderiza o template HTML passando categoria e resposta como variáveis
    return render_template("index.html", categoria=categoria, resposta=resposta)

# Este bloco só é executado quando rodamos o arquivo diretamente
# Exemplo: python app.py
# Ele não é executado quando o arquivo é importado como módulo
if __name__ == "__main__":

    # Importa o módulo os para acessar variáveis de ambiente
    import os

    # Railway (e outras plataformas) definem a porta em uma variável de ambiente chamada "PORT"
    # Aqui tentamos pegar essa variável. Se não existir, usamos a porta 8080 como padrão.
    port = int(os.environ.get("PORT", 8080))

    # Inicia o servidor Flask
    # host="0.0.0.0" permite que a aplicação seja acessível externamente (não apenas localmente)
    # port=port faz o servidor usar a porta definida pelo ambiente (Railway) ou 8080 localmente
    app.run(host="0.0.0.0", port=port)
