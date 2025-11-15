from transformers import pipeline
import re

# Inicializa um classificador leve baseado em BERT multilíngue.
# Usa "nlptown/bert-base-multilingual-uncased-sentiment" que retorna labels tipo "1 star"..."5 stars".
# Escolhi este modelo por ser mais leve e suportar múltiplos idiomas (inclui PT-BR).
classificador = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def classificar_email(texto):
    # Normaliza e limpa o texto recebido para reduzir ruído
    texto = limpar_texto(texto)

    # Lista de palavras-chave que indicam email improdutivo
    palavras_improdutivas = ["natal", "reclamação", "festas", "festa", "promoção"]
    
    # Verifica se alguma palavra-chave improdutiva está presente no texto (comparação em minúsculas)
    if any(palavra in texto.lower() for palavra in palavras_improdutivas):
        # Retorna diretamente "Improdutivo" sem chamar o modelo (regra simples)
        return "Improdutivo"
    if (len(texto) < 10):
        return "Improdutivo"
    
    # Chama o pipeline de classificação e obtém o primeiro resultado
    resultado = classificador(texto)[0]
    # O label vem no formato "1 star", "2 stars", etc. Extrai o dígito inicial e converte para int
    estrelas = int(resultado["label"][0])
    # Imprime número de estrelas no console para debug/monitoramento
    print(estrelas)
    # Interpreta 3-5 estrelas como conteúdo produtivo, 1-2 como não produtivo
    if estrelas >= 3:
        return "Produtivo"
    else:
        return "Não Produtivo"


def gerar_resposta(classificacao):
    # Gera uma resposta padrão dependendo da classificação recebida
    if classificacao == "Produtivo":
        # Resposta mais completa para mensagens consideradas úteis
        return "Obrigado pelo contato! Sua solicitação foi recebida e será analisada em breve."
    else:
        # Resposta genérica para mensagens não produtivas/improdutivas
        return "Obrigado pelo contato!"
    

def limpar_texto(texto):
    """
    Limpa e normaliza o texto do email para melhor processamento.
    Remove quebras de linha, espaços duplicados e caracteres inválidos.
    
    Args:
        texto (str): Texto bruto do email
        
    Returns:
        str: Texto limpo e normalizado
    """
    # Substitui quebras de linha por espaço para manter fraseado linear
    texto = texto.replace('\n', ' ')
    
    # Remove múltiplos espaços consecutivos usando regex
    texto = re.sub(r'\s+', ' ', texto)
    
    # Codifica em UTF-8 ignorando caracteres inválidos, depois decodifica
    texto = texto.encode('utf-8', 'ignore').decode('utf-8')
    
    # Exibe o texto limpo no console para debug (útil durante desenvolvimento)
    print(repr(texto))
    
    # Remove espaços em branco no início e final e retorna
    return texto.strip()