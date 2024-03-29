<h1 align="center">"All-in-One" e-store</h1>

<p align="center">
<img align="middle" src="https://github.com/twillecke/Store_web_app_django/blob/main/core/static/core/logo.svg" width="60%" height="60%">
</p>

## O que é?
Este projeto tem como objetivo o desenvolvimento do backend de um aplicativo web de comércio, usando o framework Python Django.

As principais funcionalidades do projeto incluem:
<ul>
<li>Modelagem do banco de dados com Django ORM e servidor MySQL.</li>
<ul>
<li>Modelos para Produtos, Carrinhos, Clientes, Coleções, Tags, Usuários, Promoção, Compra e Review.</li>
<li>Banco de dados pré-populado com produtos para fins de teste.</li>
</ul>
<li>Sistema de criação e autenticação de usuário usando o Djoser e JSON web tokens.</li>
<li>Painel do administrador configurado para visualização e operações CRUD com o banco de dados.</li>
<li>APIs no padrão RESTful implementadas com o Django REST Framework.</li>
<ul>
<li>APIs protegidas por autenticação e diferentes níveis de privilégio.</li>
<li>APIs para "carrinho de compra" e "itens de compra".</li>
</ul>
<li>Upload de imagens para os Produtos.</li>
<li>Testes unitários na API "collections" com pytest e django-pytest.</li>
</ul>

## Requisitos

Python 3.x https://www.python.org/downloads/ <br>
Pipenv `pip install pipenv`<br>
MySQL Community Server 8.0.32 https://dev.mysql.com/downloads/mysql/ <br>
MySQL Workbench 8.0.32 https://dev.mysql.com/downloads/workbench/

## Setup

1. Clone este repositório em seu computador: `git clone https://github.com/twillecke/Store_web_app_django`
2. Ative o ambiente virtual e instale as dependências do projeto: `pipenv install` ou `pipenv install -r requirements.txt`
3. Configure o login do servidor MySQL e crie uma base de dados usando o MySQL Workbench: `CREATE DATABASE storefront2;`
4. Em storefront/settings/dev.py, configure o nome da base de dados e login de acordo com o item 3. 

<p align="center">
<img align="middle"
src="https://drive.google.com/uc?export=view&id=1c8kthbpOze1oaROMjKEpozT4m02IsUPA" width="80%">
</p>

5. Propague os modelos do projeto para o esquema da base de dados configurada: `python manage.py makemigrations` e `python manage.py migrate`
7. Crie uma conta administrador para acessar o "Admin Panel": `python manage.py createsuperuser`
8. Inicie o servidor do Django no terminal: `python manage.py runserver`
9. Acesse o aplicativo em: http://localhost:8000/ ou http://127.0.0.1:8000/

<h1>Mais informações</h1> 

## Diagrama da base de dados

<p align="center">
<img align="middle"
src="https://drive.google.com/uc?export=view&id=1sJOMRDFHLXld33FiD36YO-_hgXB5bdpQ" width="80%">
</p>

O esquema de base de dados  possui várias entidades que se relacionam entre si. A entidade "Product" é uma das principais, possuindo um título, uma descrição, um preço unitário, um inventário, a última atualização e uma coleção - relacionada através de uma chave estrangeira com a entidade "Collection" -. Ela também possui uma relação many-to-many com a entidade "Promotion", o que permite que um produto possa participar de várias promoções diferentes.

## Admin Panel

A página do administrador é uma feature nativa do Django. Nesse projeto ela foi customizada para os propósitos de uma loja online permitindo o controle de produtos, clientes, coleções, níveis de privilégio, etc.

A página é acessada em http://127.0.0.1:8000/admin/ com o login do administrador.


## Próximas metas 
- Implementar interface frontend
- Implementar testes nas demais funcionalidades do app
- Otimizar queryes
