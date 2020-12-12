from benchmark import benchmark


class GenerateStorage(object):

    def __init__(self, cursor):
        self.__cursor = cursor

    @benchmark
    def generate_tournament(self, count_teams: int, count_playground: int, count_games: int, count_results: int):
        _id = self.__tournaments_generate()
        array_id_teams = []
        print('tournament id : {}'.format(_id))
        for x in range(0, count_teams):
            array_id_teams += self.__teams_generate_in_tournament(_id)
        array_id_playgrounds = []
        for x in range(0, count_playground):
            array_id_playgrounds += self.__playground_generate_in_tournament(_id)
        array_id_games = []
        for x in range(0, count_games):
            array_id_games += self.__games_generate_in_tournament(_id)
        array_id_games_results = []
        for x in range(0, count_results):
            array_id_games_results += self.__match_results_generate_in_tournament(_id)

        return [_id, array_id_teams, array_id_playgrounds, array_id_games, array_id_games_results]

    def __tournaments_generate(self):
        self.__cursor.callproc('generate_tournament')
        return self.__cursor.fetchall()[0]

    def __playground_generate_in_tournament(self, tournament_id: int):
        self.__cursor.callproc('public.generate_playground_in_tournament', (tournament_id,))
        return self.__cursor.fetchall()[0]

    def __teams_generate_in_tournament(self, tournament_id: int):
        self.__cursor.callproc('generate_team_in_tournament', tournament_id, )
        return self.__cursor.fetchall()[0]

    def __games_generate_in_tournament(self, tournament_id: int):
        self.__cursor.callproc('public.generate_match_schedule_record_in_tournament', (tournament_id, ))
        return self.__cursor.fetchall()[0]

    def __match_results_generate_in_tournament(self, tournament_id: int):
        self.__cursor.callproc('public.generate_match_results_record_in_tournament', (tournament_id, ))
        return self.__cursor.fetchall()[0]
