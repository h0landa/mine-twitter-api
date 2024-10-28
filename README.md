# Projeto Mine-Twitter-API

Este projeto é uma API desenvolvida com Django e Django REST Framework. Este README fornece instruções sobre como configurar e rodar o projeto localmente usando Docker.

## Pré-requisitos

Antes de começar, você precisará ter os seguintes softwares instalados:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3](https://python.org.br/instalacao-windows/)

## Configuração do Ambiente

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/h0landa/mine-twitter-api.git
   cd mine-twitter-api
2. **Crie o arquivo .env**:
   Vou deixar um arquivo .env-example para facilitar

3. **Instale as dependências**:
   As dependências do projeto estão listadas no arquivo requirements.txt. Elas serão instaladas automaticamente ao construir a imagem do Docker.
## Construindo e Executando Projeto

1. **Construa a imagem Docker**:
   Execute o seguinte comando para construir a imagem Docker e iniciar os containers:
    ```bash
   docker build -t mine-twitter-api .
    
2. **Ligar**:
    ```bash
   docker-compose up
    
3. **Realize as migrações do banco**:
   ```bash
   docker-compose run web python manage.py migrate

## EU TENTANDO APRENDER DOCKER:
![](https://github.com/h0landa/mine-twitter-api/blob/main/GUTS.gif)
