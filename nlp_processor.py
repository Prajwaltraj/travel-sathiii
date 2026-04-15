import spacy
from textblob import TextBlob

class NLPManager:
    def __init__(self):
        # Make sure to run: python -m spacy download en_core_web_sm
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            self.nlp = None

    def analyze(self, text):
        results = {"entities": [], "sentiment": "neutral"}
        
        if self.nlp:
            doc = self.nlp(text)
            results["entities"] = [(ent.text, ent.label_) for ent in doc.ents]
        
        # Simple sentiment logic
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.1: results["sentiment"] = "positive"
        elif polarity < -0.1: results["sentiment"] = "negative"
        
        return results