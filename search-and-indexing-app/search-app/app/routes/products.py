from fastapi import APIRouter
from app.models.product import Product
from app.database.documentdb import products_collection
from app.services.indexer import index_product

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/")
def create_product(product: Product):
    products_collection.insert_one(product.dict())
    index_product(product.dict())
    return {"message": "Product created"}
