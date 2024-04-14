# Descrição: Código de exemplo para criar uma API com FastAPI

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Meu primeiro código FastAPI"}

@app.get("/pedido/")
def lendo_item(item: str, quantidade: int, valor: int):
    return {"item": item, 
            "quantidade": quantidade,
            "valor": valor,
            "total": quantidade * valor}

if __name__ == "__main__":
    
    uvicorn.run(app) # Rodando a API. A API estará disponível em http://localhost:8000