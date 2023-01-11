import os
import unittest
from app.lib.game import Game
from app.lib.mongo_client import MongoClient

class TestGame(unittest.TestCase):
  ''' Юнит - тесты для движка игры '''

  def test_start_game(self):
    ''' Проверяет создание новой игры '''
    result = Game().create()
    assert result['status'] == 'success'
    assert len(result['game_id']) == 10
    game_item = MongoClient().collection('games').find_one({ '_id': result['game_id'] })
    assert game_item is not None
    assert len(game_item['attempts']) == 0
