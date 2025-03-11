Uma API simples desenvolvida com Django Ninja para gerenciar livros, permitindo cadastro, avaliação e sorteio de livros com base em filtros.

Tecnologias Usadas
 -Python 3.x
 -Django
 -Django Ninja (para criação da API)
SQLite (ou PostgreSQL para produção)

1- Criar um Livro
POST /livros/

2- Avaliar um Livro
PUT /livros/{livro_id}/

3- Deletar um Livro
DELETE /livros/{livro_id}/

4️- Sortear um Livro com Filtros
GET /livros/sortear/
