import datetime


class Participant(object):

    def __init__(self, name: str, surname: str, birthday: datetime.date, id: int = 0):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.id = id

    def to_string(self):
        return 'id: {}; fullname: {} {}; birthday: {};'\
            .format(self.id, self.name, self.surname, self.birthday)
