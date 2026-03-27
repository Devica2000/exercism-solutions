def square_root(number):
    
    for i in range(1, number + 1, 1):
        value = round(i * i, 2)
        if value == number:
            return i
            
