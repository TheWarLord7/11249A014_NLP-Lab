from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

sent = 'I love Python I love NLP Python is easy'.lower()

tokens = [word for word in word_tokenize(sent) if word.isalpha()]
count = Counter(tokens)
V = len(count)
N = sum(count.values())

print("{:<15} {:<15} {:<15}".format('Word', 'Count', 'Smoothed Probability'))
for i,j in count.items():
    for k in [i,j,round((j+1)/(N+V),4)]: print(k, ' '*(15-len(str(k))), end='')
    print()