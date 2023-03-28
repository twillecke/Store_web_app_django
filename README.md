<h1 align="center">"All-in-One" e-store | Django</h1>

<p align="center">
<img align="middle" src="https://github.com/twillecke/Store_web_app_django/blob/main/core/static/core/logo.svg" width="40%" height="40%">
</p>

## Requisitos

Python 3.x https://www.python.org/downloads/ <br>
Pipenv `pip install pipenv`<br>
MySQL Community Server 8.0.32 https://dev.mysql.com/downloads/mysql/ <br>
MySQL Workbench 8.0.32 https://dev.mysql.com/downloads/workbench/

## Setup

1. Clone este repositório no seu PC `git clone https://github.com/twillecke/Store_web_app_django`
2. Ative o ambiente virtual e instale as dependências do projeto `pipenv install` ou `pipenv install -r requirements.txt`
3. Configure o login do MySQL e crie uma base de dados com MySQL Workbench `CREATE DATABASE storefront2;`
4. Em storefront/settings/dev.py configure o nome da base de dados e login de acordo com o item 4.

<p align="center">
<img align="middle"
src="https://drive.google.com/uc?export=view&id=1c8kthbpOze1oaROMjKEpozT4m02IsUPA" width="60%">
</p>

5. No terminal inicie o servidor do Django `python3 manage.py runserver`
6. Acesse o app em http://localhost:8000/ ou http://127.0.0.1:8000/

## O que é?
Esse é um projeto com objetivo de desenvolver o backend de um web app de comércio com Python Django. 

As features são as seguintes:
- Base de dados modelada com Django ORM e servidor MySQL;
- Modelos de Produtos, Carrinhos, Clientes, Coleções, Tags, Usuários, Promoção, Compra e Review;
- Base de dados populada com produtos para testes;
- sistema de criação e autenticação de usuário com Djoser e JSON web tokens;
- painel do administrador configurada para visualizar e operar CRUD com a base de dados;
- APIs todas no padrão RESTful com Django REST Framework;
- APIs seguras exigindo níveis de privilégio e autenticação para CRUD dependendo do contexto. (Ex. apenas o admin pode modificar Produtos);
- APIs de "carrinho de compra" e "itens de compra" funcionais.
- Upload de imagens para os Produtos;
- Testes automatizados com pytest e django-pytest de operações CRUD em "Coleções".

## Diagrama da base de dados

<p align="center">
<img align="middle"
src="https://drive.google.com/uc?export=view&id=1sJOMRDFHLXld33FiD36YO-_hgXB5bdpQ" width="80%">
</p>


## Próximas metas
- Implementar interface frontend
- Implementar testes nas demais funcionalidades do app
- Otimizar queryes
