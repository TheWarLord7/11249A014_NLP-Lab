import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter
import string

with open('a.txt') as f: x = f.read().lower()
sent = sent_tokenize(x)[0]

tokens = [word for word in word_tokenize(sent) if word not in string.punctuation]
filtered_words = (lambda tokens, stop_words=set(stopwords.words('english')) : [word for word in tokens if word not in stop_words])(tokens)

ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in filtered_words]

freq = Counter(filtered_words)

print(tokens)
print(filtered_words)
print(stemmed_words)

for i,j in freq.items(): print(f'{i}: {j}')


