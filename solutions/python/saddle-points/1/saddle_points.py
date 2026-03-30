def saddle_points(matrix):
    
    if not matrix or matrix == [[]]:
        return []
        
    rows = len(matrix)
    cols = len(matrix[0])

    for row in matrix:
        if len(row) != cols:
            raise ValueError("irregular matrix") 

    row_maxes = [max(row) for row in matrix]

    col_mins = []
    for c in range(cols):
        col_values = []
        for r in range(rows):
            col_values.append(matrix[r][c])
        col_mins.append(min(col_values))

    results = []

    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if val == row_maxes[r] and val == col_mins[c]:
                results.append({"row": r + 1, "column": c + 1})
                
    return results
                
                
            
            