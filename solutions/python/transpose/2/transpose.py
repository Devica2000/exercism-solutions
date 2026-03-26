def transpose(text):
    rows = text.split('\n')
    max_len = max(len(row) for row in rows)

    padded = [row.ljust(max_len, '\0') for row in rows]

    transposed = []

    for col in range(max_len):
        new_text = ''
        for row in padded:
            new_text += row[col]
            
        transposed.append(new_text)

    result = [] 
    for row in transposed:
        stripped = row.rstrip('\0')
        restored = stripped.replace('\0', ' ')
        result.append(restored)

    return '\n'.join(result)
        
    
