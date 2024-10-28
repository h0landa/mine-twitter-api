# Use uma imagem base oficial do Python
FROM python:3.12

# Defina a variável de ambiente para evitar a criação de arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instale as dependências do sistema
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev default-libmysqlclient-dev

RUN mkdir /mine_twitter_api
WORKDIR /mine_twitter_api
COPY . /mine_twitter_api/

RUN pip install -r requirements.txt


# Exponha a porta que o Django usará
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
