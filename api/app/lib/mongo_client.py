import os
import pymongo
from app.lib.singleton import Singleton

class MongoClient(metaclass = Singleton):
  def __init__(self):
    self.client = pymongo.MongoClient(f"mongodb://{self.__mongo_user_name()}:{self.__mongo_password()}@{self.__mongo_host()}")
    self.db = self.client[self.__mongo_database_name()]

  def check_connection(self):
    ''' Преверяет статус соединения с mongodb '''
    return self.client.server_info()['version'] is not None

  def collection(self, collection_name):
    ''' Возвращает коллекцию по имени '''
    return self.db[collection_name]

  # Приватные методы класса

  def __mongo_user_name(self):
    ''' Из переменных окружения получает имя пользователя mongodb '''
    print(f"{os.getenv('MONGO_USER_NAME')=}")
    return os.getenv('MONGO_USER_NAME')

  def __mongo_password(self):
    ''' Из переменных окружения получает пароль пользователя mongodb '''
    print(f"{os.getenv('MONGO_USER_PASSWORD')=}")
    return os.getenv('MONGO_USER_PASSWORD')

  def __mongo_database_name(self):
    ''' Из переменных окружения получает имя БД mongodb '''
    print(f"{os.getenv('MONGO_DATABASE_NAME')=}")
    return os.getenv('MONGO_DATABASE_NAME')

  def __mongo_host(self):
    ''' Из переменных среды получает адрес хоста с mongodb '''
    print(f"{os.getenv('MONGO_HOST')=}")
    return os.getenv('MONGO_HOST')
