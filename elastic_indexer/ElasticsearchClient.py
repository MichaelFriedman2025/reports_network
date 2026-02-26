from elasticsearch import Elasticsearch
import os


class ElasticsearchClient:

    def __init__(self):
        elastic_uri = os.getenv("ELASTIC_URI", "http://localhost:9200")
        self.client = Elasticsearch(elastic_uri)
        self.index = "images"
        self.create_schema()

    def create_schema(self):
        if not self.client.indices.exists(index=self.index):
            mapping = {
                "mappings": {
                    "properties": {
                        "image_id": {"type": "keyword"},
                        "text": {"type": "text"},
                        "image_format": {"type": "keyword"},
                        "width": {"type": "integer"},
                        "height": {"type": "integer"},
                        "channels": {"type": "integer"},
                        "clean_text": {"type": "text"},
                        "text_analyze": {"type": "keyword"},
                        "list_of_weapons": {"type": "keyword"},
                        "top_common_words": {"type": "keyword"},
                    }
                }
            }
            self.client.indices.create(index=self.index, body=mapping)

    def insert_to_elastic(self, metadat):
        self.client.update(
            index=self.index,
            id=metadat["image_id"],
            body={"doc": metadat, "doc_as_upsert": True},
        )
