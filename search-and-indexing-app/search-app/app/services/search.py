from opensearchpy import OpenSearch
import os

client = OpenSearch(
    hosts=[{"host": os.getenv("OPENSEARCH_HOST"), "port": 443}],
    http_auth=(os.getenv("OS_USER"), os.getenv("OS_PASSWORD")),
    use_ssl=True,
    verify_certs=True
)
