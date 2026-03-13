def rows(letter):
    n = ord(letter) - ord('A')
    rows = []
    for i in range(n + 1):
        char = chr(ord('A') + i)
        padding = ' ' * (n - i)
        inner = ' ' * (2 * i - 1) if i > 0 else ''
        body = char if i == 0 else char + inner + char
        rows.append(padding + body + padding)

    return rows + rows[-2::-1]
