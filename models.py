from sqlalchemy import Table, Column, Integer, String, Float
from database import metadata

orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("symbol", String, index=True),
    Column("price", Float),
    Column("quantity", Integer),
    Column("order_type", String),
    Column("status", String, default="pending"),
)
