# Imagem base com Python
FROM python:3.10-slim

# Previne mensagens interativas
ENV PYTHONUNBUFFERED=1

# Define área de trabalho
WORKDIR /app

# Copia requirements
COPY requirements.txt .

# Instala dependências do sistema (para PyPDF2, torch etc)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia tudo
COPY . .

# Expõe porta padrão do Flask
EXPOSE 8080

# Comando pra rodar
CMD ["python", "app.py"]
