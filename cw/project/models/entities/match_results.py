import datetime
from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey
from db import Base


class MatchResults(Base):
    __tablename__ = 'match_results'

    match_schedule_id = Column(Integer, ForeignKey("match_schedule.id", ondelete='CASCADE'), primary_key=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    points_1 = Column(Integer)
    points_2 = Column(Integer)

    def __init__(self, teams_id_1: int, teams_id_2: int,
                 scheduled_start: datetime.datetime, id: int = None):
        self.teams_id_1 = teams_id_1
        self.teams_id_2 = teams_id_2
        self.scheduled_start = scheduled_start
        self.id = id

