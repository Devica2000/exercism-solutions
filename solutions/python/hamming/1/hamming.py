def distance(strand_a, strand_b):
    
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    distance = 0
    for i in range(len(strand_a)):
        if strand_a[i].lower() != strand_b[i].lower():
            distance += 1

    return distance