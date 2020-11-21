import psycopg2
import datetime
from benchmark import benchmark


class SearchesModel:

    def __init__(self, cursor: psycopg2):
        self.cursor = cursor

    @benchmark
    def tournaments_schedule(self, tournaments_id: int):
        self.cursor.callproc("tournaments_schedule", [tournaments_id, ])
        return self.cursor.fetchall()

    @benchmark
    def tournaments_schedule_in_time_range(self, tournaments_id: int, time_begin: datetime, time_end: datetime):
        self.cursor.execute(
            f'SELECT * FROM tournaments_schedule({tournaments_id}) '
            f'WHERE scheduled_start BETWEEN \'{time_begin.strftime("%H:%m")}\' AND \'{time_end.strftime("%H:%m")}\' '
            f'ORDER BY scheduled_start'
        )
        return self.cursor.fetchall()

    @benchmark
    def tournaments_like(self, pattern: str):
        self.cursor.execute(
            f'SELECT * FROM tournaments '
            f'WHERE name LIKE \'{pattern}\';'
        )
        return self.cursor.fetchall()
