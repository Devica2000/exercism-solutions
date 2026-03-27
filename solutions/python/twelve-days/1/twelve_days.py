def recite(start_verse, end_verse):
    
    days = ['', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
           'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    
    gifts = ['', "a Partridge in a Pear Tree.",
             "two Turtle Doves",
             "three French Hens",
             "four Calling Birds",
             "five Gold Rings",
             "six Geese-a-Laying",
             "seven Swans-a-Swimming",
             "eight Maids-a-Milking",
             "nine Ladies Dancing",
             "ten Lords-a-Leaping",
             "eleven Pipers Piping",
             "twelve Drummers Drumming"]

    result = []

    for i in range(start_verse, end_verse + 1):
        if i == 1:
            combined_gifts = gifts[i]
        else:
            combined_gifts = ', '.join(gifts[j] for j in range(i, 1, -1))
            combined_gifts += f", and {gifts[1]}"

        result.append(f"On the {days[i]} day of Christmas my true love gave to me: {combined_gifts}")

    return result

             
             
             
             
             
             
             
        

    
