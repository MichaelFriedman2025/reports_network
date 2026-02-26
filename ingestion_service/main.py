import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from OCREngine import OCREngine
from MetadataExtractor import MetadataExtractor
from KafkaPublisher import KafkaPublisher
from fastapi import FastAPI
import requests
import uvicorn
import os

metadata_extractor = MetadataExtractor()
ocr_engine = OCREngine()
kafka_producer = KafkaPublisher()
app = FastAPI()


@app.get("/start")
def main_flow():

    FOLDER_PATH = "images"
    for filename in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH,filename)
        binary_file = open(file_path,"rb")
        requests.post(url="http://localhost:8080/image",files={"file":binary_file})
        binary_file.close()

        metadata = metadata_extractor.extract_metadata(file_path=file_path)
        metadata["image_id"] = metadata_extractor.generate_image_id()
        metadata["text"] = ocr_engine.extract_text(file_path=file_path)

        kafka_producer.produce_data(metadata)
        

if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000)


