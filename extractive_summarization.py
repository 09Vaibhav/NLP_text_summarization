# import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def extractive_summarization(text, num_sentences=3):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize the sentences into words and remove stopwords
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Calculate the frequency of each word
    word_frequencies = FreqDist(words)
    
    # Assign scores to sentences based on word frequencies
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if i not in sentence_scores:
                    sentence_scores[i] = word_frequencies[word]
                else:
                    sentence_scores[i] += word_frequencies[word]
    
    # Sort the sentences based on their scores
    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    
    # Select the top n sentences for the summary
    summary_sentences = ranked_sentences[:num_sentences]
    
    # Sort the summary sentences in the original order
    summary_sentences = sorted(summary_sentences)
    
    # Construct the summary
    summary = ' '.join([sentences[i] for i in summary_sentences])
    return summary

# Example usage
# text = '''
# The recent advancements in artificial intelligence have significantly impacted various industries. 
# AI-powered technologies are being used in healthcare for diagnosis and treatment planning. 
# In the automotive industry, self-driving cars are becoming a reality. 
# AI algorithms have also improved the accuracy of financial market predictions. 
# Moreover, natural language processing techniques enable chatbots to provide efficient customer support. 
# Overall, AI has transformed many sectors and continues to revolutionize the way we work and live.
# '''

# summary = extractive_summarization(text)
# print(summary)
