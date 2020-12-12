import datetime
from sqlalchemy import Column, Integer, Time, Sequence, ForeignKey
from db import Base


class MatchSchedule(Base):
    __tablename__ = 'match_schedule'

    id = Column(Integer, Sequence('match_schedule_id_seq'), primary_key=True)
    teams_id_1 = Column(Integer, ForeignKey('teams.id'))
    teams_id_2 = Column(Integer, ForeignKey('teams.id'))
    scheduled_start = Column(Time)
    playgrounds_id = Column(Integer, ForeignKey('playgrounds.id'))
    tournaments_id = Column(Integer, ForeignKey("tournaments.id", ondelete='CASCADE'))

    def __init__(self, teams_id_1: int, teams_id_2: int,
                 scheduled_start: datetime.datetime,
                 playgrounds_id: int, id: int = None):
        self.teams_id_1 = teams_id_1
        self.teams_id_2 = teams_id_2
        self.scheduled_start = scheduled_start
        self.playgrounds_id = playgrounds_id
        self.id = id
