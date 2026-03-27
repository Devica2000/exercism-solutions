def translate(text):
    words = text.split()
    return ' '.join(process_word(word) for word in words)

def process_word(word):
    vowels = 'aeiou'

    if word[0] in vowels or word[:2] in('xr', 'yt'):
        return word + 'ay'

    i = 0
    while i < len(word):

        ch = word[i]

        if word[i:i+2] == 'qu':
            i += 2
            break

        if ch == 'y' and i > 0:
            break

        if ch in vowels:
            break

        i += 1

    return word[i:] + word[:i] + 'ay'


    

    
    
    
    
