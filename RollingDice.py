import random


class Dice:
    def roll(self):
        numbers = (1, 2, 3, 4, 5, 6)
        print(f'({random.choice(numbers)},{random.choice(numbers)})')


dice = Dice()
dice.roll()