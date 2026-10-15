from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.util import ngrams

with open('a.txt') as f: sent = sent_tokenize(f.read().lower())[0]

tokens = word_tokenize(sent)
print(tokens)

print('Unigram:\n', *ngrams(tokens, 1))
print('Bigram:\n', *ngrams(tokens, 2))
print('Trigram:\n', *ngrams(tokens, 3))