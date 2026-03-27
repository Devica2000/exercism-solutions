import sys

def is_valid(isbn):
# - Conditions:
# 1. 10 digits in total
# 2. First 9 didgits are numbers
# 3. Last digit can be a number of "X"
# 4. May or may not have hyphens
# 5. mod 11 == 0
    
    if not isbn:
        return False
        
    valid_isbn = isbn.replace("-", "").strip().upper()

    if len(valid_isbn) != 10:
        return False

    if not valid_isbn[:9].isdigit():
        return False

    last = valid_isbn[9]
    if not (last == "X" or last.isdigit()):
        return False

    total = 0
    for idx, val in enumerate(valid_isbn):
        weight = 10 - idx
        if val == "X":
            total += 10 * weight
        else:
            total += int(val) * weight

    return total % 11 == 0

                            
    
    