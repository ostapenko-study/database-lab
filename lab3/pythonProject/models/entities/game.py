import datetime
from sqlalchemy import Column, Integer, String, DateTime, Date, Sequence, ForeignKey
from base import Base
import view


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, Sequence('games_id_seq'), primary_key=True)
    teams_id_1 = Column(Integer, ForeignKey('teams.id'))
    teams_id_2 = Column(Integer, ForeignKey('teams.id'))
    scheduled_start = Column(DateTime)

    def __init__(self, teams_id_1: int, teams_id_2: int,
                 scheduled_start: datetime.datetime, id: int = None):
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
        teams_id_1 = view.enter_integer()
        print('teams_id_2: ')
        teams_id_2 = view.enter_integer()
        print('scheduled_start: ')
        scheduled_start = view.enter_time()
        print('id:')
        id = view.enter_integer()
        return Game(teams_id_1, teams_id_2, scheduled_start, id)
