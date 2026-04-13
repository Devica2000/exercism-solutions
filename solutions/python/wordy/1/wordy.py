def answer(question):
    if not question.startswith("What is"):
        raise ValueError("unknown operation")

    question = question.removeprefix("What is").removesuffix("?").strip()

    if not question:
        raise ValueError("syntax error")

    question = question.replace("multiplied by", "multiplied_by")
    question = question.replace("divided by", "divided_by")
    tokens = question.split()

    try:
        result = int(tokens[0])
    except ValueError:
        raise ValueError("syntax error")

    valid_ops = {"plus", "minus", "multiplied_by", "divided_by"}

    i = 1
    while i < len(tokens):
        op = tokens[i]

        # Check operator validity FIRST
        if op not in valid_ops:
            if op.lstrip("-").isdigit():
                raise ValueError("syntax error")
            raise ValueError("unknown operation")

        # Then check for missing operand
        if i + 1 >= len(tokens):
            raise ValueError("syntax error")

        try:
            num = int(tokens[i + 1])
        except ValueError:
            raise ValueError("syntax error")

        if op == "plus":
            result += num
        elif op == "minus":
            result -= num
        elif op == "multiplied_by":
            result *= num
        elif op == "divided_by":
            result //= num

        i += 2

    return result