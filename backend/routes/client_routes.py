from fastapi import APIRouter, HTTPException, Response
import uuid
from config.db import engine
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from models.client_model import clients
from typing import List
from schemas.client_schema import ClientSchema
import json

client_routes = APIRouter()

@client_routes.post("/clients/")
def create_client(client: ClientSchema):
    with engine.connect() as conn:
        new_client = client.model_dump()
        new_client['id'] = str(uuid.uuid4())
        conn.execute(clients.insert().values(new_client))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

@client_routes.get("/clients/")
def get_clients():
    with engine.connect() as conn:
        result = conn.execute(clients.select()).fetchall()
        conn.commit()
        return {
            "success": True,
            "data": json.dumps(result, default=str)
        }

@client_routes.get("/clients/{client_id}")
def get_client(client_id: str):
    with engine.connect() as conn:
        result = conn.execute(clients.select().where(clients.c.id == client_id)).first()
        conn.commit()
        return {
            "success": True,
            "data": json.dumps(result, default=str)
        }

@client_routes.put("/clients/{client_id}")
def update_client(client_update: ClientSchema, client_id: str):
    with engine.connect() as conn:
        conn.execute(clients.update().values(name=client_update.name, password=client_update.password, role=client_update.role, ip=client_update.ip).where(clients.c.id == client_id))
        conn.commit()

        result = conn.execute(clients.select().where(clients.c.id == client_id)).first()

        # return {
        #     "success": True,
        #     "data": json.dumps(result, default=str)
        # }
        return Response(status_code=HTTP_204_NO_CONTENT)
    
@client_routes.delete("/clients/{client_id}", status_code=HTTP_204_NO_CONTENT)
def delete_client(client_id: str):
    with engine.connect() as conn:
        conn.execute(clients.delete().where(clients.c.id == client_id))
        conn.commit()

        return Response(status_code=HTTP_204_NO_CONTENT)