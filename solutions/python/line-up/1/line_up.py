def line_up(name, number):
    
    last_two = number % 100
    last_one = number % 10

    if last_two in (11, 12, 13):
        ending = "th"
    elif last_one == 1:
        ending = 'st'
    elif last_one == 2:
        ending = 'nd'
    elif last_one == 3:
        ending = 'rd'
    else:
        ending = 'th'

    return f"{name}, you are the {number}{ending} customer we serve today. Thank you!"
