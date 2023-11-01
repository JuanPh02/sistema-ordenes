from fastapi import APIRouter, HTTPException, Response
import uuid
from config.db import engine
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from models.product_model import products
from typing import List
from schemas.product_schema import ProductSchema
import json

product_routes = APIRouter()

@product_routes.post("/products/")
def create_product(product: ProductSchema):
    with engine.connect() as conn:
        new_product = product.model_dump()
        new_product['id'] = str(uuid.uuid4())
        conn.execute(products.insert().values(new_product))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

@product_routes.get("/products/")
def get_products():
    with engine.connect() as conn:
        result = conn.execute(products.select()).fetchall()
        conn.commit()
        return {
            "success": True,
            "data": json.dumps(result, default=str)
        }

@product_routes.get("/products/{product_id}")
def get_product(product_id: str):
    with engine.connect() as conn:
        result = conn.execute(products.select().where(products.c.id == product_id)).first()
        conn.commit()
        return {
            "success": True,
            "data": json.dumps(result, default=str)
        }

@product_routes.put("/products/{product_id}")
def update_product(product_update: ProductSchema, product_id: str):
    with engine.connect() as conn:
        conn.execute(products.update().values(name=product_update.name, description=product_update.description, price=product_update.price, stock=product_update.stock).where(products.c.id == product_id))
        conn.commit()

        result = conn.execute(products.select().where(products.c.id == product_id)).first()

        # return {
        #     "success": True,
        #     "data": json.dumps(result, default=str)
        # }
        return Response(status_code=HTTP_204_NO_CONTENT)
    
@product_routes.delete("/products/{product_id}", status_code=HTTP_204_NO_CONTENT)
def delete_product(product_id: str):
    with engine.connect() as conn:
        conn.execute(products.delete().where(products.c.id == product_id))
        conn.commit()

        return Response(status_code=HTTP_204_NO_CONTENT)