def tick(matrix):
    if not matrix:
        return []
        
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            counts = 0 
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue

                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        counts += matrix[nr][nc]

            if matrix[row][col] == 1 and counts in (2,3):
                result[row][col] = 1
            elif matrix[row][col] == 0 and counts == 3:
                result[row][col] = 1

    return result
                    

            
                
            
            
