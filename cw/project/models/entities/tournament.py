import datetime
from sqlalchemy import Column, String, Integer, Date, Sequence
from db import Base


class Tournament(Base):
    __tablename__ = 'tournaments'

    id = Column(Integer, Sequence('tournaments_id_seq'), primary_key=True)
    name = Column(String)
    date = Column(Date)

    # def __repr__(self):
    #     return "<Tournaments(name='%s', date='%s')>" % \
    #            (self.name, self.date)

    def __init__(self, name: str, date: datetime, id: int = None):
        self.name = name
        self.date = date
        self.id = id

