import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Gerekli nltk verilerini indirme (sadece ilk sefer çalıştırın)
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_comment(comment):
    # Küçük harfe çevirme
    comment = comment.lower()
    # Özel karakterleri kaldırma
    comment = re.sub(r'[^\w\s]', '', comment)
    # Tokenize etme
    tokens = word_tokenize(comment)
    # Stop kelimeleri kaldırma
    tokens = [word for word in tokens if word not in stopwords.words('turkish')]
    return tokens