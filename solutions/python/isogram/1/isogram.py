def is_isogram(string):
    letters = [s for s in string.lower() if s.isalnum()]
    return len(letters) == len(set(letters))
