\# Search \& Indexing Application



This project demonstrates a simple search and indexing system using

AWS DocumentDB and Amazon OpenSearch.



\## Features

\- Store documents in DocumentDB

\- Index searchable fields in OpenSearch

\- Full-text search with filters

\- REST API using FastAPI



\## Tech Stack

\- Python (FastAPI)

\- Amazon DocumentDB

\- Amazon OpenSearch

\- Docker



\## Run Locally

1\. Set environment variables

2\. Build Docker image

3\. Start application

4\. Create OpenSearch index



\## Endpoints

\- POST /products

\- GET /search?q=keyword



Deployment Steps (AWS)

Step 1: AWS Resources



DocumentDB



Create cluster



Enable TLS



Security group allows app access



OpenSearch



Create domain



Enable fine-grained access



Public or VPC access



Compute



EC2 (simple)



or ECS Fargate



or Lambda (advanced)



Step 2: Environment Variables

DOCUMENTDB\_URI=mongodb://user:pass@host:27017/?tls=true

OPENSEARCH\_HOST=search-domain.amazonaws.com

OS\_USER=admin

OS\_PASSWORD=\*\*\*\*\*



Step 3: Docker Build \& Run

docker build -t search-app .

docker run -p 8000:8000 --env-file .env search-app



Step 4: Initialize OpenSearch Index

python scripts/create\_index.py



