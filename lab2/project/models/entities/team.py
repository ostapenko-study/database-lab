import datetime
from models.entities.abstract_object import AObject
import view as View


class Team(AObject):

    def __init__(self, name: str, tournaments_id: int, registered_at: datetime.datetime, id: int = 0):
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
        name = View.enter_string()
        print('tournaments_id: ')
        tournaments_id = View.enter_integer()
        print('id:')
        id = View.enter_integer()
        registered_at = datetime.datetime.now()
        print('registered_at : {}', (registered_at, ))
        return Team(name, tournaments_id, registered_at, id)
