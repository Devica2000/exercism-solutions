def append(list1, list2):
    # for item in list2:
        # list1 += [item]
    for i, item in enumerate(list2):
        list1.insert(len(list1) + i, item)
    return list1

def concat(lists):
    final_list = []
    for list in lists:
        append(final_list, list)
    return final_list
            
def filter(function, list):
    result = []
    for item in list:
        if function(item):
            append(result, [item])
    return result
            
def length(list):
    count = 0 
    for elem in list:
        count += 1
    return count

def map(function, list):
    result = []
    for item in list:
        append(result, [function(item)])
    return result

def foldl(function, list, initial):
    acc = initial
    for item in list:
        acc = function(acc, item)
    return acc
    

def foldr(function, list, initial):
    acc_r = initial
    for item in reverse(list):
        acc_r = function(acc_r, item)
    return acc_r


def reverse(list):
    result = []
    for item in range(len(list) - 1, -1, -1):
        append(result, [list[item]])
    return result
        
