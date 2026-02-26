from ElasticsearchClient import ElasticsearchClient
from KafkaConsumer import KafkaConsumer

consumer = KafkaConsumer()
es = ElasticsearchClient()


while True:
    try:
        msg = consumer.get_data_from_producer()
        if not msg:
            continue
        else:
            es.insert_to_elastic(msg)
            
    except Exception as error:
        print("❌ERROR:",error)