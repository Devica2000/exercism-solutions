def is_pangram(sentence):
    letters = {alphabet for alphabet in sentence.lower() if alphabet.isalpha()}
    return len(letters) == 26