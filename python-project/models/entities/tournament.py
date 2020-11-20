import datetime
from models.entities.abstract_object import AObject
import view as View


class Tournament(AObject):

    def __init__(self, name: str, date: datetime, id: int = 0):
        self.name = name
        self.date = date
        self.id = id

    def to_string(self):
        return 'id: {}; name: {}; date: {};'\
            .format(self.id, self.name, self.date)

    @staticmethod
    def input_from_console():
        print('Enter tournament:')
        print('name: ')
        name = View.enter_string()
        date = View.enter_date()
        print('id:')
        id = View.enter_integer()
        return Tournament(name, date, id)
