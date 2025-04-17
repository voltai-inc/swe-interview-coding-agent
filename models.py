from pydantic import BaseModel
from typing import Optional

class CreateUser(BaseModel):
    name: str
    email: str

class User(CreateUser):
    id: int

class CreateProduct(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

class Product(CreateProduct):
    id: int

