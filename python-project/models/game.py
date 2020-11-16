import datetime


class Game(object):

    def __init__(self, tournament_id: int, teams_id_1: int, teams_id_2: int, playground_id: int,
                 scheduled_start: datetime.datetime, id: int = 0):
        self.tournament_id = tournament_id
        self.teams_id_1 = teams_id_1
        self.teams_id_2 = teams_id_2
        self.playground_id = playground_id
        self.scheduled_start = scheduled_start
        self.id = id

    def to_string(self):
        return 'id: {}; tournament_id: {}; teams_id_1: {}; teams_id_2: {}; playground_id: {}; scheduled_start: {}' \
            .format(self.id, self.tournament_id, self.teams_id_1, self.teams_id_2, self.playground_id,
                    self.scheduled_start)
