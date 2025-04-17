from models import CreateUser, User, CreateProduct, Product

def get_user_by_id(user_id: int, users: list[User]) -> User | None:
    return next((u for u in users if u.id == user_id), None)

def get_product_by_id(product_id: int, products: list[Product]) -> Product | None:
    return next((p for p in products if p.id == product_id), None)

def create_user(user: CreateUser, users: list[User]) -> User:
    user_id = len(users) + 1
    new_user = User(id=user_id, **user.dict())
    users.append(new_user)
    return new_user

def create_product(product: CreateProduct, products: list[Product]) -> Product:
    product_id = len(products) + 1
    new_product = Product(id=product_id, **product.dict())
    products.append(new_product)
    return new_product

