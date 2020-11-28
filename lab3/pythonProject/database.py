from models.searches import SearchesModel
from models.storage import Storage
from benchmark import benchmark
from models.entities.tournament import Tournament
from models.entities.team import Team
from models.entities.game import Game

import psycopg2


class Database(object):

    @benchmark
    def __init__(self):
        self.__conn = psycopg2.connect(dbname='tournaments', user='postgres',
                                       password='1', host='localhost')
        self.__cursor = self.__conn.cursor()
        self.tournaments = Storage(Tournament)
        self.teams = Storage(Team)
        self.games = Storage(Game)

        self.searches = SearchesModel(self.__cursor)

    @benchmark
    def __del__(self):
        self.__conn.commit()
        self.__cursor.close()
        self.__conn.close()

    @benchmark
    def generate_tournament(self, count_teams: int, count_games: int):
        _id = self.__tournaments_generate()
        array_id_teams = []
        print('tournament id : {}'.format(_id))
        for x in range(0, count_teams):
            array_id_teams += self.__teams_generate_in_tournament(_id)
        array_id_games = []
        for x in range(0, count_games):
            array_id_games += self.__games_generate_in_tournament(_id)
        return [_id, array_id_teams, array_id_games]

    def __tournaments_generate(self):
        self.__cursor.callproc('generate_tournament')
        return self.__cursor.fetchall()[0]

    def __teams_generate_in_tournament(self, tournament_id: int):
        self.__cursor.callproc('generate_team_for_tournament', tournament_id, )
        return self.__cursor.fetchall()[0]

    def __games_generate_in_tournament(self, tournament_id: int):
        self.__cursor.callproc('public.generate_game_for_tournament', (tournament_id, ))
        return self.__cursor.fetchall()[0]
