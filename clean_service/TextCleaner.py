import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



class TextCleaner:

    def __init__(self):
        nltk.download('punkt_tab',quiet=True)
        nltk.download('stopwords',quiet=True)
        nltk.download('punkt',quiet=True)
        self.stop_words = set(stopwords.words('english'))

    
    def remove_stop_words(self,text:str):
        tokens = word_tokenize(text.lower())
        filtered_tokens = [word for word in tokens if word.isalnum() and word not in self.stop_words]
        return filtered_tokens