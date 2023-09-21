# Usa a imagem oficial do Python como base
FROM python:3.8

# Define as variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Cria o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências do projeto
COPY requirements.txt /app/

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do projeto para o contêiner
COPY . /app/

# Verifica o sistema base para instalação do cliente PostgreSQL
RUN chmod a+x ./install_postgresql.sh
RUN /app/install_postgresql.sh

# Expõe a porta do servidor Django
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "bibliotech_back.wsgi:application"]