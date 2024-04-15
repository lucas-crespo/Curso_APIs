# Descrição: Código de exemplo para criar uma API com FastAPI

from fastapi import FastAPI
import uvicorn
from sqlmodel import SQLModel

app = FastAPI()


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

class Pedido(SQLModel):
    item: str
    quantidade: int
    preco_unitario: float

    
@app.get("/")
def root():
    return {"mensagem": "Meu primeiro código FastAPI"}

# CREATE
@app.post("/orders/")
def create_order(item: Pedido):

        order = {"id": max([order["id"] for order in PEDIDOS]) + 1,
                "item": item.item,
                "quantidade": item.quantidade,
                "preco_unitario": item.preco_unitario,
                "total": item.quantidade * item.preco_unitario}
    
        PEDIDOS.append(order)
        return order
    
# READ
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in PEDIDOS:
        if order["id"] == order_id:
            return order
    return {"mensagem": "Pedido não encontrado"}

# UPDATE
@app.put("/orders/{order_id}")
def update_order(order_id: int, item: Pedido):
    for order in PEDIDOS:
        if order["id"] == order_id:
            order["item"] = item.item
            order["quantidade"] = item.quantidade
            order["preco_unitario"] = item.preco_unitario
            order["total"] = item.quantidade * item.preco_unitario
            return order
    return {"mensagem": "Pedido não encontrado"}

# DELETE
@app.delete("/orders/{order_id}")
def delete_order(order_id: int):
    for order in PEDIDOS:
        if order["id"] == order_id:
            PEDIDOS.remove(order)
            return {"mensagem": "Pedido removido com sucesso"}
    return {"mensagem": "Pedido não encontrado"}

if __name__ == "__main__":
    
    uvicorn.run(app) # Rodando a API. A API estará disponível em http://localhost:8000