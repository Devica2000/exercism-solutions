def is_pangram(sentence):
    letters = {ch for ch in sentence.lower() if ch.isalpha()}
    return len(letters) == 26