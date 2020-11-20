from models.storages.tournaments import TournamentStorage
from models.storages.teams import TeamStorage
from models.storages.games import GameStorage
from models.storages.participants import ParticipantStorage
from models.searches import SearchesModel
from benchmark import benchmark

import psycopg2


class Database(object):

    @benchmark
    def __init__(self):
        self.__conn = psycopg2.connect(dbname='tournaments', user='postgres',
                                       password='1', host='localhost')
        self.__cursor = self.__conn.cursor()
        self.tournaments = TournamentStorage(self.__cursor, 'public.tournaments')
        self.teams = TeamStorage(self.__cursor, 'public.teams')
        self.games = GameStorage(self.__cursor, 'public.games')
        self.participants = ParticipantStorage(self.__cursor, 'public.participants')

        self.searches = SearchesModel(self.__cursor)

    @benchmark
    def __del__(self):
        self.__conn.commit()
        self.__cursor.close()
        self.__conn.close()

    @benchmark
    def generate_tournament(self, count_teams: int, count_games: int):
        _id = self.tournaments.generate()
        array_id_teams = []
        for x in range(0, count_teams):
            array_id_teams += self.teams.generate_in_tournament(_id)
        array_id_games = []
        for x in range(0, count_games):
            array_id_games += self.games.generate_in_tournament(_id)
        return [array_id_teams, array_id_games]

