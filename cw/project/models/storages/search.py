from benchmark import benchmark
import datetime


class SearchStorage(object):

    def __init__(self, cursor):
        self.__cursor = cursor

    @benchmark
    def get_statistic_tournaments(self):
        self.__cursor.execute(
            'select * from tournaments '
            'inner join tournaments_statistics '
            'on tournaments.id=tournaments_statistics.tournaments_id '
        )
        return self.__cursor.fetchall(), [desc[0] for desc in self.__cursor.description]

    @benchmark
    def get_statistic_teams_in_tournament(self, _id: int):
        self.__cursor.execute(
            f'select * from teams '
            f'inner join teams_statistics_in_tournament({_id}) as t '
            f'on teams.id = t.teams_id'
        )
        return self.__cursor.fetchall(), [desc[0] for desc in self.__cursor.description]

    @benchmark
    def tournaments_schedule(self, tournaments_id: int):
        self.__cursor.callproc("tournaments_schedule", [tournaments_id, ])
        return self.__cursor.fetchall(), [desc[0] for desc in self.__cursor.description]

    @benchmark
    def tournaments_schedule_in_time_range(self, tournaments_id: int, time_begin: datetime, time_end: datetime):
        self.__cursor.execute(
            f'SELECT * FROM tournaments_schedule({tournaments_id}) '
            f'WHERE scheduled_start BETWEEN \'{time_begin.strftime("%H:%m")}\' AND \'{time_end.strftime("%H:%m")}\' '
            f'ORDER BY scheduled_start'
        )
        return self.__cursor.fetchall(), [desc[0] for desc in self.__cursor.description]

    @benchmark
    def schedule_for_team(self, teams_id: int):
        self.__cursor.execute(
            f'SELECT '
            f'(select name from teams where teams.id=other_teams_id) as other_team_name '
            f', scheduled_start'
            f', (select name from playgrounds where id=playgrounds_id) as playground_name '
            f'FROM all_matches_for_team({teams_id}) '
        )
        return self.__cursor.fetchall(), [desc[0] for desc in self.__cursor.description]

    def schedule_for_playground(self, playgrounds_id: int):
        self.__cursor.execute(
            f'SELECT '
            f'(select name from teams where id=match_schedule.teams_id_1) AS teams_name_1, '
            f'(select name from teams where id=match_schedule.teams_id_2) AS teams_name_2, '
            f'scheduled_start '
            f'FROM match_schedule '
            f'WHERE playgrounds_id={playgrounds_id}'
        )
        return self.__cursor.fetchall(), [desc[0] for desc in self.__cursor.description]
