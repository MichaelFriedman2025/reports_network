from elasticsearch import Elasticsearch
import os

class ElasticsearchClient:

    def __init__(self):
        elastic_uri = os.getenv("ELASTIC_URI","http://localhost:9200")
        self.client = Elasticsearch(elastic_uri)
    
    def create_doc(self):
        self.client.indices()