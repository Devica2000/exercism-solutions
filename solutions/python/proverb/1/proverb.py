def proverb(*items, qualifier = ""):
    if not items:
        return []
        
    string = []
    for i in range(len(items) - 1):
        string_to_add = f"For want of a {items[i]} the {items[i+1]} was lost."
        string.append(string_to_add)

    first = f"{qualifier} {items[0]}".strip() if qualifier else items[0]
        
    string.append(f"And all for the want of a {first}.")
    return string
        
