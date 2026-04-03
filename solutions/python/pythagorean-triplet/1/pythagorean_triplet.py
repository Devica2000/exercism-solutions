def triplets_with_sum(number):
    result = []

    for a in range(1, number // 3):
        numerator = number * (number - 2 * a)
        denominator = 2 * (number - a)
        if numerator % denominator == 0:
            b = numerator // denominator
            c = number - a - b
            if a < b < c:
                result.append([a, b, c])

    return result

    
    # for i in range(1, number // 3):
    #     for j in range(i + 1, (number - i) // 2):
    #         k = number - i - j
    #         if i**2 + j**2 == k**2:
    #             result.append([i, j , k])
    # return result
                        
                    
