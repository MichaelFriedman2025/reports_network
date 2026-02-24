from KafkaConsumer import KafkaConsumer
from KafkaPublisher import KafkaPublisher
from TextAnalyzer import TextAnalyzer
import json 

consumer = KafkaConsumer()
producer = KafkaPublisher()
text_analyze = TextAnalyzer()

while True:
    try:
        msg = consumer.get_data_from_producer()
        if not msg:
            continue
        else:
            text = msg["text"]
            res_of_text_analyze = text_analyze.analyze_text(text=text)
            list_of_weapons = text_analyze.count_weapons_in_text()
            top_common_words = text_analyze.top_10_words_common(text)
            data = {"image_id":msg["image_id"],"text_analyze":res_of_text_analyze,"list_of_weapons":list_of_weapons,"top_common_words":top_common_words}
            producer.produce_data(data=json.dumps(data))
    except Exception as error:
        print("❌ERROR:",error)