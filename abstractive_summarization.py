from transformers import pipeline

def abstractive_summarization(text):
    summarization_pipeline = pipeline("summarization")
    summary = summarization_pipeline(text, max_length=100, min_length=30, do_sample=True)[0]['summary_text']
    return summary

# # Example usage
text = '''
The recent advancements in artificial intelligence have significantly impacted various industries. 
AI-powered technologies are being used in healthcare for diagnosis and treatment planning. 
In the automotive industry, self-driving cars are becoming a reality. 
AI algorithms have also improved the accuracy of financial market predictions. 
Moreover, natural language processing techniques enable chatbots to provide efficient customer support. 
Overall, AI has transformed many sectors and continues to revolutionize the way we work and live.
'''

summary = abstractive_summarization(text)
print(summary)