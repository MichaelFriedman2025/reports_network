import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter


class TextAnalyzer:

    def __init__(self):
        nltk.download("vader_lexicon", quiet=True)

    def analyze_text(self, text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        result = score["compound"]
        if result >= 0.5:
            return "positive"
        elif result >= (-0.5):
            return "natoral"
        else:
            return "negative"

    def count_weapons_in_text(self, text):
        with open("weapon_list.txt", "r", encoding="utf-8-sig") as f:
            weapons = f.read().splitlines()
        list_of_all_weapons = [weapon for weapon in weapons if weapon in text]
        return list_of_all_weapons

    def top_10_words_common(self, text: str):
        top_words = Counter(text.split()).most_common(10)
        return [word[0] for word in top_words]
    