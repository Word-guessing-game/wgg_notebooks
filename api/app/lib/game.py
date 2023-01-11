''' Contains Guess word game flow '''
import random
import string
from app.models.nltk import Nltk
from app.lib.mongo_client import MongoClient

class Game:
  def __init__(self):
    self.word_corpus = Nltk()
    self.hidden_word = self.word_corpus.random_word()

  def create(self):
    ''' Создаёт новую игру '''
    game_id = self.__generate_id()
    self.__create_game_item(game_id)
    return { 'status': 'success', 'game_id': game_id }

  def check(self, word: str):
    ''' Check user attempt to guess word '''
    similarity_degree, similarity_index = self.word_corpus.similarity(self.hidden_word, word)

    if word == self.hidden_word:
      return { 'status': 'guess', 'msg': f'{word} is great! {similarity_degree}' }

    message = f'{word} is {similarity_degree}, at a distance of {similarity_index} words from the intended word.'
    return { 'status': 'not_guess', 'msg': message }

  # Приватные методы

  def __generate_id(self, size = 10):
    ''' Генерирует случайную строку заданной длины '''
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))

  def __create_game_item(self, game_id: str):
    ''' Создаёт новую запись в коллекции games в mongodb '''
    MongoClient().collection('games').insert_one({ '_id': game_id, 'attempts': [] })
