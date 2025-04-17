from fastapi import FastAPI, HTTPException
from models import User, Product, CreateUser, CreateProduct
from utils import get_user_by_id, get_product_by_id, create_user, create_product

app = FastAPI()

# In-memory 'database'
users = []
products = []

@app.get("/")
def root():
    return {"message": "Welcome to the Online Store API!"}

@app.post("/users", response_model=User)
def add_user(user: CreateUser):
    new_user = create_user(user, users)
    return new_user

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    user = get_user_by_id(user_id, users)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/products", response_model=Product)
def add_product(product: CreateProduct):
    new_product = create_product(product, products)
    return new_product

@app.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int):
    product = get_product_by_id(product_id, products)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

