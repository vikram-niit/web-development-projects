from fastapi import FastAPI
from app.routes import products, search

app = FastAPI(title="Search & Indexing API")

app.include_router(products.router)
app.include_router(search.router)
