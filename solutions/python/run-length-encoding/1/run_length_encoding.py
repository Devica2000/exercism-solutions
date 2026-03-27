def decode(string):
    decoded = ''
    count_str = ''

    for elem in string:
        if elem.isdigit():
            count_str += elem
        else:
            count = int(count_str) if count_str else 1
            decoded += elem * count
            count_str = ''

    return decoded
    
def encode(string):
    if not string:
        return ''

    encoded = ''
    count = 1

    for i in range(1, len(string), 1):
        if string[i] == string[i - 1]:
            count += 1

        else:
            encoded += (str(count) if count > 1 else '') + string[i-1]
            count = 1

    encoded += (str(count) if count > 1 else '') + string[-1]
    
    return encoded

    
