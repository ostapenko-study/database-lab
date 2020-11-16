import datetime


class Tournament(object):

    def __init__(self, name: str, date: datetime, id: int = 0):
        self.name = name
        self.date = date
        self.id = id

    def to_string(self):
        return 'id: {}; name: {}; date: {};'\
            .format(self.id, self.name, self.date)
