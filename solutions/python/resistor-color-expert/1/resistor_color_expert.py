def resistor_label(colors):
    mapping = {
                    "black": 0,
                     "brown": 1,
                     "red": 2,
                     "orange": 3,
                     "yellow": 4,
                     "green": 5,
                     "blue": 6,
                     "violet": 7,
                     "grey": 8,
                     "white": 9
            }
    tolerances = {"grey": 0.05,
                 "violet": 0.1,
                 "blue": 0.25,
                 "green": 0.5,
                 "brown": 1,
                 "red": 2,
                 "gold": 5,
                 "silver": 10
    }

    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        base = (mapping[colors[0]] * 10) + mapping[colors[1]]
        zeros = mapping[colors[2]]
        tolerance = tolerances[colors[3]]
        
    if len(colors) == 5:
        base = (mapping[colors[0]] * 100) + (mapping[colors[1]] * 10) + mapping[colors[2]]
        zeros = mapping[colors[3]]
        tolerance = tolerances[colors[4]]

    value = base * (10 ** zeros)

    if value >= 1_000_000_000:
        amount = value / 1_000_000_000
        unit = "gigaohms"
    elif value >= 1_000_000:
        amount = value / 1_000_000
        unit = "megaohms"
    elif value >= 1_000:
        amount = value / 1_000
        unit = "kiloohms"
    else:
        amount = value
        unit = "ohms"

    if amount == int(amount):
        amount = int(amount)

    return f"{amount} {unit} ±{tolerance}%"

        
        
    
