# Descrição: Código de exemplo para criar uma API com FastAPI

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return {"mensagem": "Meu primeiro código FastAPI"}

@app.post("/orders/")
def create_item(item: str, quantidade: int, preco_unitario: float = 3.70):
    
    order = {"item": item,
             "quantidade": quantidade,
             "preco_unitario": preco_unitario,
             "total": quantidade * preco_unitario}

    return order

if __name__ == "__main__":
    
    uvicorn.run(app) # Rodando a API. A API estará disponível em http://localhost:8000