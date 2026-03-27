class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        card = self.card_num.replace(" ", "")
        
        if len(card) <= 1:
            return False

        if not card.isdigit():
            return False
            
        total = 0
        for i, digit in enumerate(reversed(card)):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n

        return total % 10 == 0