def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
           'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
           'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    def helper(n):
        if n < 20:
            return ones[n]
        if n < 100:
            remainder = n % 10
            base = tens[n // 10]
            return base if remainder == 0 else f"{base}-{ones[remainder]}"
        if n < 1_000:
            remainder = n % 100
            base = f"{helper(n // 100)} hundred"
            return base if remainder == 0 else f"{base} {helper(remainder)}"
        if n < 1_000_000:
            remainder = n % 1000
            base = f"{helper(n // 1000)} thousand"
            return base if remainder == 0 else f"{base} {helper(remainder)}"
        if n < 1_000_000_000:
            remainder = n % 1_000_000
            base = f"{helper(n // 1_000_000)} million"
            return base if remainder == 0 else f"{base} {helper(remainder)}"
        else:
            remainder = n % 1_000_000_000
            base = f"{helper(n // 1_000_000_000)} billion"
            return base if remainder == 0 else f"{base} {helper(remainder)}"
            
    return helper(number)