{
  "settings": {
    "number_of_shards": 1
  },
  "mappings": {
    "properties": {
      "name": { "type": "text" },
      "description": { "type": "text" },
      "tags": { "type": "keyword" },
      "price": { "type": "float" }
    }
  }
}
