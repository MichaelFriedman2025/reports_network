from KafkaConsumer import KafkaConsumer
from KafkaPublisher import KafkaPublisher
from TextCleaner import TextCleaner 
import json 

consumer = KafkaConsumer()
producer = KafkaPublisher()
text_cleaner = TextCleaner()

while True:
    try:
        msg = consumer.get_data_from_producer()
        if not msg:
            continue
        else:
            text = msg["text"]
            removing_stop_words = " ".join(text_cleaner.remove_stop_words(text))
            data = json.dumps({"image_id":msg["image_id"],"clean_text":removing_stop_words})
            producer.produce_data(data=data)
    except Exception as error:
        print("❌ERROR:",error)