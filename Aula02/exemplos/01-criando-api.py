# Descrição: Código de exemplo para criar uma API com FastAPI

# Importando a biblioteca:
# FastAPI - Biblioteca para criação de APIs
# uvicorn - Servidor HTTP para rodar a API

from fastapi import FastAPI
import uvicorn

# Criando uma instância da classe FastAPI
app = FastAPI()

# Criando uma rota para a raiz da API (http://localhost:8000/)
@app.get("/")
def root(): # Função que será executada quando a rota for acessada
    return {"message": "Meu primeiro código FastAPI"} # Retorno da função

if __name__ == "__main__":
    
    uvicorn.run(app) # Rodando a API. A API estará disponível em http://localhost:8000