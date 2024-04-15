# Descrição: Código de exemplo para criar uma API com FastAPI

from fastapi import FastAPI
import uvicorn
from sqlmodel import SQLModel

PEDIDOS = [
    {
        "id": 1,
        "item": "Paper type A2",
        "quantidade": 10,
        "preco_unitario": 75.50,
        "total": 10 * 75.50
    },
    {
        "id": 2,
        "item": "Paper type A3",
        "quantidade": 5,
        "preco_unitario": 95.25,
        "total": 5 * 95.25
    },
    {
        "id": 3,
        "item": "Paper type A4",
        "quantidade": 20,
        "preco_unitario": 105.75,
        "total": 20 * 105.75
    },
]

app = FastAPI()

@app.get("/")
def root():
    return {"mensagem": "Meu primeiro código FastAPI"}


# @app.post("/orders/")
# def create_item(item: str, quantidade: int, valor: float = 3.70):
    
#     order = {"item": item,
#              "quantidade": quantidade,
#              "valor": valor,
#              "total": quantidade * valor}

#     return order


@app.get("/orders/{order_id}")
def create_item(order_id: int):
    
    for order in PEDIDOS:
        if order["id"] == order_id:
            return order

    return {"mensagem": "Pedido não encontrado"}


class Item(SQLModel):
    item: str
    quantidade: int
    valor: float = 3.70


@app.post("/orders/")
def create_item(item: Item):
        
    order = {"item": item.item,
            "quantidade": item.quantidade,
            "valor": item.valor,
            "total": item.quantidade * item.valor}
    
    return order



if __name__ == "__main__":
    
    uvicorn.run(app) # Rodando a API. A API estará disponível em http://localhost:8000