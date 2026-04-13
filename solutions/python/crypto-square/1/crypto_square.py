import math

def cipher_text(plain_text):

    normalized = "".join(c.lower() for c in plain_text if c.isalnum())

    if not normalized:
        return ""

    length = len(normalized)
    c = math.ceil(math.sqrt(length))
    r = math.ceil(length / c)

    normalized = normalized.ljust(r * c)

    rows = [normalized[i * c: (i + 1) * c] for i in range(r)]

    chunks = []
    for col in range(c):
        chunk = "".join(row[col] for row in rows)
        chunks.append(chunk)

    return " ".join(chunks)

    
