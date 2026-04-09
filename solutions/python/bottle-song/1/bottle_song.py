def recite(start, take=1):
    number_words = ["no", "one", "two", "three", "four", "five",
                   "six", "seven", "eight", "nine", "ten"]

    def bottles(n):
        word = number_words[n]
        plural = "s" if n != 1 else ""
        return f"{word} green bottle{plural}"

    result = []

    for current in range(start, start - take, -1):
        remaining = current - 1
        if result:
            result.append("")
        result += [
            f"{bottles(current)} hanging on the wall,".capitalize(),
            f"{bottles(current)} hanging on the wall,".capitalize(),
            "And if one green bottle should accidentally fall,",
            f"There'll be {bottles(remaining)} hanging on the wall.",
        ]

    return result
