from pydantic import BaseModel

class OrderCreate(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str

class Order(OrderCreate):
    id: int
    status: str

    class Config:
        from_attributes = True
