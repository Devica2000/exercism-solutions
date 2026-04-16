def rectangles(strings):
    rows = len(strings)
    cols = len(strings[0]) if rows else 0

    corners = [(r,c) for r in range(rows)
              for c in range(cols)
              if strings[r][c] == '+']

    count = 0 

    for r1, c1 in corners:
        for r2, c2 in corners:
            if r2 <= r1 or c2 <= c1:
                continue
            if strings[r1][c2] != '+' or strings[r2][c1] != '+':
                continue
            if any(strings[r1][c] not in '+-' for c in range(c1 + 1, c2)):
                continue
            if any(strings[r2][c] not in '+-' for c in range(c1 + 1, c2)):
                continue
            if any(strings[r][c1] not in '+|' for r in range(r1 + 1, r2)):
                continue
            if any(strings[r][c2] not in '+|' for r in range(r1 + 1, r2)):
                continue
            count += 1

    return count
            
    
