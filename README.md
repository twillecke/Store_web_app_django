<h1 align="center">"All-in-One" e-store | Django</h1>

<p align="center">
<img align="middle" src="https://github.com/twillecke/Store_web_app_django/blob/main/core/static/core/logo.svg" width="40%" height="40%">
</p>

## Requisitos

Python 3.x;
Pipenv `pip install pipenv`;

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

## Como testar?
- Clone este repositório no seu PC;
- Instale as dependências com `pipenv install`
- No terminal ative o servidor do Django `python3 manage.py runserver`
- Acesse o app em http://localhost:8000/store ou http://127.0.0.1:8000/store

## Próximas metas
- Implementar interface frontend
- Implementar testes nas demais funcionalidades do app
- otimizar queryes
