from fastapi import APIRouter
from app.database.opensearch import client

router = APIRouter(prefix="/search", tags=["search"])

@router.get("/")
def search_products(q: str):
    query = {
        "query": {
            "multi_match": {
                "query": q,
                "fields": ["name", "description", "tags"]
            }
        }
    }
    return client.search(index="products", body=query)
