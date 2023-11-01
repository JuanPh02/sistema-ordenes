from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

clients = Table("clients", meta_data,
              Column("id", String(60), primary_key=True),
              Column("name", String(200), nullable=False),
              Column("user", String(200), nullable=False),
              Column("password", String(200), nullable=False),
              Column("role", String(20), nullable=False),
              Column("ip", String(15), nullable=False))