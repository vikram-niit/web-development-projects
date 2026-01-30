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



curl -i -X POST http://ec2-54-167-51-235.compute-1.amazonaws.com:8000/products/ -H "Content-Type: application/json" -d '{

&nbsp; "id": "p001",

&nbsp; "name": "Wireless Mouse",

&nbsp; "description": "Ergonomic wireless mouse with 2-year battery",

&nbsp; "tags": \["electronics", "accessories", "mouse"],

&nbsp; "price": 29.99

}'

message: Product created

.

Verify the product in OpenSearch (indexing)

Check index exists

curl -u user:password \\

&nbsp; https://xxx.us-east-1.es.amazonaws.com/products/\_count





Expected output:



{ "count": 1 }



Fetch the document

curl -u user:password \\

&nbsp; https://xxx.us-east-1.es.amazonaws.com/products/\_search





You should see your product in \_source.



✅ If it’s here → indexing pipeline works.



Test search api

curl "http://localhost:8000/products/search?q=laptop"



Make it visible to opensearch dashboards

Add search filters



price range



category



Pagination



from, size



Index mapping



keyword vs text fields



Background reindex job



Health endpoint



/health/docdb



/health/opensearch



Check opensearch authentication

curl -u opensearchuser:Opensearch2026! https://search-testdomain-rvplcvqbevpp6auo3s5vjqsegy.us-east-1.es.amazonaws.com/

&nbsp;curl -u opensearchuser:Opensearch2026! https://search-testdomain-rvplcvqbevpp6auo3s5vjqsegy.us-east-1.es.amazonaws.com/products/\_search?pretty



Following is the output from opensearch

{

&nbsp; "took": 6,

&nbsp; "timed\_out": false,

&nbsp; "\_shards": {

&nbsp;   "total": 5,

&nbsp;   "successful": 5,

&nbsp;   "skipped": 0,

&nbsp;   "failed": 0

&nbsp; },

&nbsp; "hits": {

&nbsp;   "total": {

&nbsp;     "value": 1,

&nbsp;     "relation": "eq"

&nbsp;   },

&nbsp;   "max\_score": 0.13076457,

&nbsp;   "hits": \[

&nbsp;     {

&nbsp;       "\_index": "products",

&nbsp;       "\_id": "p001",

&nbsp;       "\_score": 0.13076457,

&nbsp;       "\_source": {

&nbsp;         "name": "Wireless Mouse",

&nbsp;         "description": "Ergonomic wireless mouse with 2-year battery",

&nbsp;         "tags": \[

&nbsp;           "electronics",

&nbsp;           "accessories",

&nbsp;           "mouse"

&nbsp;         ],

&nbsp;         "price": 29.99

&nbsp;       }

&nbsp;     }

&nbsp;   ]

&nbsp; }

}



This confirms that your OpenSearch indexing is working correctly — you now have 1 document in the products index, and the \_source shows all your fields:

{

&nbsp; "name": "Wireless Mouse",

&nbsp; "description": "Ergonomic wireless mouse with 2-year battery",

&nbsp; "tags": \["electronics", "accessories", "mouse"],

&nbsp; "price": 29.99

}



What this tells us



Document exists → \_count is correct



Index name is correct → products



Fields are searchable → name, description, tags, price 





ssh tunnelling

ssh tunnel (DocumentDB)

ssh -i my-key.pem \\

&nbsp; -L 27017:docdb-cluster.cluster-xyz.us-east-1.docdb.amazonaws.com:27017 \\

&nbsp; ec2-user@<EC2\_PUBLIC\_IP>



What this does:



Local localhost:27017 → forwarded to DocDB inside VPC



Connect using mongosh

mongosh "mongodb://user:password@localhost:27017" \\

&nbsp; --tls \\

&nbsp; --authenticationMechanism SCRAM-SHA-1 \\

&nbsp; --retryWrites=false \\

&nbsp; --tlsCAFile rds-combined-ca-bundle.pem



✅ You’re now securely connected to DocumentDB.



2️⃣ SSH tunnel into AWS OpenSearch

SSH tunnel command (OpenSearch)

ssh -i my-key.pem \\

&nbsp; -L 9200:search-xyz.us-east-1.es.amazonaws.com:443 \\

&nbsp; ec2-user@<EC2\_PUBLIC\_IP>





This maps:



localhost:9200 → OpenSearch HTTPS endpoint



Test OpenSearch locally

curl -u user:password https://localhost:9200/\_cluster/health





or (if IAM-based auth):



curl --aws-sigv4 "aws:amz:us-east-1:es" https://localhost:9200/\_cluster/health



3️⃣ Important SSL note (OpenSearch)



Because OpenSearch uses TLS:



Your browser / curl may warn about cert hostname mismatch



This is expected when tunneling



To bypass during testing:



curl -k -u user:password https://localhost:9200





⚠️ Use -k only for local testing.



4️⃣ Can you tunnel BOTH at once?



✅ Yes — just use multiple -L options:



ssh -i my-key.pem \\

&nbsp; -L 27017:docdb-cluster.cluster-xyz.us-east-1.docdb.amazonaws.com:27017 \\

&nbsp; -L 9200:search-xyz.us-east-1.es.amazonaws.com:443 \\

&nbsp; ec2-user@<EC2\_PUBLIC\_IP>



ssh -vvv -i ~/.ssh/aws/testkeypair20260129.pem \\

&nbsp; -f \\

&nbsp; -N \\

&nbsp; -L 27017:test-doc-db-cluster-2026-01-26-368673729078.us-east-1.docdb-elastic.amazonaws.com:27017 \\

&nbsp; -L 9200:search-testdomain-rvplcvqbevpp6auo3s5vjqsegy.us-east-1.es.amazonaws.com:443 \\

&nbsp; ec2-user@54.167.51.235

&nbsp;

Update your package index

sudo apt update

sudo apt install -y wget gnupg



2️⃣ Add MongoDB’s official GPG key

wget -qO - https://www.mongodb.org/static/pgp/server-7.0.asc | \\

sudo gpg --dearmor -o /usr/share/keyrings/mongodb-server-7.0.gpg



3️⃣ Add the MongoDB repository



Replace jammy if you’re on a different Ubuntu version:



jammy → 22.04



focal → 20.04



echo "deb \[ signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] \\

https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | \\

sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list



4️⃣ Install mongosh

sudo apt update

sudo apt install -y mongodb-mongosh



5️⃣ Verify installation

mongosh --version



&nbsp;mongosh "mongodb://test:Documentdb2026%21@localhost:27017"   --tls   --authenticationMechanism SCRAM-SHA-1   --retryWrites=false --tlsAllowInvalidHostnames



Opensearch

&nbsp;curl -k -u opensearchuser:Opensearch2026! https://localhost:9200/\_cluster/health



{"cluster\_name":"368673729078:testdomain","status":"green","timed\_out":false,"number\_of\_nodes":6,"number\_of\_data\_nodes":3,"discovered\_master":true,"discovered\_cluster\_manager":true,"active\_primary\_shards":31,"active\_shards":93,"relocating\_shards":0,"initializing\_shards":0,"unassigned\_shards":0,"delayed\_unassigned\_shards":0,"number\_of\_pending\_tasks":0,"number\_of\_in\_flight\_fetch":0,"task\_max\_waiting\_in\_queue\_millis":0,"active\_shards\_percent\_as\_number":100.0}



curl -k -u opensearchuser:Opensearch2026! https://localhost:9200/products/\_count

{"count":1,"\_shards":{"total":5,"successful":5,"skipped":0,"failed":0}}



You should see a version number 🎉



Run docker image locally

sudo docker run -d -p 8000:8000 --name search-app-container --env-file .env search-app

curl -i -X POST http://localhost:8000/products/ -H "Content-Type: application/json" -d '{

  "id": "p001",

  "name": "Wireless Mouse",

  "description": "Ergonomic wireless mouse with 2-year battery",

  "tags": \["electronics", "accessories", "mouse"],

  "price": 29.99

}'



Running docker image locally might cause errors. You might need to change few settings similar to the cmd equivalents such as adding --tlsAllowInvalidHostnames through pymongo and same when creating opensearch client programmatically



File "/usr/local/lib/python3.11/site-packages/pymongo/synchronous/topology.py", line 298, in select\_servers

&nbsp;   server\_descriptions = self.\_select\_servers\_loop(

&nbsp;                         ^^^^^^^^^^^^^^^^^^^^^^^^^^

&nbsp; File "/usr/local/lib/python3.11/site-packages/pymongo/synchronous/topology.py", line 359, in \_select\_servers\_loop

&nbsp;   raise ServerSelectionTimeoutError(

pymongo.errors.ServerSelectionTimeoutError:



