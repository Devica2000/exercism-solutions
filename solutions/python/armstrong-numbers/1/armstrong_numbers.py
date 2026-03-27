def is_armstrong_number(number):
    total_digits = len(str(number))
    sum = 0
    for num in str(number):
        sum += int(num) ** total_digits
    return sum == number
        
        
