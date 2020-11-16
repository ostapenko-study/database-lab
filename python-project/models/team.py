import datetime


class Team(object):

    def __init__(self, name: str, tournaments_id: int, registered_at: datetime.datetime, id: int = 0):
        self.name = name
        self.tournaments_id = tournaments_id
        self.registered_at = registered_at
        self.id = id

    def to_string(self):
        return 'id: {}; tournaments_id: {}; registered_at: {};'.\
            format(self.id, self.tournaments_id, self.registered_at)
