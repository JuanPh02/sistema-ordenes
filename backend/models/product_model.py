from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

products = Table("products", meta_data,
              Column("id", String(60), primary_key=True),
              Column("name", String(200), nullable=False),
              Column("description", String(200), nullable=False),
              Column("price", Integer, nullable=False),
              Column("stock", Integer, nullable=False))