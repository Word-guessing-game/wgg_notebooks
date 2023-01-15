import os
from dotenv import load_dotenv
from .singleton import Singleton

class Env(metaclass = Singleton):
  def __init__(self):
    load_dotenv()

  def get(self, variable_name: str):
    ''' Получает содержимое переменной окружения '''
    return os.getenv(variable_name)
