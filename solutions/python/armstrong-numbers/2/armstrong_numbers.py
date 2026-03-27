def is_armstrong_number(number):
    total_digits = len(str(number))
    digit_sum = 0
    for num in str(number):
        digit_sum += int(num) ** total_digits
    return digit_sum == number
        
        
