from models.storages.search import SearchStorage
from models.storages.entity import StorageEntity
from models.storages.generate import GenerateStorage
from benchmark import benchmark
from models.entities.tournament import Tournament
from models.entities.team import Team

import psycopg2
from config import Config


class Database(object):

    @benchmark
    def __init__(self):
        self.__conn = psycopg2.connect(dbname=Config.db_name, user=Config.user,
                                       password=Config.passwd, host='localhost')
        self.__cursor = self.__conn.cursor()
        self.tournaments = StorageEntity(Tournament)
        self.teams = StorageEntity(Team)

        self.searches = SearchStorage(self.__cursor)
        self.generate = GenerateStorage(self.__conn)

    @benchmark
    def __del__(self):
        self.__conn.commit()
        self.__cursor.close()
        self.__conn.close()
