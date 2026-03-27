def sum_of_multiples(limit, multiples):
    
    result = set()
    
    for elem in multiples:
        if elem != 0 and elem < limit:
            loop_until = limit//elem
            
            for i in range(1, loop_until + 1, 1):
                value = elem * i
                if value < limit:
                    result.add(value)
                    
    return sum(result)
                
        
