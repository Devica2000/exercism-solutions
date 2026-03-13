def egg_count(display_value):
    
    count = 0

    while display_value > 0:
        remainder = display_value % 2
        if remainder == 1:
            count += 1
        display_value //= 2

    return count
    
    # if display_value == 0:
    #     return 0 

    # binary_number = ""
    # while display_value > 0:
    #     remainder = display_value % 2
    #     binary_number = str(remainder) + binary_number
    #     display_value = display_value // 2

    # count = 0
    
    # for num in binary_number:
    #     if num == "1":
    #         count += 1
            
    # return count
