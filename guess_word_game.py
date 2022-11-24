from app.models.word_corpus import WordCorpus
from app.use_cases.games.guess_word_game import GuestWordGame

game = GuestWordGame(WordCorpus)
game.run()
