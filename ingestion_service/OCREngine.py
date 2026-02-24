import easyocr


class OCREngine:

    def __init__(self):
        self.reader = easyocr.Reader(["en"], gpu=False)
    
    def extract_text(self,file_path):
        return " ".join(self.reader.readtext(file_path, detail=0))