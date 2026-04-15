import spacy
from textblob import TextBlob

class NLPManager:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            self.nlp = None

    def analyze(self, text):
        sentiment = "neutral"
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.1: sentiment = "positive"
        elif polarity < -0.1: sentiment = "negative"
        
        entities = []
        if self.nlp:
            doc = self.nlp(text)
            entities = [(ent.text, ent.label_) for ent in doc.ents]
            
        return {"sentiment": sentiment, "entities": entities}