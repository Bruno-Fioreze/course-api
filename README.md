# course_api


### Dependências

- Python
- FastAPI
- Docker
- PIP
- PyTest


## Passos para executar a aplicação.
Caso esteja utilizando windows troque o python3 por python.

- Execute o seguinte comando:
- sudo docker run -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres &
- Conecte-se ao banco de dados utilizando os dados do arquivo .env e crie uma instância chamada db_digital, após isso copie o conteúdo do arquivo chamado dump e insira no banco.
- Entre na pasta do projeto.
- Execute o comando python3 -m venv venv
- No caso do linux, ative a venv com source venv/bin/activate
- No caso do windows, ative a venv com venv/Scripts/Activate
- Execute o comando pip install -r requirements.txt
- Execute o comando uvicorn main:app

## Comandos para executar os testes.
    - Não implementados ainda.
	
## Um pouco sobre a aplicação.
Api foi feita com FastAPI utilizando Autenticação JWT