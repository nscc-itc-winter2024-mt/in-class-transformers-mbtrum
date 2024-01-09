from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis", "distilbert-base-uncased-finetuned-sst-2-english")
#sentiment_pipeline = pipeline("sentiment-analysis", model="Distilbert-base-uncased-emotion")

feeling = ["Eek"]

result = sentiment_model(feeling)

print(result)