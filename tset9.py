from nltk.tokenize import word_tokenize
from nltk import pos_tag

sent = 'The quick brown fox jumps over the lazy dog.'

tokens = word_tokenize(sent)
tags = pos_tag(tokens)


print(f'{'Words':<15} {'Tags'}')
for word, tag in tags:
    print(f'{word:<15} {tag}')
