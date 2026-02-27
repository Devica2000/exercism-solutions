def rotate(text, key):
    if key < 0 or key > 26:
        raise ValueError("Invalid")

    cipher_text = ""

    for val in text:
        if val.isalpha():
            if val.islower():
                base = ord('a')
            else:
                base = ord('A')
            rotated = (ord(val) - base + key) % 26
            result = chr(base + rotated)
            cipher_text += result
        else:
            cipher_text += val

    return cipher_text