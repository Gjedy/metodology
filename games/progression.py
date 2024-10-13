from random import randrange



class progression_game:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def start(self):
        print("What number is missing in the progression?")
        
    def generate_numbers(self):
        lst = []
        length = randrange(5, 10)
        progression_num = randrange(self.min, self.max)
        hidden = randrange(self.min, length)
        for i in range(length):
            if i == hidden:
                self.answer = progression_num**hidden
                lst.append(".." )
            else:
                lst.append(progression_num**i)
        return lst

    def get_answer(self, numbers):
        return self.answer
        
    
        
        