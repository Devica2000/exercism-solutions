def label(colors):
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
    base = (mapping[colors[0]] * 10) + mapping[colors[1]]
    zeros = mapping[colors[2]]
    value = base * (10 ** zeros)

    if value == 0:
        return f"{value} ohms"

    if value % 1000000000 == 0:
        return f"{value // 1000000000} gigaohms"
    if value % 1000000 == 0:
        return f"{value // 1000000} megaohms"
    if value % 1000 == 0:
        return f"{value // 1000} kiloohms"
    return f"{value} ohms"

    
#     color_mapping = {
#                     "black": 0,
#                      "brown": 1,
#                      "red": 2,
#                      "orange": 3,
#                      "yellow": 4,
#                      "green": 5,
#                      "blue": 6,
#                      "violet": 7,
#                      "grey": 8,
#                      "white": 9
#                     }
#     zero_mapping = {}
#     power = color_mapping[colors[2]]
#     result = int("".join(str(color_mapping[c]) for c in colors[:2])) * (10**power)

#     if power == 9:
#         result = int("".join(str(color_mapping[c]) for c in colors[:2]))
#         return f"{result} gigaohms"
#     elif power == 6:
#         result = int("".join(str(color_mapping[c]) for c in colors[:2]))
#         return f"{result} megaohms"
        
#     if result > 1000:
#         return f"{result//1000} kiloohms"
#     else:
#         return f"{result} ohms"
