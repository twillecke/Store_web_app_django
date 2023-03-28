<h1 align="center">"All-in-One" e-store</h1>

<p align="center">
<img align="middle" src="https://github.com/twillecke/Store_web_app_django/blob/main/core/static/core/logo.svg" width="40%" height="40%">
</p>

## O que é?
Este projeto tem como objetivo o desenvolvimento do backend de um aplicativo web de comércio, usando o framework Python Django.

As principais funcionalidades do projeto incluem:

- Modelagem do banco de dados com Django ORM e servidor MySQL.
- Modelos para Produtos, Carrinhos, Clientes, Coleções, Tags, Usuários, Promoção, Compra e Review.
- Banco de dados pré-populado com produtos para fins de teste.
- Sistema de criação e autenticação de usuário usando o Djoser e JSON web tokens.
- Painel do administrador configurado para visualização e operações CRUD com o banco de dados.
- Todas as APIs seguindo o padrão RESTful com o Django REST Framework.
- APIs seguras com diferentes níveis de privilégio e autenticação.
- APIs funcionais para "carrinho de compra" e "itens de compra".
- Possibilidade de upload de imagens para os Produtos.
- Testes automatizados para operações CRUD em "Coleções", usando pytest e django-pytest.

## Requisitos

Python 3.x https://www.python.org/downloads/ <br>
Pipenv `pip install pipenv`<br>
MySQL Community Server 8.0.32 https://dev.mysql.com/downloads/mysql/ <br>
MySQL Workbench 8.0.32 https://dev.mysql.com/downloads/workbench/

## Setup

1. Clone este repositório em seu computador com o comando git clone https://github.com/twillecke/Store_web_app_django.
2. Ative o ambiente virtual e instale as dependências do projeto executando `pipenv install` ou `pipenv install -r requirements.txt`.
3. Configure o login do servidor MySQL e crie uma base de dados usando o MySQL Workbench, executando o comando `CREATE DATABASE storefront2;`.
4. Em storefront/settings/dev.py, configure o nome da base de dados e login de acordo com o item 3.

<p align="center">
<img align="middle"
src="https://drive.google.com/uc?export=view&id=1c8kthbpOze1oaROMjKEpozT4m02IsUPA" width="60%">
</p>

5. Propague os modelos do projeto para o esquema da base de dados configurada com o comando python manage.py makemigrations e python manage.py migrate.
6. Inicie o servidor do Django no terminal, digitando python3 manage.py runserver.
7. Acesse o aplicativo em http://localhost:8000/ ou http://127.0.0.1:8000/.


## Diagrama da base de dados

<p align="center">
<img align="middle"
src="https://drive.google.com/uc?export=view&id=1sJOMRDFHLXld33FiD36YO-_hgXB5bdpQ" width="80%">
</p>

O esquema de base de dados  possui várias entidades que se relacionam entre si. A entidade "Product" é uma das principais, possuindo um título, uma descrição, um preço unitário, um inventário, a última atualização e uma coleção - relacionada através de uma chave estrangeira com a entidade "Collection" -. Ela também possui uma relação many-to-many com a entidade "Promotion", o que permite que um produto possa participar de várias promoções diferentes.



## Próximas metas
- Implementar interface frontend
- Implementar testes nas demais funcionalidades do app
- Otimizar queryes
