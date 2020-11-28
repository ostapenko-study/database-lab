# import datetime
# from models.entities.tournament import Tournament
# from base import Session
#
# tournament = Tournament("Kiev Cup", datetime.date(2020, 10, 10))
#
# session = Session()
#
# session.add(tournament)
#
# session.commit()
# session.close()
from database import Database
from controllers.controller import Controller

database = Database()

controller = Controller(database)

controller.loop()
