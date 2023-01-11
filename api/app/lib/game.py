''' Contains Guess word game flow '''
from app.models.nltk import Nltk
from app.lib.mongo_client import MongoClient

class Game:
  def __init__(self):
    self.word_corpus = Nltk()
    self.hidden_word = self.word_corpus.random_word()

  def check(self, word: str):
    ''' Check user attempt to guess word '''
    similarity_degree, similarity_index = self.word_corpus.similarity(self.hidden_word, word)

    if word == self.hidden_word:
      return { 'status': 'guess', 'msg': f'{word} is great! {similarity_degree}' }

    message = f'{word} is {similarity_degree}, at a distance of {similarity_index} words from the intended word.'
    return { 'status': 'not_guess', 'msg': message }
