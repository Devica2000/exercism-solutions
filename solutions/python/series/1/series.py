def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if not series:
        raise ValueError("series cannot be empty")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    return [series[i:i+length] for i in range(len(series) - length + 1)]

    # final_list = []
    
    # for i in range(0, len(series), 1):
    #     val = series[i:i+length]
    #     if len(val) != length:
    #         continue
    #     else:
    #         final_list.append(series[i:i+length])

    # return final_list
        
        
        
        

        
