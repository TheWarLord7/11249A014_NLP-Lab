from nltk.metrics import edit_distance

sent = 'I love Python I love NLP Python is easy'.lower()
sent1 = 'I love Java I love NLP Java is easy'.lower()

dist = edit_distance(sent, sent1)
maxl = max(len(sent), len(sent1))
sim = 1 if maxl == 0 else 1 - (dist/maxl)

print(f'String 1: {sent}\nString 2: {sent1}')   
print(f'Edit Distance: {dist}\nSimilarity Score: {round(sim, 4)}\nSimilarity Percentage: {round(sim, 4)*100}%')
print(f'Result: {'Highly Similar' if sim >= .8 else 'Moderately Similar' if sim >= .5 else 'Less Similar'}')