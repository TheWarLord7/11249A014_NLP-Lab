def generate_words(w: str):

    print('Root Word:', w)
    print('Plural Form:', w+'es' if w.endswith(('s','x','z','ch','sh')) else w+'s')
    print('Present Participle Form:', w[:-1]+'ing' if w.endswith('e') and not w.endswith('ee') else w+'ing')
    print('Past Tense Form:', w+'d' if w.endswith('e') else w+'ed')

generate_words(input('Enter Root Word: '))