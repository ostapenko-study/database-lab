import datetime
from sqlalchemy import Column, String, Integer, Date, Sequence, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db import Base


class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, Sequence('teams_id_seq'), primary_key=True)
    name = Column(String)
    tournaments_id = Column(Integer, ForeignKey('tournaments.id', ondelete='CASCADE'))
    registered_at = Column(DateTime, default=datetime.datetime.utcnow)

    child = relationship("Tournaments")

    # def __repr__(self):
    #     return "<Team(name='%s', tournaments_id='%s', registered_at='%s')>" % (
    #                             self.name, self.tournaments_id, self.registered_at)

    def __init__(self, name: str, tournaments_id: int, registered_at: datetime.datetime, id: int = None):
        self.name = name
        self.tournaments_id = tournaments_id
        self.registered_at = registered_at
        self.id = id