def reverse(text):
    reversed_str = ""
    for char in range(len(text) - 1, -1, -1):
        reversed_str += text[char]
    return reversed_str
        
