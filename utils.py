import re
import nltk
from nltk.corpus import stopwords

# Tell nltk where to look for manually added data
nltk.data.path.append("C:/Users/admin/nltk_data")  # Forward slashes are perfect

# No need to call nltk.download('stopwords') here
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    tokens = text.lower().split()
    tokens = [t for t in tokens if t not in STOPWORDS]
    return ' '.join(tokens)

def extract_keywords(text, top_k=10):
    from sklearn.feature_extraction.text import CountVectorizer
    vec = CountVectorizer(stop_words='english', max_features=top_k)
    vec.fit([text])
    return vec.get_feature_names_out()
