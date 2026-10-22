from nltk import word_tokenize
from nltk.tag import hmm

training_data = [
    [
        ('The', 'DET'),
        ('customer', 'NOUN'),
        ('needs', 'VERB'),
        ('help', 'NOUN')
    ],
    [
        ('The', 'DET'),
        ('user', 'NOUN'),
        ('reports', 'VERB'),
        ('problem', 'NOUN')
    ],
    [
        ('A', 'DET'),
        ('customer', 'NOUN'),
        ('requests', 'VERB'),
        ('support', 'NOUN')
    ],
    [
        ('The', 'DET'),
        ('agent', 'NOUN'),
        ('provides', 'VERB'),
        ('assistance', 'NOUN')
    ]
]

HMM = hmm.HiddenMarkovModelTrainer()
tagger = HMM.train_supervised(training_data)

sent = 'The agent provides assistance'
tokens = word_tokenize(sent)
tags = tagger.tag(tokens)

print('Words\t\tTags')
for word, tag in tags: print(f'{word}\t\t{tag}')
