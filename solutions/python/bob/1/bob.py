def response(hey_bob):
    if hey_bob.strip().endswith("?") and not hey_bob.isupper():
        return "Sure."
    elif hey_bob.isupper() and not hey_bob.strip().endswith("?"):
        return "Whoa, chill out!"
    elif hey_bob.strip().endswith("?") and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.strip() == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."