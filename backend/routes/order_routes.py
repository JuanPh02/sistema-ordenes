from fastapi import APIRouter, HTTPException, Response
import uuid
from config.db import engine
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from models.order_model import orders
from typing import List
from schemas.order_schema import OrderSchema
import json

order_routes = APIRouter()

@order_routes.post("/orders/")
def create_order(order: OrderSchema):
    with engine.connect() as conn:
        new_order = order.model_dump()
        new_order.id = str(uuid.uuid4())
        conn.execute(orders.insert().values(new_order))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

@order_routes.get("/orders/")
def get_orders():
    with engine.connect() as conn:
        result = conn.execute(orders.select()).fetchall()
        conn.commit()
        return {
            "success": True,
            "data": json.dumps(result, default=str)
        }

@order_routes.get("/orders/{order_id}")
def get_order(order_id: str):
    with engine.connect() as conn:
        result = conn.execute(orders.select().where(orders.c.id == order_id)).first()
        conn.commit()
        return {
            "success": True,
            "data": json.dumps(result, default=str)
        }

@order_routes.put("/orders/{order_id}")
def update_order(order_update: OrderSchema, order_id: str):
    with engine.connect() as conn:
        conn.execute(orders.update().values(quantity=order_update.quantity, status=order_update.status).where(orders.c.id == order_id))
        conn.commit()

        result = conn.execute(orders.select().where(orders.c.id == order_id)).first()

        # return {
        #     "success": True,
        #     "data": json.dumps(result, default=str)
        # }
        return Response(status_code=HTTP_204_NO_CONTENT)
    
@order_routes.delete("/orders/{order_id}", status_code=HTTP_204_NO_CONTENT)
def delete_order(order_id: str):
    with engine.connect() as conn:
        conn.execute(orders.delete().where(orders.c.id == order_id))
        conn.commit()

        return Response(status_code=HTTP_204_NO_CONTENT)