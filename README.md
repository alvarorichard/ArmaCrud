# Arma CRUD

# Como subir

precisa tar instalado:

- Docker
- Docker Compose
- Python 3.9+

## Banco de dados

Suba o postgresql com docker compose

```sh
# ou docker-compose
sudo docker-compose up -d
```

Crie a tabela com seu cliente favorito

```sql
CREATE TABLE users (
   id UUID PRIMARY KEY,
   username VARCHAR(50) NOT NULL,
   password VARCHAR(50) NOT NULL
);
```

## Backend

```sh
python -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
python armacrud
```

Pronto deve estar tudo online

# Requisicoes

## Criar

```sh
curl --request POST \
  --url http://127.0.0.1:5000/create \
  --header 'Content-Type: application/json' \
  --data '{
 	"user": "USUARIO",
	"pass": "SENHA"
}'{
	"error": 0,
	"message": "deleted 3d4ad4ad-b93d-49c0-ba78-e105ade47623"
}
```

### Deve Retorna:

```json
{
  "error": 0
}
```

## Ler

```sh
 curl --request GET \
  --url http://127.0.0.1:5000/read
```

### Deve retornar

```json
[
  {
    "id": "df845519-2648-450d-b892-469d6824c89e",
    "password": "5179b21fc1d50950b99b4eecaa48c614",
    "username": "mrmoon"
  },
  {
    "id": "b81757c7-c71a-42c0-96ec-976f23d79fdd",
    "password": "01c860da53e2e7ebd2ae0b30b62eb762",
    "username": "banana"
  },
  {
    "id": "3d4ad4ad-b93d-49c0-ba78-e105ade47623",
    "password": "5299c79aeb8eb1f87039ed87ac9d15db",
    "username": "pessoa"
  }
]
```

## Atualizar

```sh
curl --request POST \
  --url http://127.0.0.1:5000/update \
  --header 'Content-Type: application/json' \
  --data '{
	"uuid": "3d4ad4ad-b93d-49c0-ba78-e105ade47623",
	"update": {
		"user": "novo_usuario",
		"pass": "nova_senha"
	}
}'

```

### Deve retornar

```json
{
  "error": 0,
  "message": "Updated 3d4ad4ad-b93d-49c0-ba78-e105ade47623"
}
```

## Deletar

```sh
curl --request POST \
  --url http://127.0.0.1:5000/delete \
  --header 'Content-Type: application/json' \
  --data '{
	"id": "3d4ad4ad-b93d-49c0-ba78-e105ade47623"
}'
```

### Deve retornar

```json
{
  "error": 0,
  "message": "deleted 3d4ad4ad-b93d-49c0-ba78-e105ade47623"
}
```



# Documentação das funções

O código apresentado define um servidor Flask com quatro rotas para manipulação de dados de usuários armazenados em um banco de dados PostgreSQL.
get_conn()

Função responsável por estabelecer uma conexão com o banco de dados usando a biblioteca psycopg2.
read()

Rota para leitura de todos os dados dos usuários na tabela "users" do banco de dados. A função estabelece uma conexão com o banco de dados usando get_conn(), cria um cursor para a conexão com cursor_factory=RealDictCursor (que retorna os dados em formato de dicionário), executa uma consulta SQL para selecionar todos os dados da tabela "users", recupera todos os dados usando fetchall(), fecha o cursor e a conexão e retorna os dados em formato JSON. Se houver algum erro durante a execução da função, um objeto JSON de erro é retornado.
update()

Rota para atualização de dados de um usuário na tabela "users". A função obtém os dados enviados pelo cliente usando request.get_json(), estabelece uma conexão com o banco de dados usando get_conn(), cria um cursor para a conexão com cursor_factory=RealDictCursor, cria um hash MD5 da senha fornecida pelo cliente, executa uma consulta SQL para atualizar o usuário com o ID fornecido pelo cliente, fecha o cursor e a conexão e retorna um objeto JSON com uma mensagem de sucesso se a atualização for bem-sucedida. Caso contrário, um objeto JSON de erro é retornado.
create()

Rota para a criação de um novo usuário na tabela "users". A função obtém os dados enviados pelo cliente usando request.get_json(), estabelece uma conexão com o banco de dados usando get_conn(), cria um cursor para a conexão, cria um hash MD5 da senha fornecida pelo cliente, gera um ID aleatório usando a biblioteca uuid4, executa uma consulta SQL para inserir o novo usuário na tabela "users", fecha o cursor e a conexão e retorna um objeto JSON com uma mensagem de sucesso se a criação for bem-sucedida. Caso contrário, um objeto JSON de erro é retornado.
delete()

Rota para exclusão de um usuário da tabela "users". A função obtém os dados enviados pelo cliente usando request.get_json(), estabelece uma conexão com o banco de dados usando get_conn(), cria um cursor para a conexão, executa uma consulta SQL para excluir o usuário com o ID fornecido pelo cliente, fecha o cursor e a conexão e retorna um objeto JSON com uma mensagem de sucesso se a exclusão for bem-sucedida. Caso contrário, um objeto JSON de erro é retornado.
main()

Função que inicia a execução do servidor Flask com a função app.run().

