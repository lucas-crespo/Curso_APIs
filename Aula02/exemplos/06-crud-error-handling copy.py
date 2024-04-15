# Descrição: Código de exemplo para criar uma API com FastAPI

from fastapi import FastAPI, HTTPException
import uvicorn
from sqlmodel import SQLModel

app = FastAPI(title="API de Pedidos")


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
@app.post("/orders/", status_code=201)
def create_order(item: Pedido):
    """
    Cria um novo pedido com o item fornecido.

    Args:
    - item (Pedido): O item a ser adicionado ao pedido.

    Returns:
    - dict: O pedido criado.

    """
    order = {
        "id": max([order["id"] for order in PEDIDOS]) + 1,
        "item": item.item,
        "quantidade": item.quantidade,
        "preco_unitario": item.preco_unitario,
        "total": item.quantidade * item.preco_unitario
    }

    PEDIDOS.append(order)
    return order
    
# READ
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    """
    Retorna um pedido com base no ID fornecido.

    Args:
    - order_id (int): O ID do pedido a ser buscado.

    Returns:
    - dict: Um dicionário contendo as informações do pedido encontrado.

    Raises:
    - HTTPException: Caso o pedido com o ID fornecido não seja encontrado.
    """
    for order in PEDIDOS:
        if order["id"] == order_id:
            return order
    raise HTTPException(status_code=404, detail=f"Pedido id={order_id} não encontrado")

# UPDATE
@app.put("/orders/{order_id}")
def update_order(order_id: int, item: Pedido):
    """
    Atualiza um pedido com base no ID fornecido.

    Parâmetros:
    - order_id (int): O ID do pedido a ser atualizado.
    - item (Pedido): O objeto Pedido contendo as informações atualizadas do pedido.

    Retorna:
    - dict: O pedido atualizado.

    """
    for order in PEDIDOS:
        if order["id"] == order_id:
            order["item"] = item.item
            order["quantidade"] = item.quantidade
            order["preco_unitario"] = item.preco_unitario
            order["total"] = item.quantidade * item.preco_unitario
            return order
    raise HTTPException(status_code=404, detail=f"Pedido id={order_id} não encontrado")

# DELETE
@app.delete("/orders/{order_id}")
def delete_order(order_id: int):
    """
    Remove um pedido com base no ID fornecido.

    Parâmetros:
    - order_id (int): O ID do pedido a ser removido.

    Retorna:
    - dict: Um dicionário contendo a mensagem de sucesso da remoção do pedido.

    """
    for order in PEDIDOS:
        if order["id"] == order_id:
            PEDIDOS.remove(order)
            return {"mensagem": f"Pedido id={order_id} removido com sucesso"}
    raise HTTPException(status_code=404, detail=f"Pedido id={order_id} não encontrado")

if __name__ == "__main__":
    
    uvicorn.run(app) # Rodando a API. A API estará disponível em http://localhost:8000