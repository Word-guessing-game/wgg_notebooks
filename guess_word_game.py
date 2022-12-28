from app.models.nlp.nltk import Nltk as NlpModel
from app.use_cases.games.guess_word_game import GuestWordGame

game = GuestWordGame(NlpModel)
game.run()
