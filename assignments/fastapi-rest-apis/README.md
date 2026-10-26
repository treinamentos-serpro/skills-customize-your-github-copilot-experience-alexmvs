# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a criar uma API REST com FastAPI, definindo rotas, validando dados com modelos Pydantic e implementando operações CRUD com respostas HTTP apropriadas.

## 📝 Tasks

### 🛠️ Criar a API e listar livros

#### Descrição
Prepare o ambiente, crie a aplicação FastAPI e implemente endpoints para verificar se a API está funcionando e listar os livros disponíveis.

#### Requisitos
O programa concluído deve:

- Instalar FastAPI e Uvicorn e permitir iniciar a aplicação com `uvicorn main:app --reload`
- Expor `GET /health`, retornando um objeto JSON que indique que a API está funcionando
- Expor `GET /books`, retornando uma lista JSON de livros
- Representar cada livro com pelo menos `id`, `title` e `author`

### 🛠️ Criar e buscar livros

#### Descrição
Adicione a criação de livros com validação dos dados recebidos e implemente uma rota para buscar um livro pelo identificador.

#### Requisitos
O programa concluído deve:

- Definir um modelo Pydantic para validar os dados de entrada; `title` e `author` não podem ser vazios
- Expor `POST /books` para criar um livro e retornar o livro criado com status HTTP `201`
- Gerar um identificador único para cada livro criado
- Expor `GET /books/{book_id}` para retornar um livro existente ou status HTTP `404` quando ele não existir
- Confirmar que dados inválidos enviados para `POST /books` recebem uma resposta de validação `4xx`

### 🛠️ Atualizar e excluir livros

#### Descrição
Complete as operações CRUD permitindo atualizar e excluir um livro. Use as mesmas regras de busca por identificador das tarefas anteriores.

#### Requisitos
O programa concluído deve:

- Expor `PUT /books/{book_id}` para atualizar o título e o autor de um livro existente
- Expor `DELETE /books/{book_id}` para excluir um livro existente
- Retornar status HTTP `404` ao tentar atualizar ou excluir um identificador inexistente
- Verificar que as alterações e exclusões também são refletidas em `GET /books`
