from sqlalchemy import Column, Integer, DateTime, Sequence, ForeignKey, String
from db import Base


class Playground(Base):
    __tablename__ = "playgrounds"

    id = Column(Integer, Sequence('playgrounds_id_seq'), primary_key=True)
    name = Column(String)
    tournaments_id = Column(Integer, ForeignKey("tournaments.id"))

    def __init__(self, name: str, tournaments_id: int, id: int = None):
        self.name = name
        self.tournaments_id = tournaments_id
        self.id = id