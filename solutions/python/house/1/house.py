def recite(start_verse: int, end_verse: int) -> list[str]:
    subjects = [
        "the house that Jack built.",
        "the malt",
        "the rat",
        "the cat",
        "the dog",
        "the cow with the crumpled horn",
        "the maiden all forlorn",
        "the man all tattered and torn",
        "the priest all shaven and shorn",
        "the rooster that crowed in the morn",
        "the farmer sowing his corn",
        "the horse and the hound and the horn",
    ]

    actions = [
        None,
        "that lay in",
        "that ate",
        "that killed",
        "that worried",
        "that tossed",
        "that milked",
        "that kissed",
        "that married",
        "that woke",
        "that kept",
        "that belonged to",
    ]

    verses = []

    for n in range(start_verse, end_verse + 1):
        line = "This is " + subjects[n - 1]

        for i in range(n - 1, 0, -1):
            line += " " + actions[i] + " " + subjects[i - 1]

        verses.append(line)

    return verses