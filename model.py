# Importa pipeline de classificação zero-shot do Hugging Face Transformers
from transformers import pipeline
# Importa módulo de expressões regulares para processamento de texto
import re

# Inicializa o classificador usando modelo BART pré-treinado do Facebook
# Modelo: facebook/bart-large-mnli - especializado em classificação de similaridade textual
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classificar_email(texto):
    """
    Classifica um email como 'Produtivo' ou 'Improdutivo'.
    
    Args:
        texto (str): Texto do email a ser classificado
        
    Returns:
        str: Categoria do email ('Produtivo' ou 'Improdutivo')
    """
    # Limpa o texto removendo caracteres inválidos e formatações
    new_texto = limpar_texto(texto)
    
    # Define as categorias possíveis para classificação
    labels = ["Produtivo", "Improdutivo"]
    
    # Executa a classificação usando o modelo BART
    resultado = classifier(new_texto, labels)
    
    # Extrai a categoria com maior confiança (primeira do resultado)
    categoria = resultado['labels'][0]
    
    return categoria


def gerar_resposta(categoria):
    """
    Gera uma resposta automática baseada na categoria do email.
    
    Args:
        categoria (str): Categoria do email classificado
        
    Returns:
        str: Mensagem de resposta apropriada para a categoria
    """
    # Se o email é produtivo, envia resposta detalhada
    if categoria == "Produtivo":
        return "Obrigado pelo contato! Sua solicitação foi recebida e será analisada em breve."
    # Caso contrário, envia resposta genérica
    else:
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
    # Substitui quebras de linha por espaço
    texto = texto.replace('\n', ' ')
    
    # Remove múltiplos espaços consecutivos usando regex
    texto = re.sub(r'\s+', ' ', texto)
    
    # Codifica em UTF-8 ignorando caracteres inválidos, depois decodifica
    texto = texto.encode('utf-8', 'ignore').decode('utf-8')
    
    # Remove espaços em branco no início e final
    return texto.strip()