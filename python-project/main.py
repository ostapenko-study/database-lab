from models.participant import Participant
from models.tournament import Tournament
from models.game import Game
from models.team import Team

from database import Database

import datetime

team = Team('Dogs', 1, datetime.datetime.now())
t = Tournament('Kiev Cup', datetime.date(2021, 6, 7), 6)
p = Participant('Ivan', 'Petrov', datetime.date(2000, 6, 7))
g = Game(1, 1, 2, 1, datetime.datetime(2020, 6, 7, 14, 0), 1)

database = Database()
