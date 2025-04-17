import pytest
pytestmark = pytest.mark.asyncio


from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Online Store API!"}

@pytest.mark.asyncio
async def test_create_and_get_user():
    user_data = {"name": "Alice", "email": "alice@example.com"}
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        create_res = await ac.post("/users", json=user_data)
        assert create_res.status_code == 200
        created_user = create_res.json()
        assert created_user["name"] == user_data["name"]

        get_res = await ac.get(f"/users/{created_user['id']}")
        assert get_res.status_code == 200
        assert get_res.json() == created_user

@pytest.mark.asyncio
async def test_create_and_get_product():
    product_data = {
        "name": "Test Product",
        "price": 9.99,
        "description": "Just a test item"
    }

    async with AsyncClient(app=app, base_url="http://test") as ac:
        create_res = await ac.post("/products", json=product_data)
        assert create_res.status_code == 200
        created_product = create_res.json()
        assert created_product["name"] == product_data["name"]

        get_res = await ac.get(f"/products/{created_product['id']}")
        assert get_res.status_code == 200
        assert get_res.json() == created_product

@pytest.mark.asyncio
async def test_prevent_duplicate_emails():
    user_data = {"name": "Bob", "email": "bob@example.com"}
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # First user creation should succeed
        res1 = await ac.post("/users", json=user_data)
        assert res1.status_code == 200

        # Second creation with same email should fail
        res2 = await ac.post("/users", json=user_data)
        assert res2.status_code == 400
        assert res2.json()["detail"] == "Email already registered"


@pytest.mark.asyncio
async def test_update_user_name():
    user_data = {"name": "Charlie", "email": "charlie@example.com"}
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create a user
        create_res = await ac.post("/users", json=user_data)
        assert create_res.status_code == 200
        user = create_res.json()

        # Update the user's name
        updated_data = {"name": "Charlie Updated", "email": user["email"]}
        update_res = await ac.put(f"/users/{user['id']}", json=updated_data)
        assert update_res.status_code == 200
        assert update_res.json()["name"] == "Charlie Updated"


@pytest.mark.asyncio
async def test_get_products_with_price_filter():
    products = [
        {"name": "Cheap Pen", "price": 2.99},
        {"name": "Mid-range Notebook", "price": 9.99},
        {"name": "Expensive Monitor", "price": 199.99},
    ]

    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Add products
        for product in products:
            await ac.post("/products", json=product)

        # Filter products between 5 and 100
        res = await ac.get("/products", params={"min": 5, "max": 100})
        assert res.status_code == 200
        filtered = res.json()

        names = [p["name"] for p in filtered]
        assert "Mid-range Notebook" in names
        assert "Cheap Pen" not in names
        assert "Expensive Monitor" not in names


