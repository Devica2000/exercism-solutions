class Allergies:
    allergy_scores = {128: 'cats',
                  64: 'pollen',
                  32: 'chocolate',
                  16: 'tomatoes',
                  8: 'strawberries',
                  4: 'shellfish',
                  2: 'peanuts',
                  1: 'eggs'}

    def __init__(self, score):
        self.score = score % 256
        self._allergies = []
        remaining = self.score

        for value, name in self.allergy_scores.items():
            if remaining >= value:
                remaining -= value
                self._allergies.append(name)

    def allergic_to(self, item):
        return item in self._allergies

    @property
    def lst(self):
        return self._allergies
        