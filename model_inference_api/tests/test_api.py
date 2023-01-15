from unittest import TestCase
from fastapi.testclient import TestClient
from ..app.api import app
from .helpers.assertions import assertJsonEqual, assertListOfJsonEqual

client = TestClient(app)

def test_health():
    ''' Проверка "Здоровья" соединения с mongodb '''
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == True

def test_get_games_numbers():
    ''' Получение списка заготовленных четырёх игр '''
    response = client.post("/get_games_numbers")
    assert response.status_code == 200
    assert len(response.json()) == 4

def test_get_word_position():
    ''' Получение расстояния до загаданного кода в выбранной игре '''
    response = client.post("/get_word_position", json = {"n_game": "game4", "game_word": "lolol"})
    assert response.status_code == 200
    assertJsonEqual(response.json(), {'position': 9999999, 'word': 'lolol'})

def test_get_word_position_without_params():
    ''' Получение расстояния до загаданного кода в выбранной игре, если передан пустой параметр '''
    response = client.post("/get_word_position", json = {"n_game": "game4", "game_word": ""})
    assert response.status_code == 200
    assertJsonEqual(response.json(), {'position': 9999999, 'word': ''})

def test_get_first_similar_words():
    ''' Получение 10 похожих слов '''
    response = client.post("/get_first_similar_words", json = {"n_game": "game4"})
    assert response.status_code == 200
    assert len(response.json()) == 10
