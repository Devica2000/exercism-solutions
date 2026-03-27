def find_anagrams(word, candidates):

    result = []
    
    word_cnt = {}
    for i in range(len(word)):
        word_cnt[word[i].lower()] = 1 + word_cnt.get(word[i].lower(), 0)

    for candidate in candidates:
        if len(candidate) != len(word):
            continue
        if candidate.lower() == word.lower():
            continue
            
        candidate_cnt = {}
        for i in range(len(candidate)):
            candidate_cnt[candidate[i].lower()] = 1 + candidate_cnt.get(candidate[i].lower(), 0)
            
        if candidate_cnt == word_cnt:
            result.append(candidate)

    return result
                
