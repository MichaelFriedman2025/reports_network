from confluent_kafka import Consumer
import os
import json


class KafkaConsumer:
    def __init__(self):

        kafka_uri = os.getenv("KAFKA_URI", "localhost:9092")
        consumer_config = {
            "bootstrap.servers": kafka_uri,
            "group.id": "clean_service",
            "auto.offset.reset": "earliest",
        }

        self.consumer = Consumer(consumer_config)
        self.consumer.subscribe(["Raw"])

    def get_data_from_producer(self):
        msg = self.consumer.poll()
        if msg is None:
            return None
        elif msg.error():
            print("❌ Error:", msg.error())
            return None
        else:
            value = msg.value().decode("utf-8")
            return json.loads(value)
        