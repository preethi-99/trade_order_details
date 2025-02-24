from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from database import database
from models import orders
from schemas import Order, OrderCreate
from typing import List

app = FastAPI()

# Store active WebSocket connections
clients = []

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/orders/", response_model=Order)
async def create_order(order: OrderCreate):
    query = orders.insert().values(
        symbol=order.symbol,
        price=order.price,
        quantity=order.quantity,
        order_type=order.order_type,
        status="received"
    )
    order_id = await database.execute(query)
    created_order = {**order.dict(), "id": order_id, "status": "received"}

    # Notify all connected WebSocket clients
    for client in clients:
        await client.send_json(created_order)

    return created_order

@app.get("/orders/", response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)

@app.websocket("/ws/orders")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        clients.remove(websocket)

@app.get("/")
async def root():
    return {"message": "Welcome to the Trade Orders API"}
