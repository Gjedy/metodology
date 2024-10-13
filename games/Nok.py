from random import randrange
from math import gcd

class nok_game:
    def __init__(self, min, max, number_amount):
        self.min = min
        self.max = max
        self.number_amount = number_amount

    def start(self):
        print("Find the smallest common multiple of given numbers.")
    
    def generate_numbers(self):
        lst = list()
        for i in range(self.number_amount):
            lst.append(randrange(self.min, self.max))
        return lst
        
    def get_answer(self, numbers):
        lcm = 1
        for number in numbers:
            lcm = lcm * number // gcd(lcm, number)
        return lcm
        


