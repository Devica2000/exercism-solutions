def is_paired(input_string):
    stack = []
    valid_matches = {")": "(", "}": "{", "]": "["}
    openers = set(valid_matches.values())

    for letter in input_string:
        if letter in valid_matches:
            if stack and stack[-1] == valid_matches[letter]:
                stack.pop()
            else:
                return False
        elif letter in openers:
            stack.append(letter)

    return True if not stack else False

    # return len(stack) == 0
    # return not stack
            
            
        