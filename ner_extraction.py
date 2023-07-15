import spacy
import matplotlib.pyplot as plt
from collections import defaultdict

# Load spaCy English model for NER
nlp = spacy.load('en_core_web_sm')

# Function to perform named entity recognition (NER) on text
def ner_extraction(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Example usage
text = '''
The recent advancements in artificial intelligence have significantly impacted various industries. 
AI-powered technologies are being used in healthcare for diagnosis and treatment planning. 
In the automotive industry, self-driving cars are becoming a reality. 
AI algorithms have also improved the accuracy of financial market predictions. 
Moreover, natural language processing techniques enable chatbots to provide efficient customer support. 
Overall, AI has transformed many sectors and continues to revolutionize the way we work and live.
'''

# Perform NER extraction
ner_entities = ner_extraction(text)

for entity in ner_entities:
    print("Entity:", entity[0])
    print("Type:", entity[1])
    print("----")

# Calculate occurrence of entity types and their frequency count
entity_counts = defaultdict(int)
for entity in ner_entities:
    entity_counts[entity[1]] += 1

# Plot bar graph for entity type frequency count
entity_types = list(entity_counts.keys())
frequency_counts = list(entity_counts.values())

plt.figure(figsize=(10, 5))
plt.bar(entity_types, frequency_counts)
plt.xlabel('Entity Type')
plt.ylabel('Frequency Count')
plt.title('NER Entity Type Frequency Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()