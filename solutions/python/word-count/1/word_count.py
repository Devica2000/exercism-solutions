import re

def count_words(sentence):
    
    sentence = sentence.lower()
    words = re.split(r"[^a-z0-9']|_", sentence)
    word_count = {}

    for word in words:
        word = word.strip("'")
        if word and re.search(r"[a-z0-9]", word):
            word_count[word] = word_count.get(word, 0) + 1

    return word_count
