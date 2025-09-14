# model.py

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

class AIModel:
    def __init__(self):
        self.model = LogisticRegression()
        self.vectorizer = TfidfVectorizer()
        self.trained = False

    def train(self, data, labels):
        self.vectorizer.fit(data)
        vectors = self.vectorizer.transform(data)
        self.model.fit(vectors, labels)
        self.trained = True

    def analyze(self, data):
        if not self.trained:
            return "AI Model: Not trained yet"
        vector = self.vectorizer.transform([data])
        prediction = self.model.predict(vector)[0]
        if prediction == 1:
            return "AI Model: Threat Level - High"
        else:
            return "AI Model: Threat Level - Low"

    def save(self, filename):
        joblib.dump(self, filename)

    def load(self, filename):
        loaded_model = joblib.load(filename)
        self.model = loaded_model.model
        self.vectorizer = loaded_model.vectorizer
        self.trained = True
