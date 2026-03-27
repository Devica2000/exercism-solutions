def value(colors):
    color_map = {
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

    return int("".join(str(color_map[color]) for color in colors[:2]))
    
    # result = ""
    # for i in range(2):
    #     band_color = colors[i]
    #     color_val = color_map[band_color]
    #     result += str(color_val)

    # return int(result)
        
        
        
