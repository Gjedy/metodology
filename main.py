from games.Nok import nok_game
from games.progression import progression_game
from engine.gameEngine import game_engine
from src.cli import cli 


name = cli.greeting()
nok = nok_game(1, 10, 3)
progression = progression_game(2, 10)
engine = game_engine(3)
#engine.play(name, nok)
engine.play(name, progression)

#numbers = nok.generate_numbers()
#print('Question:',' '.join(str(number) for number in numbers))
#game = progression.progression_game(1, 10, name)
#print(game.progression_hidden)
#print(game.progression_length)
#game.start()