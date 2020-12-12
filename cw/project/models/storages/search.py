from benchmark import benchmark
import datetime


class SearchStorage(object):

    def __init__(self, cursor):
        self.__cursor = cursor

    @benchmark
    def get_statistic_tournaments(self):
        self.__cursor.execute(
                'select * from tournaments_statistics'
        )
        return self.__cursor.fetchall(), [desc[0] for desc in self.__cursor.description]

    @benchmark
    def get_statistic_teams_in_tournament(self, _id: int):
        self.__cursor.execute(
                f'select * from teams_statistics_in_tournament({_id})'
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
