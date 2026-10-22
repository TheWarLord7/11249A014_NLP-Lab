from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag, RegexpParser

with open('a.txt') as f: x = f.read().lower()
sent = sent_tokenize(x)[0]

tokens = word_tokenize(sent)
pos_tags = pos_tag(tokens)


GRAMMER = r'NP: {<DT>?<JJ>*<NN.*>+}'
chunk_parser = RegexpParser(GRAMMER)

chunk_tree = chunk_parser.parse(pos_tags)

print(pos_tags)
print(chunk_tree)

