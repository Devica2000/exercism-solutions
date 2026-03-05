def square_of_sum(number):
    sum = 0
    for num in range(1, number + 1):
        sum += num
    return sum ** 2

def sum_of_squares(number):
    result = 0
    for num in range(1, number + 1):
        square = num ** 2
        result += square
        
    return result

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
