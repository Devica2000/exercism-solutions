def transform(legacy_data):
    
    new_mapping = {}
    
    for key, val in legacy_data.items():
        new_val = key
        for letter in val:
            if letter.lower() not in new_mapping:
                new_mapping[letter.lower()] = new_val
                
    return new_mapping

    