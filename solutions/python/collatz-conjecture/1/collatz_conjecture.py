def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
        
    total_count = 0
    
    while number > 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        total_count += 1
            
    return total_count
        
        