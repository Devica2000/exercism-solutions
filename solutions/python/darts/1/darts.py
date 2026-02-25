def score(x, y):
    point_radius = x ** 2 + y ** 2

    if point_radius <= 1:
        return 10
    elif point_radius <= 25:
        return 5
    elif point_radius <= 100:
        return 1
    else:
        return 0
    
        
