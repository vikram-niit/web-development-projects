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





\# Start ec2 instance

Edit inbound rules and allow ssh traffic on port 22 from all/custom ips

\# Installing mongodb on ec2-instance

 curl -LO https://downloads.mongodb.com/linux/mongodb-linux-x86\_64-6.0.7.tgz

\# Install docker

sudo dnf update -y

sudo dnf install -y docker

sudo systemctl start docker

sudo systemctl status docker



oneliner

sudo dnf update -y \&\& sudo dnf install -y docker \&\& sudo systemctl start docker \&\& sudo systemctl enable docker \&\& echo "Docker installed and started"





 cat <<EOF | sudo tee /etc/yum.repos.d/mongodb-org.repo

\[mongodb-org-7.0]

name=MongoDB Repository

baseurl=https://repo.mongodb.org/yum/amazon/2023/mongodb-org/7.0/x86\_64/

gpgcheck=1

enabled=1

gpgkey=https://www.mongodb.org/static/pgp/server-7.0.asc

EOF

\[mongodb-org-7.0]

name=MongoDB Repository

baseurl=https://repo.mongodb.org/yum/amazon/2023/mongodb-org/7.0/x86\_64/

gpgcheck=1

enabled=1

gpgkey=https://www.mongodb.org/static/pgp/server-7.0.asc



sudo dnf install -y mongodb-org



\# Connecting to aws document db

 mongosh 'mongodb://test:Documentdb2026!@test-doc-db-cluster-2026-01-26-368673729078.us-ea

st-1.docdb-elastic.amazonaws.com:27017' --tls --authenticationMechanism SCRAM-SHA-1 --retryWrites=false



if DOCUMENTDB\_URI is None export the environment variables in the cmd line

&nbsp;export DOCUMENTDB\_URI='mongodb://test:Documentdb2026%21@test-doc-db-cluster-2026

-01-26-368673729078.us-east-1.docdb-elastic.amazonaws.com:27017?tls=true\&retryWrites=false\&authMechanism=SCRAM-SHA-1'

export OPENSEARCH\_HOST=https://search-testdomain-rvplcvqbevpp6auo3s5vjqsegy.us-east-1.es.amazonaws.com:443

export OS\_USER=opensearchuser

export OS\_PASSWORD=Opensearch2026!



curl -i -X POST http://ec2-54-167-51-235.compute-1.amazonaws.com:8000/products/ -H "Conte

nt-Type: application/json" -d '{

&nbsp; "id": "p001",

&nbsp; "name": "Wireless Mouse",

&nbsp; "description": "Ergonomic wireless mouse with 2-year battery",

&nbsp; "tags": \["electronics", "accessories", "mouse"],

&nbsp; "price": 29.99

}'



