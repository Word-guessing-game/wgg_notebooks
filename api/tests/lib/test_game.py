import os
import unittest
from app.lib.game import Game

class TestGame(unittest.TestCase):
  ''' Юнит - тесты для монго-клиента '''

  def test_check_connection(self):
    ''' Проверяет правильность соединения клиента с mongodb '''
    assert MongoClient().check_connection() is True

  def test_collection(self):
    ''' Проверяет правильность создания коллекций '''
    games_collection = MongoClient().collection('games')
    assert games_collection.database.name == os.getenv('MONGO_DATABASE_NAME')
