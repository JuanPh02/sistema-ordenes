from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

orders = Table("orders", meta_data,
              Column("id", String(60), primary_key=True),
              Column("product", String(60), nullable=False),
              Column("quantity", Integer, nullable=False),
              Column("createDate", String(100), nullable=False),
              Column("status", String(20), nullable=False),
              Column("user", String(200), nullable=False))