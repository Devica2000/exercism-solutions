def encode(plain_text):
    new_text = ""
    for t in plain_text.strip().lower():
        if t.isalpha():
            index = ord('z') - ord(t) + ord('a')
            new_letter = chr(index)
            new_text += new_letter
        elif t.isnumeric():
            new_text += t
        else:
            continue

    chunks = ' '.join(new_text[i:i+5] for i in range(0, len(new_text), 5))

    return chunks

def decode(ciphered_text):
    final_text = ""
    for t in ciphered_text.strip().lower():
        if t.isalpha():
            index = ord('z') - ord(t) + ord('a')
            letter = chr(index)
            final_text += letter
        elif t.isnumeric():
            final_text += t

    return final_text
            
    
