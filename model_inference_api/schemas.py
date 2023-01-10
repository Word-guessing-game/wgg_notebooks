from pydantic import BaseModel


class WordPosition(BaseModel):
    n_game: str
    game_word: str
