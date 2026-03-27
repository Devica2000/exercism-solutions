import re

def abbreviate(words):
    
    cleaned = re.sub(r"[^A-Za-z0-9\s-]", "", words)
    word_list = cleaned.replace("-", " ").split()
    return "".join(word[0].upper() for word in word_list)


    
    # word_list = words.split()
    # abb = ""
    # special_character = ['-']
    # for word in word_list:
    #     if '-' not in word:
    #         replaced_word = word.replace('_', '')
    #         abb += replaced_word.upper()[0]
    #     elif '-' in word and len(word) > 1:
    #         new_word = word.split("-")
    #         for new in new_word:
    #             abb += new.upper()[0]
    #     else:
    #         continue

    # return abb
                
            
