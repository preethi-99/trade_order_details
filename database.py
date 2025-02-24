from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql+asyncpg://postgres:Yougotthis%4099@db:5432/trade_order_details"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL.replace("+asyncpg", ""))
metadata.create_all(engine)
