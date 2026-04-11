from collections import Counter

def best_hands(hands):
    def parse_hands(hand):
        VALUE_MAP = {'2': 2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
                     '10':10,'J':11,'Q':12,'K':13,'A':14}
        cards = hand.split()
        return [(VALUE_MAP[c[:-1]], c[-1]) for c in cards]

    def hand_rank(hand):
        #list of (val, suit) tuples
        cards = parse_hands(hand)
        vals = sorted([v for v, s in cards], reverse = True)
        suits = [s for v, s in cards]

        is_flush = len(set(suits)) == 1
        is_straight = vals[0] - vals[4] == 4 and len(set(vals)) == 5
        straight_high = vals[0]

        if not is_straight and set(vals) == {14, 2, 3, 4, 5}:
            is_straight = True
            straight_high = 5
            
        #{value:count}
        
        counts = Counter(vals)
        groups = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
        tiebreak = tuple(v for v, _ in groups) 
        top_count = groups[0][1]
        second_count = groups[1][1] if len(groups) > 1 else 0
    
        if is_flush and is_straight:             return (9, (straight_high,))
        if top_count == 4:                       return (8, tiebreak)
        if top_count == 3 and second_count == 2: return (7, tiebreak)
        if is_flush:                             return (6, tiebreak)
        if is_straight:                          return (5, (straight_high,))
        if top_count == 3:                       return (4, tiebreak)
        if top_count == 2 and second_count == 2: return (3, tiebreak)
        if top_count == 2:                       return (2, tiebreak)
        return (1, tiebreak)

    best_rank = max(hand_rank(h) for h in hands)
    return [h for h in hands if hand_rank(h) == best_rank]
        
    