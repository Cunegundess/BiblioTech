# Usa a imagem oficial do Python como base
FROM python:3.8

# Define as variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Cria o diretório de trabalho
WORKDIR /app

# Verifica o sistema base para instalação do cliente PostgreSQL
RUN if [ -x "$(command -v pacman)" ]; then \
        pacman -Sy --noconfirm postgresql && \
        rm -rf /var/cache/pacman/pkg/* ; \
    elif [ -x "$(command -v apt-get)" ]; then \
        apt-get update && \
        apt-get install -y --no-install-recommends postgresql postgresql-contrib && \
        rm -rf /var/lib/apt/lists/* ; \
    fi

# Copia os arquivos de dependências do projeto
COPY requirements.txt /app/

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do projeto para o contêiner
COPY . /app/

# Expõe a porta do servidor Django
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "bibliotech_back.wsgi:application"]