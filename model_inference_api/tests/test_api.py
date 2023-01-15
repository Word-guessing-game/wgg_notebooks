import mongomock
from fastapi.testclient import TestClient
from ..app.api import app

mongo_client = mongomock.MongoClient()
mongo_db = mongo_client.db
client = TestClient(app)

@mongomock.patch(servers=(('0.0.0.0', 27017),))
def test_health():
    ''' Проверка "Здоровья" соединения с mongodb '''
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == True


@mongomock.patch(servers=(('0.0.0.0', 27017),))
def test_get_games_numbers():
    ''' Получение списка заготовленных четырёх игр '''
    response = client.post("/get_games_numbers")
    assert response.status_code == 200
    expected_game_numbers = [{'name': 'game3', 'number': 0}, {'name': 'game4', 'number': 1}, {'name': 'game1', 'number': 2}, {'name': 'game2', 'number': 3}]
    assert response.json() == expected_game_numbers

@mongomock.patch(servers=(('0.0.0.0', 27017),))
def test_get_word_position():
    ''' Получение расстояния до загаданного кода в выбранной игре '''
    response = client.post("/get_word_position", json = {"n_game": "game4", "game_word": "lolol"})
    assert response.status_code == 200
    assert response.json() == {'position': 9999999, 'word': 'lolol'}

@mongomock.patch(servers=(('0.0.0.0', 27017),))
def test_get_word_position_without_params():
    ''' Получение расстояния до загаданного кода в выбранной игре, если передан пустой параметр '''
    response = client.post("/get_word_position", json = {"n_game": "game4", "game_word": ""})
    assert response.status_code == 200
    assert response.json() == {'position': 9999999, 'word': ''}

@mongomock.patch(servers=(('0.0.0.0', 27017),))
def test_get_first_similar_words():
    ''' Получение 10 похожих слов '''
    response = client.post("/get_first_similar_words", json = {"n_game": "game4"})
    assert response.status_code == 200
    assert len(response.json()) == 10

