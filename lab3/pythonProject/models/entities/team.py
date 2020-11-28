import datetime
from sqlalchemy import Column, String, Integer, DateTime, Sequence, ForeignKey
from base import Base
import view


class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, Sequence('teams_id_seq'), primary_key=True)
    name = Column(String)
    tournaments_id = Column(Integer, ForeignKey('tournaments.id'))
    registered_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name: str, tournaments_id: int, registered_at: datetime.datetime, id: int = None):
        self.name = name
        self.tournaments_id = tournaments_id
        self.registered_at = registered_at
        self.id = id

    def to_string(self):
        return 'id: {}; tournaments_id: {}; registered_at: {};'.\
            format(self.id, self.tournaments_id, self.registered_at)

    @staticmethod
    def input_from_console():
        print('Enter team:')
        print('name: ')
        name = view.enter_string()
        print('tournaments_id: ')
        tournaments_id = view.enter_integer()
        print('id:')
        id = view.enter_integer()
        registered_at = datetime.datetime.now()
        print('registered_at : {}', (registered_at, ))
        return Team(name, tournaments_id, registered_at, id)
