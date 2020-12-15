import datetime
from sqlalchemy import Column, String, Integer, Date, Sequence
from db import Base
import view


class Tournament(Base):
    __tablename__ = 'tournaments'

    id = Column(Integer, Sequence('tournaments_id_seq'), primary_key=True)
    name = Column(String)
    date = Column(Date)

    def __init__(self, name: str, date: datetime, id: int = None):
        self.name = name
        self.date = date
        self.id = id

    def __repr__(self):
        return 'id: {}; name: {}; date: {};' \
            .format(self.id, self.name, self.date)

    @staticmethod
    def input_from_console():
        print('Enter tournament:')
        print('name: ')
        name = view.enter_string()
        print('start date: ')
        date = view.enter_date()
        print('id:')
        id = view.enter_integer()
        return Tournament(name, date, id)