from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.lib.game import Game

class Guess(BaseModel):
  word: str

app = FastAPI()
app.game = None

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/hello-world")
async def read_main():
  return {"msg": "Hello World"}

@app.post("/start-game")
async def start_game():
  app.game = Game()
  return {"msg": "Game started"}

@app.post("/reset-game")
async def reset_game():
  app.game = Game()
  return {"msg": "Game restarted"}

@app.post("/guess-word")
async def guess(request: Guess):
  print(f'{request.word=}')

  result = app.game.check(request.word)
  return result
