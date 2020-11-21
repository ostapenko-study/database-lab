import datetime
from models.entities.abstract_object import AObject
import view as View


class Game(AObject):

    def __init__(self, teams_id_1: int, teams_id_2: int,
                 scheduled_start: datetime.datetime, id: int = 0):
        self.teams_id_1 = teams_id_1
        self.teams_id_2 = teams_id_2
        self.scheduled_start = scheduled_start
        self.id = id

    def to_string(self):
        return 'id: {}; teams_id_1: {}; teams_id_2: {}; scheduled_start: {}' \
            .format(self.id, self.teams_id_1, self.teams_id_2, self.scheduled_start)

    @staticmethod
    def input_from_console():
        print('Enter game:')
        print('teams_id_1: ')
        teams_id_1 = View.enter_integer()
        print('teams_id_2: ')
        teams_id_2 = View.enter_integer()
        print('scheduled_start: ')
        scheduled_start = View.enter_time()
        print('id:')
        id = View.enter_integer()
        return Game(teams_id_1, teams_id_2, scheduled_start, id)
