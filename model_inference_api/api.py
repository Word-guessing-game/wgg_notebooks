import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware


from utils import get_word_dict, get_word_list_json, get_database

load_dotenv()
host = os.environ.get("HOST")
mongodb = get_database()


if host is None:
    raise ValueError("Environment variable HOST should be defined!")

word_dict = get_word_dict()

app = FastAPI()

origins = [
    f"{host}:3000",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", status_code=status.HTTP_200_OK)
def is_model_loaded() -> bool:
    """Check whether model was loaded.

    Need this to force other services wait until model will be loaded.
    """
    return word_dict is not None


words_for_game = ["government", "mistake", "notebook", "bathroom"]

if mongodb.list_collection_names() == []:
    for count, word in enumerate(words_for_game, start=1):
        word_json = get_word_list_json(word, word_dict)
        mycol = mongodb[f"game{count}"]
        mycol.insert_many(word_json)


@app.post("/get_games_numbers", status_code=200)
async def get_collections_names():
    """Returns numbers of games recorded in db."""
    names = mongodb.list_collection_names()
    result = []
    for num, value in enumerate(names):
        result.append({"number": num, "name": value})
    return result


@app.post("/get_word_position", status_code=200)
async def get_word_position_in_collection(n_game: str = "game1", word: str = "country"):
    """Returns word position in requested game."""
    query = {"word": word}
    result = mongodb[n_game].find(query)
    word_position = []
    for i in result:
        word_position.append(i.get("position"))
    result_obj = {"word": word, "position": word_position[0]}
    return result_obj


@app.post("/get_first_similar_words", status_code=200)
async def get_similar_words(n_game: str = "game1"):
    """Returns first 10 similar words to guessed word."""
    result = mongodb[n_game].find().sort("position").limit(10)
    similar_words = []
    for i in result:
        similar_words.append([i.get("word"), i.get("position")])
    return similar_words
