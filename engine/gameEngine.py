class game_engine:
    def __init__(self, round_amount) :
        self.correct_answer_counter = 0
        self.round_amount = round_amount

    def play(self, name, game):
        game.start()

        for round in range(self.round_amount):
            numbers = game.generate_numbers()
            print('Question:',' '.join(str(number) for number in numbers))
            correct_answer = game.get_answer(numbers)
            print("Your answer: ")
            answer = input()
            if int(answer) == correct_answer:
                print("Correct!")
                self.correct_answer_counter += 1
            else:
                print(str(answer) + " is wrong answer ;(. Correct answer was " + str(correct_answer))
        
        if self.correct_answer_counter == self.round_amount:
            print("Congratulations, " + name + "!")
        else:
            print("You get " + str(self.correct_answer_counter) + "/" + str(self.round_amount) + " right")
            print("Let's try again, " + name + "!")