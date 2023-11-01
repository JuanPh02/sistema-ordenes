from routes.order_routes import order_routes
from routes.client_routes import client_routes
from routes.product_routes import product_routes
from config.db import engine
from facade import Facade
from models.client_model import clients
import json
from fastapi import FastAPI

app = FastAPI()
facade = Facade()

# @app.get("/")
# def index():
#   return {'message': 'Hello World!'}

# @app.get("/clients/{user}")
# def getClient(user):
#   return {"data": user}

app.include_router(order_routes, prefix="/api")
app.include_router(client_routes, prefix="/api")
app.include_router(product_routes, prefix="/api")

@app.post("/send_request")
async def send_request(data: dict):
  
  # with engine.connect() as conn:
  #   result = conn.execute(c.select().where(clients.c.id == data.client.id)).first()
  #   conn.commit()
  #   client = json.dumps(result, default=str)
  print(data['client']['ip_address']) 
  result = facade.send_request(data)
  return result

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)