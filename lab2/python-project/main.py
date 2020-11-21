from database import Database
from controllers.controller import Controller

database = Database()

controller = Controller(database)

controller.loop()
