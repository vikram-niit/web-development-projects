from app.database.opensearch import client

def index_product(product):
    client.index(
        index="products",
        id=product["id"],
        body={
            "name": product["name"],
            "description": product["description"],
            "tags": product["tags"],
            "price": product["price"]
        }
    )
