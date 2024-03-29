import os
import pymongo
from .singleton import Singleton
from .env import Env

class MongoClient(metaclass = Singleton):
  def __init__(self):
    self.__initialize_client()

  def get_database(self):
    return self.db

  def __fast_api_mode(self):
    return Env().get('FASTAPI_MODE')

  def __initialize_client(self):
    mongo_connection = Env().get("MONGO_CONNECTION")
    CONNECTION_STRING = f"mongodb://{mongo_connection}/"
    self.client = pymongo.MongoClient(CONNECTION_STRING)
    mongo_db_name = Env().get('MONGO_DB_NAME')
    self.db = self.client[mongo_db_name]
