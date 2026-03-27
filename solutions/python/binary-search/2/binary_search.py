def find(search_list, value):
    low, high = 0, len(search_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = search_list[mid]

        if value == mid_val:
            return mid
        if value > mid:
            low = mid + 1
        else:
            high = mid - 1

    raise ValueError("value not in array")
            
        
