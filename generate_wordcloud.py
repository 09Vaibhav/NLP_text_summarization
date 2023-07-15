import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import spacy
import matplotlib.pyplot as plt

# Download required resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Function to generate a word cloud from text
def generate_wordcloud(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Filter out stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]

    # Create word frequency dictionary
    word_freq = nltk.FreqDist(filtered_tokens)

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()



# Example usage
text = '''
The recent advancements in artificial intelligence have significantly impacted various industries. 
AI-powered technologies are being used in healthcare for diagnosis and treatment planning. 
In the automotive industry, self-driving cars are becoming a reality. 
AI algorithms have also improved the accuracy of financial market predictions. 
Moreover, natural language processing techniques enable chatbots to provide efficient customer support. 
Overall, AI has transformed many sectors and continues to revolutionize the way we work and live.
'''

# Generate word cloud
generate_wordcloud(text)


