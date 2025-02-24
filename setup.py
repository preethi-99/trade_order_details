# setup_db.py
from database import engine, metadata
import models

metadata.create_all(engine)
