import random
import string

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        else:
            if key.isalpha() and key.islower():
                self.key = key
            else:
                raise ValueError("Invalid key")

    def encode(self, text):
        cipher_text = ''
        for i in range(len(text)):
            val = ord(self.key[i % len(self.key)]) - ord('a')
            new_text = chr((val + (ord(text[i]) - ord('a'))) % 26 + ord('a'))
            cipher_text += new_text
        return cipher_text

    def decode(self, text):
        plain_text = ''
        for i in range(len(text)):
            val = ord(self.key[i % len(self.key)]) - ord('a')
            new_text = chr(((ord(text[i]) - ord('a')) - val) % 26 + ord('a'))
            plain_text += new_text
        return plain_text

