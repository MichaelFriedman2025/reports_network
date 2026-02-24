import cv2
import uuid

class MetadataExtractor:

    @staticmethod
    def extract_metadata(file_path):
        image = cv2.imread(file_path)
        height, width, channels = image.shape
        image_format = file_path.split(".")[-1].lower()
        return {
            "image_format": image_format,
            "width": width,
            "height": height,
            "channels": channels
        }

    @staticmethod
    def generate_image_id():
        return str(uuid.uuid4())