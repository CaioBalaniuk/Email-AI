# 📧 AutoU — Classificador de Emails

Aplicação web que classifica emails como **Produtivo** ou **Improdutivo** usando modelos Hugging Face.

> Observação: este README foi atualizado para refletir as dependências atuais do arquivo `requirements.txt`.

---

## Resumo rápido

- Backend: Flask (Python)
- Modelo usado: `nlptown/bert-base-multilingual-uncased-sentiment` (pipeline `sentiment-analysis`)
- Interpretação usada no projeto:
  - 1–2 stars → Improdutivo
  - 3–5 stars → Produtivo
- Regras adicionais (heurística): palavras-chave como `natal`, `reclamação`, `festas`, `festa`, `promoção` são classificadas automaticamente como "Improdutivo".

## 🎯 Sobre o Projeto

AutoU é uma solução automatizada para classificação de emails. O aplicativo utiliza o modelo BART (Facebook) pré-treinado em classificação zero-shot para determinar se um email é produtivo ou improdutivo, gerando respostas automáticas apropriadas.

## ✨ Funcionalidades

- ✅ **Classificação de Emails**: Classifica emails em duas categorias (Produtivo/Improdutivo)
- ✅ **Upload de Arquivos**: Suporte para arquivos PDF e TXT
- ✅ **Entrada de Texto**: Cole diretamente o conteúdo do email
- ✅ **Geração de Respostas**: Respostas automáticas baseadas na categoria
- ✅ **Interface Responsiva**: Funciona em desktop, tablet e celular
- ✅ **Experiência de Usuário**: Loader animado durante o processamento

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.8+, Flask
- **Machine Learning**: Hugging Face Transformers (BART)
- **Frontend**: HTML5, CSS3, JavaScript
- **Processamento**: PyPDF2 (leitura de PDFs)

## Dependências (conforme requirements.txt)

Conteúdo atual de `requirements.txt`:

```
flask==3.0.2
transformers==4.35.2
tokenizers==0.15.0
pypdf2==3.0.1
sentencepiece==0.1.99
```

Observações:

- `transformers` precisa de um backend (PyTorch ou TensorFlow). O projeto não fixa `torch` no `requirements.txt` — instale `torch` manualmente se necessário (ex.: `pip install torch` ou a build CUDA apropriada).
- `pypdf2` está incluído para extração de texto de PDFs (PDFs baseados em imagem não são tratados automaticamente — veja a seção de problemas comuns).

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git (opcional, para clonar o repositório)

## 🚀 Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/AutoU.git
cd AutoU
```

### 2. Crie um ambiente virtual

**No Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**No macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Instale PyTorch (se não estiver instalado). Exemplo CPU-only:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

Para GPU, siga as instruções oficiais do PyTorch para escolher a build CUDA correta.

### 5. Execute a aplicação

```bash
python app.py
```

A aplicação estará disponível em: **http://localhost:5000**

## 📁 Estrutura do Projeto

```
AutoU/
├── app.py                      # Aplicação Flask principal
├── model.py                    # Funções de classificação e processamento
├── requirements.txt            # Dependências do projeto
├── README.md                   # Este arquivo
├── templates/
│   └── index.html             # Template HTML principal
└── static/
    ├── style.css              # Estilos CSS
    └── images/
        └── logo.jpeg          # Logo da aplicação
```

## 🎨 Como Usar

1. **Acesse a aplicação** em http://localhost:5000
2. **Escolha uma opção**:
   - Faça upload de um arquivo (`.pdf` ou `.txt`)
   - Ou cole o texto do email diretamente na textarea
3. **Clique em "Classificar Email"**
4. **Aguarde o processamento** (exibe animação de carregamento)
5. **Veja o resultado** com a categoria e resposta sugerida

## 🔧 Configuração

### Modelo de IA

O projeto utiliza o modelo `facebook/bart-large-mnli` do Hugging Face. Primeira execução pode levar tempo para baixar o modelo (aproximadamente 1.6GB).

### Categorias de Classificação

- **Produtivo**: Emails com conteúdo relevante e acionável
- **Improdutivo**: Emails spam, marketing ou não relacionados

## 🖥️ Responsividade

A aplicação foi desenvolvida com design responsivo:

- **Desktop**: Layout completo otimizado
- **Tablet**: Adaptação para telas médias (até 768px)
- **Celular**: Layout mobile (até 480px)

## 📝 Exemplos de Uso

### Upload de PDF

1. Selecione um arquivo `.pdf`
2. O sistema extrai automaticamente o texto
3. Classifica o conteúdo

### Cole de Texto

1. Copie o conteúdo do email
2. Cole na área de texto
3. Clique em classificar

## 🐛 Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'transformers'"

**Solução**: Instale as dependências

```bash
pip install -r requirements.txt
```

### Erro: "Port 5000 already in use"

**Solução**: Mude a porta no arquivo `app.py`:

```python
app.run(debug=True, port=5001)
```

### Lentidão na primeira execução

**Causa**: Primeiro download do modelo BART (1.6GB)  
**Solução**: Aguarde alguns minutos, próximas execuções serão mais rápidas

## 📖 Documentação do Código

### `app.py`

- **Função `index()`**: Rota principal que processa o formulário
- Trata upload de PDF/TXT e texto digitado
- Retorna categoria e resposta gerada

### `model.py`

- **`classificar_email(texto)`**: Classifica o email usando BART
- **`gerar_resposta(categoria)`**: Gera resposta automática
- **`limpar_texto(texto)`**: Processa e normaliza o texto

### `style.css`

- Estilos responsivos com Flexbox
- Media queries para diferentes tamanhos de tela
- Animações suaves (hover, spinner)

## 🎯 Melhorias Futuras

- [ ] Adicionar mais categorias de classificação
- [ ] Integração com APIs de email (Gmail, Outlook)
- [ ] Armazenamento de histórico de classificações
- [ ] Suporte a múltiplos idiomas
- [ ] Dashboard com estatísticas
- [ ] Sistema de feedback para melhorar o modelo

## 👨‍💻 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📞 Suporte

Para dúvidas ou problemas, abra uma issue no repositório GitHub ou entre em contato.

## 👏 Agradecimentos

- [Hugging Face](https://huggingface.co/) - Pelos modelos de IA
- [Flask](https://flask.palletsprojects.com/) - Framework web
- [Transformers](https://huggingface.co/docs/transformers/) - Biblioteca de NLP

---

Última atualização: Novembro de 2025
