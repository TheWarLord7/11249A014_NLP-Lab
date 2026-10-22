# Set of possible POS tags
tags = ['PRON', 'DET', 'NOUN', 'VERB']

# Initial probabilities
start_prob = {
    'PRON': 0.5,
    'DET': 0.2,
    'NOUN': 0.2,
    'VERB': 0.1
}

# Transition probabilities
trans_prob = {
    'PRON': {'PRON': 0.1, 'DET': 0.1, 'NOUN': 0.1, 'VERB': 0.7},
    'DET': {'PRON': 0.0, 'DET': 0.1, 'NOUN': 0.8, 'VERB': 0.1},
    'NOUN': {'PRON': 0.2, 'DET': 0.2, 'NOUN': 0.2, 'VERB': 0.4},
    'VERB': {'PRON': 0.1, 'DET': 0.5, 'NOUN': 0.3, 'VERB': 0.1}
}

# Emission probabilities
emit_prob = {
    'i': {'PRON': 0.9},
    'love': {'VERB': 0.8},
    'python': {'NOUN': 0.7},
    'nlp': {'NOUN': 0.9},
    'is': {'VERB': 0.95},
    'easy': {'NOUN': 0.6, 'VERB': 0.4}
}

# Read input sentence
sentence = 'I love Python I love NLP Python is easy'.lower().split()

# Viterbi initialization
V = [{}]
backpointer = [{}]
for tag in tags:
    emission = emit_prob.get(sentence[0], {}).get(tag, 0)
    V[0][tag] = start_prob[tag] * emission
    backpointer[0][tag] = None

# Viterbi recursion
for t in range(1, len(sentence)):
    V.append({})
    backpointer.append({})
    for tag in tags:
        emission = emit_prob.get(sentence[t], {}).get(tag, 0)
        best_prob = 0
        best_prev = None
        for prev_tag in tags:
            prob = V[t-1][prev_tag] * trans_prob[prev_tag][tag] * emission
            if prob > best_prob:
                best_prob = prob
                best_prev = prev_tag
        V[t][tag] = best_prob
        backpointer[t][tag] = best_prev

# Find the best final tag
last_tag = max(V[-1], key=V[-1].get)
if V[-1][last_tag] == 0:
    print("No valid POS tag sequence found.")
else:
    # Backtracking
    best_path = [last_tag]
    for t in range(len(sentence)-1, 0, -1):
        best_path.insert(0, backpointer[t][best_path[0]])
    
    print("\nWord\tPOS Tag")
    print("-" * 20)
    for word, tag in zip(sentence, best_path):
        print(f"{word}\t{tag}")
    print("\nMost probable tag sequence:", best_path)
