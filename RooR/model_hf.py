# model_hf.py
from transformers import pipeline

class AIModelHF:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        self.model = pipeline("sentiment-analysis", model=model_name)

    def analyze(self, data):
        truncated_data = data[:512]
        result = self.model(truncated_data)[0]
        return f"AI Model (Hugging Face): {result['label']} (score: {result['score']:.4f})"
