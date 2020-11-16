from storages.tournaments import TournamentStorage
from storages.teams import TeamStorage
from storages.games import GameStorage
from storages.participants import ParticipantStorage

import psycopg2


class Database(object):

    def __init__(self):
        self.__conn = psycopg2.connect(dbname='tournaments', user='postgres',
                                       password='1', host='localhost')
        self.__cursor = self.__conn.cursor()
        self.tournaments = TournamentStorage(self.__cursor, 'public.tournaments')
        self.teams = TeamStorage(self.__cursor, 'public.teams')
        self.games = GameStorage(self.__cursor, 'public.games')
        self.participants = ParticipantStorage(self.__cursor, 'public.participants')

    def __del__(self):
        self.__conn.commit()
        self.__cursor.close()
        self.__conn.close()
