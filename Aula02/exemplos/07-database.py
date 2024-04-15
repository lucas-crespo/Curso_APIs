# Descrição: Código de exemplo para criar uma API com FastAPI

from typing import Optional
from fastapi import FastAPI, HTTPException, Depends
import uvicorn
from sqlmodel import SQLModel, Field, create_engine, Session

app = FastAPI(title="API de Pedidos")

def get_session():
    with Session(engine) as session:
            yield session

class Pedidos(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=True, primary_key=True)
    item: str
    quantidade: int
    preco_unitario: float
    
    @property
    def total(self):
        return self.quantidade * self.preco_unitario

engine = create_engine('sqlite:///atenabackend.db', echo=True)

def create_tables():
    SQLModel.metadata.create_all(bind=engine)

@app.get("/", status_code=201)
async def root():
    create_tables()
    return {"message": "Table created"}

@app.post("/orders/", status_code=200)
def create_order(item: Pedidos, session: Session = Depends(get_session)):
    """
    Cria um novo pedido com o item fornecido.

    Args:
    - item (Pedido): O item a ser adicionado ao pedido.
    - session (Session): A sessão do banco de dados.

    Returns:
    - dict: O pedido criado.

    """
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@app.get("/orders/{order_id}", status_code=200)
def get_order(order_id: int, session: Session = Depends(get_session)):
    """
    Retorna os detalhes de um pedido específico.

    Args:
    - order_id (int): O ID do pedido.
    - session (Session): A sessão do banco de dados.

    Returns:
    - dict: Os detalhes do pedido.

    """
    order = session.get(Pedidos, order_id)
    if not order:
        raise HTTPException(status_code=404, detail=f"Pedido id={order_id} não encontrado")
    return order

@app.put("/orders/{order_id}", status_code=200)
def update_order(order_id: int, item: Pedidos, session: Session = Depends(get_session)):
    """
    Atualiza um pedido existente com o item fornecido.
    Args:
    - order_id (int): O ID do pedido a ser atualizado.
    - item (Pedido): O item atualizado do pedido.
    - session (Session): A sessão do banco de dados.
    Returns:
    - dict: O pedido atualizado.
    """
    order = session.get(Pedidos, order_id)
    if not order:
        raise HTTPException(status_code=404, detail=f"Pedido id={order_id} não encontrado")
    order.item = item.item
    order.quantidade = item.quantidade
    order.preco_unitario = item.preco_unitario
    session.commit()
    session.refresh(order)
    return order

@app.delete("/orders/{order_id}", status_code=200)
def delete_order(order_id: int, session: Session = Depends(get_session)):
    """
    Deleta um pedido existente.
    Args:
    - order_id (int): O ID do pedido a ser deletado.
    - session (Session): A sessão do banco de dados.
    """
    order = session.get(Pedidos, order_id)
    if not order:
        raise HTTPException(status_code=404, detail=f"Pedido id={order_id} não encontrado")
    session.delete(order)
    session.commit()
    return {"mensagem": f"Pedido id={order_id} removido com sucesso"}

if __name__ == "__main__":
    
    uvicorn.run(app) # Rodando a API. A API estará disponível em http://localhost:8000