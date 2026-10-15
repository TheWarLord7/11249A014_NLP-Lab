from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

with open('a.txt') as f: sent = sent_tokenize(f.read().lower())[0]

tokens = word_tokenize(sent)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

for word in tokens:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print("{:<15} {:<15} {:<15}".format(word, stem, lemma))