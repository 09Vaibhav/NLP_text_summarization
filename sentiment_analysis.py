from transformers import pipeline

def sentiment_analysis(text):
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)
    return result[0]['label'], result[0]['score']

# Example usage
text = "I really enjoyed the movie, it was fantastic!"

sentiment_label, sentiment_score = sentiment_analysis(text)
print("Sentiment Label:", sentiment_label)
print("Sentiment Score:", sentiment_score)
