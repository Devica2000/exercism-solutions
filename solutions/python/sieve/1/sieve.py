def primes(limit):
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
        p += 1

    return [i for i, prime in enumerate(is_prime) if prime]
        
    # unmarked = []
    # marked = []
    
    # for i in range(2, limit + 1):
    #     unmarked.append(i)

    # for i in range(len(unmarked)):
    #     if unmarked[i] in marked:
    #         continue
    #     for j in range(i+1, len(unmarked)):
    #         if unmarked[j] % unmarked[i] == 0:
    #             marked.append(unmarked[j])

    # result = [item for item in unmarked if item not in marked]
    # return result
            
